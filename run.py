import requests
from requests.auth import HTTPBasicAuth

baseUrl = "https://familyzone.atlassian.net/rest/api/3/"
projectId = "10042"

def jiraRequest(url, method="GET"):
   auth = HTTPBasicAuth("dominik.jarco@familyzone.com", "a3juApmssokW1EJUhidy4596")
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


versionName = "schoolmanager-next"
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
