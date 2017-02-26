import tweepy
from tweepy import OAuthHandler
consumer_key = 'vF0iA1HVBdUdYV7f4dIfMFt79'
consumer_secret = '56HehB5q9R9vB6nO6y63WAyrHGPwBRjMCgv4taHSl88ieC7N8H'
access_token = '3094801379-gNlBk39K3eSOEjpiZb9G0LcrytboTz38v38Nix3'
access_secret = 'Jj24grCai0YDBeEUr3GNUKttKIMYYT5Rw7snmNuaEQxUD'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
x=raw_input("Welcome to my application!If you want to continue press 1:")
if x=="1":	
	k=raw_input("Pease insert the name of the first user: ")
	user = api.get_user(k)
	k1=raw_input("Pease insert the name of the second user: ")
	user1 = api.get_user(k1)
	print user.screen_name, "has", user.followers_count,"followers"
	print user1.screen_name, "has", user1.followers_count,"followers"
	t=0
	print "Please wait to see if", k ," and " ,k1, "has common followers..."
	for followers in user.followers():
		for followers1 in user1.followers():
			if followers.screen_name==followers1.screen_name:
				print followers1.screen_name
				t+=1
	if t==0:
		print "Both users have no common followers!!"
	else:
		print "Finally they have ",t," common followers"
else:
	print "Thank you!!"