import json

login_response_str = '{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9", "expires_in": 3600, "status": "active"}'

# loads - converts json string to dictionary object
print(type(login_response_str))
result = json.loads(login_response_str)
print(type(result))
print(result['status'])


error_response_str = '{"error": {"code": 404, "message": "User not found", "type": "InvalidRequestException"}}'
result1 = json.loads(error_response_str)
print(result1['error']['message'])