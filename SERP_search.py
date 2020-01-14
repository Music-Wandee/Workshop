import requests
url = "https://api.serphouse.com/serp/live"
#payload = '{"data": { "domain":"google.com", "lang":"th", "q": " \\"กินดี\\" site:pantip.com after:2017-12-31 before:2019-1-1", "loc":"Bangkok,Thailand", "device": "desktop", "serp_type": "web"}}'
payload = '{"data": { "domain":"google.com", "lang":"th", "q": "กินดี", "loc":"Bangkok,Thailand", "device": "desktop", "serp_type": "web", "page": "2"}}'

headers = {
	'accept': "application/json",
	'content-type': "application/json",
	'authorization': "Bearer rgDe4q7BbPW7tBi5Z6cieTkZdTnQA5GKmAjTjAlWiYpUvPAEIxKz1hmxaneK",
}

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
print(response.text)

j = response.json()
