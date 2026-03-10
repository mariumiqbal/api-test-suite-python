import requests
import json

id = [1,999]
listResponse = []
for i in id:
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
    data = response.json()
    
    if response.status_code == 200:
        listResponse.append({"status": "success", "data": data})
        print(data)
    elif response.status_code == 404:
        listResponse.append({"status": "not_found", "id": i, "data": None})
        print("Post not found")
    else:
        listResponse.append({"status": "error", "code": response.status_code, "data": None})
        print(f"Unexpected error: {response.status_code}")
with open("response_log.json", "w") as file:
    json.dump(listResponse, file, indent=4)    


# Your code here:
# If status is 200 → print the data
# If status is 404 → print "Post not found"
# If anything else → print "Unexpected error: " + the status code