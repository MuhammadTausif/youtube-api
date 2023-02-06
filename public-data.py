api_key = 'pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2'


from googleapiclient.discovery import build

service = build('drive', 'v3')
# ...
service.close()