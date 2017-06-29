import lib.code_extract_specific_problem as code_extract
import sys
import getopt
from bs4 import BeautifulSoup 
argc = len(sys.argv)
argv = sys.argv

contest_id = None
dir_path = None
problem_char = None
submission_id = []
page_number = None

if argc < 4:
	print ("Usage: python import.py {contest_id} {problem_char} {directory_path} {page_number}")
	sys.exit(1);
else:
	page_number = argv[4]
	print(page_number)
	for i in range(1,int(page_number)):
		submission_id = submission_id + code_extract.get_submission_id(contest_id,problem_char,page_number)
	submission_id=[el.replace('\n', '') for el in submission_id]
#	submission_id=filter(lambda x: x!='\n', submission_id)
	print(submission_id)	
