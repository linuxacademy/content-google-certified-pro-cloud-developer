from os import environ
from time import sleep
import requests

receiving_service_url = environ.get("SECRET_URL")

# Set up metadata server request
# See https://cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature
metadata_server_token_url = 'http://metadata/computeMetadata/v1/instance/service-accounts/default/identity?audience='

token_request_url = metadata_server_token_url + receiving_service_url
token_request_headers = {'Metadata-Flavor': 'Google'}

# Fetch the token
token_response = requests.get(token_request_url, headers=token_request_headers)
jwt = token_response.content.decode("utf-8")

# Provide the token in the request to the receiving service
receiving_service_headers = {'Authorization': f'bearer {jwt}'}

while True:
    response = requests.get(receiving_service_url, headers=receiving_service_headers)
    print(response.text)
    sleep(5)


