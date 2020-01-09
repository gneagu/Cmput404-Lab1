import requests
print(requests.__version__)


google = requests.get("https://www.google.com")
print(google)


script = requests.get("https://raw.githubusercontent.com/gneagu/Cmput404-Lab1/m$
print(script.content)
