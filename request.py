import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':12, 'test_score':9, 'interview_score':9})

print(r.json())