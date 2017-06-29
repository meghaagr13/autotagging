from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_submission_id(contest_id,problem_char,page_number):
	url="http://codeforces.com/problemset/status/816/problem/B"
	r=requests.get(url)
	data=r.text
	soup=BeautifulSoup(data)
	table=soup.find(lambda tag: tag.name=='table',attrs={"class":"status-frame-datatable"})
	row = table.findAll('tr')
	status_id=[]
	for i in range(1,len(row)):
		first=row[i].findAll('td')[0]
		status_id.append(str(first.text))
	#print status_id

