import requests

BASE_URL = "http://127.0.0.1:5000/"
'''
data = [{"likes": 10, "name":"Tim", "views": 100},
        {"likes": 210, "name":"Joe", "views": 10220},
        {"likes": 34, "name":"Brian", "views": 1003},
        {"likes": 12, "name":"Karen", "views": 10410},
        {"likes": 12424, "name":"How to make REST APIs", "views": 1051160}]

for i in range(len(data)):
    response = requests.put(BASE_URL + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE_URL + 'video/6')
print(response.json())
'''

response = requests.patch(BASE_URL+"video/2", {"views": 99, "likes": 1})
print(response.json())