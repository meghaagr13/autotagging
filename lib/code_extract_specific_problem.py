import sys
sys.path.append('/home/dsinghvi/project/ml/codeforces_problem/lib')
from lxml import html
import urlgen
import httprequest
from exception import RequestFailureException
from bs4 import BeautifulSoup
import requests
import pandas as pd


def extract_source_code(contest_id,submission_id):
	"""Extracts source-code of submission at codeforces.com/contest/'contest_id'/submission/'submission_id'.
	
	Sends request to url mentioned above. Parses response text/html.
See lxml library documentation for more help regarding html parsing.
	:param contest_id: contest id where the problem appeared
	:param submission_id: submission id to be fetched
	"""
	
	#generates url for Codeforces submission page for submission#submissions_id
	submission_url = urlgen.generate_submission_url(contest_id, submission_id)

	print(submission_url)

	#makes a request to Codeforces API for users' submissions list
	try:
		response = httprequest.send_get_request(submission_url)
	except RequestFailureException as ex:
		print(ex.message)
	else:
		#parses html at codeforces.com/contest/contest_id/submission/submission_id to extract source_code
		tree2 = html.fromstring(response.text)
		code = tree2.xpath('//*[@id="pageContent]/div[3]/pre/text()"')

	try:
		if len(code) > 0:
			return fix_eol(code[0])
		else:
			#received empty content. unable to extract submissions using html parser
			raise ValueError('Empty Content')
	
	except ValueError as ex:
		print(ex.message)

def fix_eol(code):
	"""Fix end of line in source code and returns it"""
	code = code.replace('\\r\\n','\r\n')
	return code

def get_submission_id(contest_id,problem_char,page_number):
        url=urlgen.generate_problem_url(contest_id,problem_char,page_number)
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
        return status_id
