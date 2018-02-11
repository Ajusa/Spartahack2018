import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
import json
import threading


CLIENT_ID = '2282GZ'
CLIENT_SECRET = '28cb113a9fa6677cb63b9b798a604fca'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
today = str(datetime.datetime.now().strftime("%Y%m%d"))
def printit():
  fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date="today", detail_level='1sec')
  import json
  with open('result.json', 'w') as fp:
    json.dump(fit_statsHR["activities-heart-intraday"]["dataset"], fp)
printit()