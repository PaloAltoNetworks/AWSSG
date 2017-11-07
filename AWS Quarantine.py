from __future__ import print_function

import datetime
import boto3
import json

client = boto3.client('ec2')

print('Loading function')

# This handler converts the time format returned by AWS into something json-formattable
def datetime_handler(str_input):
    if isinstance(str_input, datetime.datetime):
        return str_input.isoformat()
    raise TypeError("Unknown type")

# This is the main handler
def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    # Convert the data coming from the API gateway into something we can manipulate
    tempvar = json.loads(event['body'])
    # source IP of the misbehaving system
    attacker = tempvar['Attacker']
    # security group id that will be used to quarantine the host
    sgid = tempvar['SGID']
    # print("attacker = ", attacker)
    # print("sgid = ", sgid)
    # Get information regarding the network interfaces, filtering on the IP of the bad actor
    response = client.describe_network_interfaces(
        Filters=[{'Name': 'addresses.private-ip-address', 'Values': [attacker]}]
    )
    # Focus on the section of interest 
    network_interface_info_dict = response["NetworkInterfaces"][0]
    # Convert the results into something we can more easily manage
    network_interface_info_string = json.dumps(network_interface_info_dict, default=datetime_handler)
    network_interface_info_json = json.loads(network_interface_info_string)
    # Pull out the network interface id associated with the IP of the bad actor
    interface_id = network_interface_info_json['NetworkInterfaceId']
    # Replace the existing security group wit the one that quarantines the bad actor
    response = client.modify_network_interface_attribute(
        Groups=[sgid],
        NetworkInterfaceId=interface_id
    )
    # Log the response for posterity
    print(response)
    #print(network_interface_info_json)

    # Return a status code to the API gateway
    return {
        "statusCode": 200, 
        "headers": {"Content-Type": "application/json"},
        "body": "body_text_goes_here"
    }