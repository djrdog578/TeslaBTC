import tweepy
import secrets
import cryptocompare


auth = tweepy.OAuthHandler(secrets.API_Key, secrets.API_Secret_Key)
auth.set_access_token(secrets.Access_Token, secrets.Token_Secret)
api = tweepy.API(auth)

price = cryptocompare.get_price('BTC', 'USD').get('BTC').get('USD')
costAvg = (43000 * 35000)
current = (43000 * price)

if current - costAvg > 0:
    api.update_status('Tesla has currently made ' + '${:,.2f}'.format(current - costAvg) + ' holding Bitcoin. #TeslaBTC')
elif current - costAvg < 0:
    api.update_status('Tesla has currently lost ' + '${:,.2f}'.format(current - costAvg) + ' holding Bitcoin. #TeslaBTC')
else:
    pass



