from TwitterAPI import TwitterAPI

search_term = 'bitcoin'
consumer_key = 'r77hwOwZ29Vsquiy2Yzch2nlC'
consumer_secret = '8b5CksWSTrewx0TMoKWc9OMr7QSAPLw18MDInAsp2Fy1zEIIY3'

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 auth_type='oAuth2')

r = api.request('search/tweets', {'q': search_term})

for item in r:
    print(item['text'] if 'text' in item else item)

print('\nQUOTA: %s' % r.get_rest_quota())
