import requests #pip install requests
import sys

print("--- Command Line:", sys.argv)
#print(len(sys.argv))

if len(sys.argv) < 2:
    # expect 2 or 3 arguments, if not, we need to exit program now! 
    # command line format: cmd, (0) linkshortening.py, (1) url, (2) short
    print(f"Usage: {sys.argv[0]} full_long_url [short_name]")
    exit(1)

url = sys.argv[1]
#print(url)

#replace this api key variable with your own! find your api key in your profile in cuttly
api_key = "160d03c1a395a524f253d757a8dc84f33d3f5"

#construct our api url to call!
if len(sys.argv) >= 3:
    #user provided a preferred shortname!
    short_name = sys.argv[2]
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={short_name}"
else:
    # user didn't provide the short name
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

print("--- api_url:", api_url)

#make the request
response = requests.get(api_url)
print("--- response:", response)
print("--- response.json:", response.json())

data = response.json()["url"]
print("--- data:", data)

if data["status"] == 7:
    # url has been shortened successfully
    shortened_url = data["shortLink"]
    print("--- Shortened URL:", shortened_url)
else:
    print("[!!!!!] ERROR SHORTENING URL:", data)