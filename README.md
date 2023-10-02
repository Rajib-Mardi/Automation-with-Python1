### Project: 
  * Automate configuring EC2 Server Instances
### Technologiesused:
  * Python, Boto3, AWS

### Project Description:
* Write a Python script that automates adding environment tags to all EC2 Server instances


1. Import the ```boto3``` Library:

* ```import boto3```: This line imports the Boto3 library, which is necessary for interacting with AWS services.
2. Create EC2 Clients and Resources for Paris and Frankfurt Regions:

*  EC2 clients and resources are created, one for the Paris region (eu-west-3) and one for the Frankfurt region (eu-central-1). These clients and resources will be used to interact with EC2 instances in their respective regions.

3. Retrieve Instance IDs in the Paris Region:

  * The script retrieves a list of instance IDs in the Paris region by calling ```describe_instances```  on the ```ec2_client_paris``` object.
  * It iterates through the reservations and instances to collect the instance IDs in the   ```instance_ids_paris``` list

4. Apply Tags to Instances in the Paris Region:

    * The script applies a "prod" environment tag to the instances in the Paris region using the ```create_tags``` method of the ```ec2_resource_paris``` object.
    * The  ```Resources``` parameter specifies the instance IDs to which the tags will be applied.

5. Retrieve Instance IDs in the Frankfurt Region:

    * Similarly, the script retrieves a list of instance IDs in the Frankfurt region using ```describe_instances``` on the  ```ec2_client_frankfurt``` object.

6.  Apply Tags to Instances in the Frankfurt Region:

    * The script applies a "dev" environment tag to the instances in the Frankfurt region using the ```create_tags``` method of the ```ec2_resource_frankfurt``` object, similar to what was done for the Paris region.
  
 * This script connects with AWS in two separate regions, lists EC2 instance IDs in each location, and tags those instances based on their environment (prod or dev). This categorization might be beneficial for organizing and managing AWS resources based on their uses or contexts.

![describe_instance_status - Boto3 1 28 51 documentation - Google Chrome 21-09-2023 10_20_20](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/c6452197-b805-4440-8b85-df3b0a09ef8a) 


![describe_instance_status - Boto3 1 28 51 documentation - Google Chrome 21-09-2023 10_20_36](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/1d4bf127-f3d0-41e7-87c0-798513f58ea1)



