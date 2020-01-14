from googleapiclient.discovery import build

api_key = "AIzaSyB0IQLZSWV7iBYUc7tnrG2Nu6R7iNforMQ"
cse_key = "001218037654599568255:526j1dfzayy"

# Authorizing requests
resource = build("customsearch", 'v1', developerKey=api_key).cse()
result = resource.list(q='กินดี', cx=cse_key).execute()

time = 'after:2017-12-31 before:2019-1-1'