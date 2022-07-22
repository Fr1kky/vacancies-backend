import requests


get_rate_url = "http://127.0.0.1:5000/v1/get_vacancy"
response = requests.get(get_rate_url)

print(response)
print(response._content)

get_vacancy_url = "http://127.0.0.1:5000/v1/get_vacancy"
response = requests.get(get_vacancy_url)

print(response)
print(response._content)

get_rank_url = "http://127.0.0.1:5000/v1/get_rank"
response = requests.post(get_rank_url, json={"salary_starts_from": 1500})

print(response)
print(response._content)
