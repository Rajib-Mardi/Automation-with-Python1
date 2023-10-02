###  Project: 
  * Automate displaying EKS cluster information
### Technologiesused: 
  * Python, Boto3, AWS EKS

###  Project Description: 
* Write a Python script that fetches and displays EKS cluster status and information

  
* Create eks cluster  with Terraform

1. Import the ```boto3``` Library:

  * ```import boto3```: This line imports the Boto3 library, which is necessary for interacting with AWS services.
    
2. Create an Amazon EKS Client:

```client = boto3.client('eks', region_name="eu-west-3")```: This line creates an Amazon EKS client for the "eu-west-3" region using the ```boto3.client``` method. The ```eks``` client allows you to interact with Amazon EKS clusters.

3. List Amazon EKS Clusters:

```clusters = client.list_clusters()['clusters']```: This line calls the ```list_clusters``` method on the client object to retrieve a list of Amazon EKS cluster names. The result is stored in the ```clusters``` variable.

4. Iterate Through the Clusters:

 * The script then enters a loop to iterate through the list of cluster names obtained in the previous step.\
   
5. Retrieve Cluster Information:

   * Within the loop, the script calls the ```describe_cluster``` method on the ```client``` object to retrieve detailed information about each cluster, including its status, endpoint, and version.
   * The ```name``` parameter is set to the current cluster name within the loop to specify which cluster to describe.
   * The response from ```describe_cluster``` is stored in the ```response``` variable.
  
6. Extract Cluster Information:
    * The script extracts specific information about the cluster from the response:
        * ```cluster_info = response['cluster']```: This line extracts the cluster information dictionary from the response.
        * ```cluster_status = cluster_info['status']```: It retrieves the status of the cluster.
        * ```cluster_endpoint = cluster_info['endpoint']```: It retrieves the endpoint (API server endpoint) of the cluster.
        * ```cluster_version = cluster_info['version']```: It retrieves the Kubernetes version of the cluster.
          
7. Print Cluster Information:

* The script then prints the extracted cluster information, including its status, endpoint, and version for each cluster.




* This script lists all Amazon EKS clusters in the "eu-west-3" region, collects detailed information about each cluster, and prints the status, endpoint, and Kubernetes version of each cluster.
