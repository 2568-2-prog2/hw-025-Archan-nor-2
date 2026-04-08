import requests

url = "http://127.0.0.1:8080/roll_dice"

data = {
    "probabilities": [0.1,0.2,0.3,0.1,0.2,0.1],
    "number_of_random": 5
}

r = requests.get(url, json=data)
print(r.json())