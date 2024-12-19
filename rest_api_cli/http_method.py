import requests
import json

def perform_request(method, url, headers={}, data=None):
    """Perform the HTTP request based on the method."""
    
    # Set Content-Type to application/json for POST, PUT, PATCH
    if method in ['POST', 'PUT', 'PATCH'] and data:
        headers['Content-Type'] = 'application/json'
    
    # Convert data to JSON if it's provided
    if data:
        data = data if isinstance(data, dict) else json.loads(data)

    response = None
    try:
        if method == 'GET':
            response = requests.get(url, headers)
        elif method == 'POST':
            response = requests.post(url, headers, data)
        elif method == 'PUT':
            response = requests.put(url, headers, data)
        elif method == 'DELETE':
            response = requests.delete(url, headers)
        elif method == 'PATCH':
            response = requests.patch(url, headers, data)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    return response
