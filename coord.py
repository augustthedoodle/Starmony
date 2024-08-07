import requests

# Build the API URL
url = "http://localhost:8090/api/objects/info?name=leo&format=json"

# Send the API request and get the response
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Extract the latitude and longitude of the result
    latitude = data["ra"]
    longitude = data["dec"]

    print(f"Latitude: {latitude}, Longitude: {longitude}")
else:
    print(f"Request failed with status code {response.status_code}")