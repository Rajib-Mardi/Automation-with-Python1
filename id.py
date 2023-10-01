import requests

# Replace with your DigitalOcean API token
api_token = 'dop_v1_03a6d9314d7660c7d87d8855f735aacf1dddcd08b0a4ff920fe8352ab965f941'

# Define the DigitalOcean API endpoint to list Droplets
url = 'https://api.digitalocean.com/v2/droplets'

# Define the headers with your API token
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

try:
    # Send a GET request to list Droplets
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        droplets = response.json()['droplets']
        for droplet in droplets:
            droplet_id = droplet['id']
            droplet_name = droplet['name']
            print(f'Droplet ID: {droplet_id}, Droplet Name: {droplet_name}')
    else:
        print(f'Failed to retrieve Droplet list. Status code: {response.status_code}')

except Exception as e:
    print(f'An error occurred: {e}')
