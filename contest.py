import json
import urllib.request
from bs4 import BeautifulSoup
from pywinauto import Application
import os

app = Application(backend='uia')
app.connect(title_re=".*Chrome.*")
dlg = app.top_window()
url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()

url = "https://" + url
if( url.find('https://codeforces.com/contest') == -1):
	with open("solution.cpp__tests", "w") as outfile:
		outfile.write('Please open a contest page')
	exit()
else:
	page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, features = "html.parser")

data = []

table = soup.find('table', attrs={'class':'problems'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

problem_tags = []
for i in range(len(data)):
	if(len(data[i])>0):
		problem_tags.append(data[i][0])

print(problem_tags)

contest_id = url[-4] + url[-3] + url[-2] + url[-1]
path = contest_id
parent_dir = os.getcwd()

path = os.path.join(parent_dir,path)
if not os.path.exists(path):
	os.mkdir(path)

for problems in problem_tags:
	problem_path = os.path.join(path,problems)
	print(problem_path)
	with open("template.cpp") as main:
	    with open(problem_path+".cpp", "w") as sec:
	        for line in main:
	                sec.write(line)
	problem_url = " " + url + "/problem/" + problems + " \"";
	os.system('python automate.py' + problem_url + problem_path + "\"") 
