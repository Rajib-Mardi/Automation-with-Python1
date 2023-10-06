### Project:
  * Website Monitoring and Recovery 
### Technologiesused: 
 * Python, Linode, Docker, Linux

### Project Description:
* Create a server on a cloud platform

* Install Docker and run a Docker container on the remote serve


1. Importing Libraries:

   * The script starts by importing necessary libraries, including ```requests``` for making HTTP requests, ```smtplib``` for sending email notifications, ```os``` for handling environment variables, ```paramiko``` for SSH connections, ```linode_api4``` for Linode API interactions, ```time``` for time-related operations, and ```schedule``` for scheduling tasks.
     
2. Environment Variables:
   
   * It retrieves certain sensitive information (email address, email password, and Linode API token) from environment variables, which should be set in the environment where this script runs.
     
3. restart_server_and_container() Function:

  * This function is responsible for restarting both the Linode server and the application container. It performs the following tasks:
       * Reboots the Linode server using the Linode API. It loads the server with a specific ID (24920590) and calls ```nginx_server.reboot()``` to initiate the reboot.
       * After initiating the server reboot, it enters a loop that continuously checks the server's status.
       * Once the server's status becomes 'running,' it sleeps for 5 seconds to allow the server to stabilize and then calls ```restart_container()``` to restart the application container.
         
4. send_notification(email_msg) Function:

This function sends an email notification using a Gmail SMTP server.
It requires the Gmail email address and password for authentication.
restart_container() Function:

This function restarts a Docker container on a remote server using SSH.
It connects to the server using SSH, starts the Docker container with a specific ID, and prints the output.
monitor_application() Function:

This function monitors the web application's availability.
It sends an HTTP GET request to the specified URL (the web application's address).
If the response status code is 200 (OK), it prints a message indicating that the application is running successfully.
If the response status code is not 200, it indicates that the application is down or not working as expected.
In this case, it sends an email notification with information about the response status code and then calls restart_container() to attempt to restart the application.
If any exception occurs during the process (e.g., a connection error), it sends an email notification and calls restart_server_and_container() to reboot both the server and the container.
Scheduling:

The script uses the schedule library to schedule the monitor_application() function to run every 5 minutes.
It enters a loop where schedule.run_pending() is called, which executes any scheduled tasks when their time comes.


