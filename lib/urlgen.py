from config import Codeforces

def generate_submission_url(contest_id,submission_id):
	"""Generates url for user submissions eg 'codeforces.com/contest/715/submissions/271829' and returns it"""
	
	url = Codeforces.BASE_URL + "/contest/" + str(contest_id) + "/submission/" + str(submission_id);
	return url

def generate_problem_url(contest_id,problem_char,page_number):
	"""Generates url for problem submissions of a particular problem """
	url = Codeforces.BASE_URL + "/problemset/status/" + str(contest_id) + "/problem/" + problem_char + "/page/" + page_number;
	return url 
