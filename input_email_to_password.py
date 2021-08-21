import http.client
import re

conn = http.client.HTTPSConnection("breachdirectory.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ff6504a139msh232744d71fffc57p1a5893jsn7e32f6e84072",
    'x-rapidapi-host': "breachdirectory.p.rapidapi.com"
    }



email = input("Enter email : ")
pattern = re.compile(r'([a-zA-Z0-9]+)*@([a-zA-Z0-9]+.[a-zA-Z0-9]+)')
matches = pattern.finditer(email)


for match in matches:
	final_request="/?func=auto&term="+match.group(1)+"%40"+match.group(2)


conn.request("GET", final_request, headers=headers)

res = conn.getresponse()
data = res.read()

raw_data = data.decode("utf-8")

pattern = re.compile(r'(password*"*:\s*")([\S]+)')
matches = pattern.finditer(raw_data)


print("all passwords found :")

for match in matches:
	print(match.group(2)[:-2])
