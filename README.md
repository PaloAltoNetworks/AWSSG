# AWSSG
Update AWS SG to quarantine hosts based upon trigger from FW threat log Edit Add topics

This example code may be used in combination with Action-Oriented Log Forwarding on a Palo Alto Networks Firewall to automatically change the Security Group (SG) assocaited with an compromised host when a threat is detected by the firewall. The HTTP Server Profile on the firewall is configured to include the relevant information in the POST request body. The code is imported as part of an HTTP-triggered Lambda function. When activated by a message from the firewall, it will extract the relevant information from the request body, and make the API call to AWS to update the network interface and quarantine the host.

The code does not have any additional requirements/libraries other than those already provided by Azure.

Additional Information:

http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html

Support Policy

This template is released under an as-is, best effort, support policy. It should be seen as community supported and Palo Alto Networks will contribute our expertise as and when possible. We do not provide technical support or help in using or troubleshooting the components of the project through our normal support options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) partners and backline support options. The underlying product used (the VM-Series firewall) by the scripts or templates are still supported, but the support is only for the product functionality and not for help in deploying or using the template or script itself. Unless explicitly tagged, all projects or work posted in our GitHub repository (at https://github.com/PaloAltoNetworks) or sites other than our official Downloads page on https://support.paloaltonetworks.com are provided under the best effort policy.
