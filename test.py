import requests

url = 'http://127.0.0.1:5000/emotionDetector' 
data = {'text': 'I think I am having fun'}  

response = requests.post(url, json=data)

print(response.text)
