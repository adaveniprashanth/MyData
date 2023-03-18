
#getting the html code from webpage
import urllib.request, urllib.error, urllib.parse
import requests
url = 'https://axeweb.intel.com/axe/tests/testlists/306/latestresults/combined/executions?executionStageId=3528,3529'
#
r = requests.get(url, allow_redirects=True)
open('testing1.txt', 'wb').write(r.content)

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('dummy.html', 'w')
f.write(webContent)
f.close
