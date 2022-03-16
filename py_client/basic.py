import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"


# Rest APIs = -> Web API
get_response = requests.get(endpoint, json={"query": "Hello world"}) # API request - HTTP request
print(get_response.text) # Print raw text response

"""
HTTP Request -> HTML
Rest API HTTP Request -> Json (sometimes xml)
"""
print(get_response.json()) # Print raw text response
print(get_response.status_code)