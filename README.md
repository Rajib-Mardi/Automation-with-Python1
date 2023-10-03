
###  Project: 
  * Data Backup & Restore
### Technologiesused: 
Project Description:
  * Python, Boto3, AWS

### Project Description:
  ### Write a Python script that automates creating backups for EC2 Volumes


 *  Create a ec2 instance in aws manually  and tag the name of volume as the "prod" and use pyhon script to create a snapshot out of it

* It creates snapshots of volumes that are tagged with the name "prod." It employs the "schedule" library to schedule and run the volume snapshot creation process at regular intervals.

1. Import Libraries:

   * ```import boto3```: This line imports the Boto3 library, which is the AWS SDK for Python, allowing interaction with AWS services.
import schedule: This library is used for task scheduling.

2. Create an EC2 Client:

   * ```ec2_client = boto3.client('ec2', region_name="eu-west-3")```: This line creates an EC2 client object for the "eu-west-3" region using the Boto3 library. It will be used to interact with AWS EC2 services in that region.

3. Define the ```create_volume_snapshot``` Function:

   * This function is responsible for creating snapshots of EC2 volumes tagged with the name "prod."
   * It uses the ```describe_volumes``` method of the ```ec2_client``` to retrieve information about volumes that match the specified filter criteria. In this case, it's looking for volumes with the tag "Name" equal to "prod."
   * It then iterates through the retrieved volumes and uses the ```create_snapshot``` method of the ```ec2_client``` to create a snapshot of each volume.
   * For each snapshot created, it prints information about the new snapshot, including its ID.
     
4.  the ```create_volume_snapshot``` Function:

  * ```schedule.every(30).seconds.do(create_volume_snapshot)```: This line schedules the ```create_volume_snapshot``` function to run every 30 seconds using the ```schedule``` library. This means that the function will be executed periodically at a 30-second interval.
    
5. Run the Scheduled Tasks in an Infinite Loop:

* ```while True:```: This is an infinite loop that continuously runs.
* Inside the loop, ```schedule.run_pending()``` is called. This method checks if there are any scheduled tasks (in this case, the ```create_volume_snapshot``` function) that need to be executed. If there are any pending tasks, they are executed.



![Automation-with-Python – volume-backups py 02-10-2023 23_13_51](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/ad742853-f0d6-490b-b72b-cd2b3ed5f9bc)

 

------------------------------------------------------------------

#### Write a Python script that cleans up old EC2 Volume snapshots
1. Import Libraries:

    * ```import boto3```: This line imports the Boto3 library, which is the AWS SDK for Python, allowing interaction with AWS services.
    * ```from operator import itemgetter```: This line imports the ```itemgetter``` function from the ```operator``` module, which will be used to sort snapshots by their start times.
      
2. Create an EC2 Client:

    * ```ec2_client = boto3.client('ec2', region_name="eu-west-3")```: This line creates an EC2 client object for the "eu-west-3" region using Boto3. It will be used to interact with AWS EC2 services in that region.
      
3. List EBS Volumes with the 'prod' Tag:

   * ```volumes = ec2_client.describe_volumes(...)```: This code calls the ```describe_volumes``` method on the ```ec2_client``` to retrieve information about EBS volumes that match the specified filter criteria. It looks for volumes with the tag "Name" equal to "prod."
     
4. Iterate Through Matching Volumes:

  * The script enters a loop to iterate through the volumes that match the filter criteria.\
    
5. List Snapshots for Each Volume:

    * For each volume, the script calls the ```describe_snapshots``` method on the ```ec2_client``` to retrieve information about snapshots associated with that volume.
    * It specifies that it wants snapshots owned by 'self' (meaning the AWS account running the script) and filtered by the volume ID of the current volume in the loop.
      
6. Sort Snapshots by Start Time:

   * The script sorts the snapshots returned by ```describe_snapshots``` by their ```StartTime``` in reverse order (from newest to oldest).
   * The ```sorted_by_date``` variable contains the sorted list of snapshots.
     
7. Delete Older Snapshots (Keeping the Two Most Recent):

   * The script then iterates through the sorted snapshots starting from the third snapshot (index 2). It excludes the two most recent snapshots and deletes the older ones.
   * For each older snapshot, it calls the ```delete_snapshot``` method on the ```ec2_client``` to delete the snapshot.
   * The ```response```variable contains the result of the deletion operation.
     
