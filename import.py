import lib.code_extract_specific_problem as code_extract
import sys
import getopt
#import lib.code 

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
	contest_id = argv[1]
	problem_char = argv[2]
	dir_path = argv[3]
	page_number = argv[4]
	print(page_number)
	for i in range(1,int(page_number)):
		submission_id = submission_id + code_extract.get_submission_id(contest_id,problem_char,page_number)


	for i in submission_id:
		source=code_extract.extract_source_code(contest_id,i)
		print(source)				
	#print(submission_id)	
