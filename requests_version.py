#This code was copied from the TA teaching the Wednesday Lab on Jan 8. (I didn't get his name)

import requests
print(requests.__version__)


google = requests.get("https://www.google.com")
print(google)


script = requests.get("https://raw.githubusercontent.com/gneagu/Cmput404-Lab1/master/requests_version.py")
print(script.content)

