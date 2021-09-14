import requests
payload = {'nojsoncallback': '1', 'format': 'json', 'method': 'flickr.photos.getPopular', 'user_id': '193897389@N05', 'api_key': "953d163a33e52481bd131c33664bb5ba"}

r = requests.get('https://www.flickr.com/services/rest', params=payload)

response = r.json()

if(response['stat']=='ok'):
	print('the request was successfull')
else:
	print('the request has failed with code:', response['code'], 'and message:', response['message'])
