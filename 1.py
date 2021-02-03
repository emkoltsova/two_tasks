import requests


r = requests.get('https://jsonplaceholder.typicode.com/posts')

result = r.json()

print("One item:")
print(result[35])

print("All id + title:")
for item in result:
    print(item["id"], item["title"])
