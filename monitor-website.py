import requests
import smtplib
import os
import paramiko
import digitalocean
import time

# response.status_code == 200:
#   print("Application is running successfully! ")
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
DIGITAL_OCEAN_TOKEN = os.environ.get('DIGITAL_OCEAN_TOKEN')


def send_notification(email_msg):
    print('sending an email....')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"subject: SITE DOWN\n{email_msg}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    global ssh
    try:
        print('Restarting the application....')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('204.48.20.211', username='root', key_filename=r'C:\Users\Rajib\.ssh\id_rsa')
        stdin, stdout, stderr = ssh.exec_command('docker start 76528853')
        print(stdout.readline())

    except paramiko.AuthenticationException as auth_error:
        print(f"Authentication failed: {auth_error}")
    except paramiko.SSHException as ssh_error:
        print(f"SSH connection failed: {ssh_error}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()


# response.status_code == 200:
try:
    response = requests.get('http://204.48.20.211:8080/')
    if response.status_code == 200:
        print("Application is running successfully! ")
    else:
        print("Application is down!. fix it")
        # send email to meEMAIL_PASSWORD
        msg = f"Application returned {response.status_code}"
        send_notification(msg)

        # restart the application
        restart_container()


except Exception as ex:
    print(f"Connection error happened: {ex}")
    msg = "Application not accessible at all"
    send_notification(msg)

    # restart the digitalOcean server
    print("rebooting the server")
    client = digitalocean.Manager(token=DIGITAL_OCEAN_TOKEN)
    droplet = client.get_droplet(droplet_id="376528853")
    droplet.reboot()

    droplet.load()
    while True:
        droplet = client.get_droplet(droplet_id="376528853")
        if droplet.status == 'active':
            droplet.load()
            time.sleep(5)
            restart_container()
            break
        time.sleep(5)  # Add a sleep statement to avoid constant polling
