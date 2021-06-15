import json
import urllib.request
from bs4 import BeautifulSoup
from pywinauto import Application
import os
import sys 

if(len(sys.argv)==1):
	app = Application(backend='uia')
	app.connect(title_re=".*Chrome.*")
	dlg = app.top_window()
	url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
	url = "https://" + url
	filename = "solution.cpp__tests"
elif(len(sys.argv)==2):
	app = Application(backend='uia')
	app.connect(title_re=".*Chrome.*")
	dlg = app.top_window()
	url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
	url = "https://" + url
	filename = sys.argv[1] + "__tests"
else:
	url = sys.argv[1]
	filename = sys.argv[2] + ".cpp__tests"

if( url.find('https://codeforces.com/') == -1):
	with open("solution.cpp__tests", "w") as outfile:
		outfile.write('Please open a problem page')
	exit()
else:
	try:
		page = urllib.request.urlopen(url)
	except:
		print(url)
		exit()
soup = BeautifulSoup(page, features = "html.parser")

x = soup.body.find_all('div', attrs={'class' : 'input'})
y = soup.body.find_all('div', attrs={'class' : 'output'})

res = ""
out = ""

for elements in x:
	for br in elements.find_all("br"):
		br.replace_with("\n")
	res += elements.text
for elements in y:
	out += elements.text

if 'Input\n' in res:
	res = res.split('Input\n')
else:
	res = res.split('Input')

if 'Output\n' in out:
	out = out.split('Output\n')
else:
	out = out.split('Output')

res.remove("")
out.remove("")

#res = [elements.strip() for elements in res]
out = [elements.strip() for elements in out]

correct = []
for elements in  out:
	correct.append([elements])

final = []
sz = len(res)

for i in range(sz):
	dic = {
		"correct_answers" : correct[i],
		"test" : res[i]
	}
	final.append(dic) 


with open(filename, "w") as outfile: 
    outfile.write(json.dumps(final)) 
