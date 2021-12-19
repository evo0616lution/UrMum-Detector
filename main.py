import requests
from time import sleep
print("Welcome to UrMum Detector, coded by https://github.com/evo0616lution")
sleep(1)
url = input("Paste website URL: ")
try:
  r = requests.get(url)
except:
  print("Invalid URL")
if "your mama" or "ur mom" or "yo mama" or "ur mother" or "yo mother" in r.text:
  print("Uh oh! This website offenses your mother, keep distance!")
  sleep(2)
else:
  print("Hakuna Matata, this website is harmless.")
  sleep(2)
