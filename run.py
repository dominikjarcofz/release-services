import requests
from requests.auth import HTTPBasicAuth
import json

configFile = "1.cfg"
f = open(configFile)
config = json.load(f)

baseUrl = config["baseUrl"]
projectId = config["projectId"]
email = config["email"]
apiToken = config["apiToken"]
versionName = config["versionName"]


def jiraRequest(url, method="GET"):
   auth = HTTPBasicAuth(email, apiToken)
   headers = { "Accept": "application/json" }
   return requests.request(
      method,
      url,
      headers=headers,
      auth=auth
   )

def getTicketsInVersion(versionId):
   url = "{0}search?jql=project={1} AND fixVersion={2}".format(baseUrl, projectId, versionId)
   return jiraRequest(url)

def getVersionId(versionName):
   url = "{0}project/{1}/version?query={2}".format(baseUrl, projectId, versionName)
   return jiraRequest(url).json()["values"][0]["id"]


print("Getting version id for {0}...".format(versionName))
versionId = getVersionId(versionName)
print("{0} has version id {1}".format(versionName, versionId))
print("Getting ticket list...")
response = getTicketsInVersion(versionId)
tickets = response.json()["issues"]

ids = []
keys = []
for ticket in tickets:
   ids.append(ticket["id"])
   keys.append(ticket["key"])

print(keys)