8. Print Deletion Responses:

   * The script prints the response received from AWS for each snapshot deletion operation.
  

* This script is a basic form of EBS snapshot management. It identifies EBS volumes tagged as "prod," lists their associated snapshots, sorts the snapshots by their start times, and deletes all but the two most recent snapshots. This can be useful for managing snapshot retention and saving storage costs.


![Automation-with-Python – cleanup-snapshots py 02-10-2023 23_20_55](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/20f2b228-b769-4259-b7f9-aeaa4835107d)


-----------------------------------------------------------------------------

* This Python script uses the Boto3 module to interface with Amazon Web Services (AWS) to generate a new Amazon Elastic Block Store (EBS) volume from the most recent snapshot of an existing EBS volume. The new volume is then attached to an EC2 instance.

1. ```Import  Libraries```:

     * ```import boto3```: This line imports the Boto3 library, which is the AWS SDK for Python.
     * ```from operator import itemgetter```: It imports the ```itemgetter``` function from the ```operator``` module, which will be used for sorting snapshots by their start times.
  

2. Create an EC2 Client and Resource:

     * ```ec2_client = boto3.client('ec2', region_name="eu-west-3")```: This code creates an EC2 client object for the "eu-west-3" region using Boto3. It will be used for various EC2-related operations.
     * ```ec2_resource = boto3.resource('ec2', region_name="eu-west-3")```: This line creates an EC2 resource object, which provides a higher-level API for managing EC2 resources.
       
3. Define the Instance ID:

   * ```instance_id = 'i-0e7beb3c9b658e98d'```: This is the ID of the EC2 instance to which you want to attach the new EBS volume.

4. Describe Volumes Attached to the Instance:

    * The script calls ```describe_volumes``` on the ```ec2_client``` to retrieve information about EBS volumes attached to the specified EC2 instance (```instance_id```).
    * It filters the volumes based on the ```attachment.instance-id``` filter, ensuring it only gets volumes attached to the specified instance.
    * It extracts the first volume (assuming only one volume is attached) and assigns it to ```instance_volume```.
  
      
5. Describe Snapshots of the Instance Volume:

    * The script uses ```describe_snapshots``` to retrieve information about snapshots owned by 'self' (the current AWS account) and associated with the ```instance_volume``` extracted in the previous step.
    * It sorts these snapshots by their ```StartTime``` in reverse order, placing the most recent snapshot first, and assigns it to latest_snapshots.
  
      
6.  Print the Start Time of the Latest Snapshot:

     * The script prints the ```StartTime``` of the latest snapshot to the console.

7. Create a New EBS Volume from the Latest Snapshot:

     * ec2_client.create_volume is called to create a new EBS volume based on the ```latest_snapshots```. It specifies:
           * ```SnapshotId```: The ID of the latest snapshot from which the new volume is created.
           * ```AvailabilityZone```: The availability zone where the new volume should be created.
           * ```TagSpecifications```: Tags to be applied to the new volume, in this case, setting the name tag to "prod."

       
8. Wait for the New Volume to Become 'available':

    * The script enters a loop to repeatedly check the state of the new volume.
    * It uses ```ec2_resource.Volume(new_volume['VolumeId'])``` to create an EC2 resource object for the new volume.
    * It checks the state of the volume using ```vol.state```.
    * If the volume state becomes 'available,' it proceeds to attach the volume to the EC2 instance.
    * The script breaks out of the loop and attaches the volume using ```ec2_resource.Instance(instance_id).attach_volume```.
  

* This script automates the process of establishing a new EBS volume from the most recent snapshot of an existing volume, waiting for the new volume to become available, and attaching it to an EC2 instance. 


![Automation-with-Python – restore-volume py 02-10-2023 23_45_03](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/365d8053-f15e-4fa3-b7d3-e240da38743a)


![Volumes _ EC2 _ eu-west-3 - Google Chrome 02-10-2023 23_52_22](https://github.com/Rajib-Mardi/Automation-with-Python1/assets/96679708/2c6bf65b-3358-4dd7-9143-dbd6ab2ff6ea)


