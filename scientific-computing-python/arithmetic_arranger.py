def arithmetic_arranger(problems, solve=False):
	# problems is a list
	# if too many problems are passed, then return an error
	
	if len(problems) > 5:
		return "Error: Too many problems."
	
	problems_dict = {}
	problem_num = range(len(problems))
	
	# check that operators are only + or -
	
	for problem in problems:
		ex = problem.split()
		if ex[1] != '+' or ex[1] != '-':
			return "Error: Operator must be '+' or '-'."
		# check that operands are actually numbers
		try:
			int(problem.split[0])
			int(problem.split[2])
		except:
			return "Error: Numbers must contain only digits."
		# check that operands are 4 characters max
		if (len(problem.split[0]) >= 5) and (len(problem.split[2]) >= 5):
			return "Error: Numbers cannot be more than four digits."
	
	    print(ex)
	
	# store the problems in a dictionary after separating the problem into two parts
	
	for i in problem_num:
		problems_dict['problem' + str(i)] = problems[i].split(' ', 1)
	
	# create dummy problems until problem 5
	num_problems = len(problems)
	while num_problems < 5:
		problems_dict['problem' + str(num_problems)] = ['', '']
		num_problems += 1
		print(problems_dict)
	
	# arrange the first line
	space = '    '
	
	line1 = problems_dict['problem1'][0] + space + problems_dict['problem2'][0] \
	        + space + problems_dict['problem3'][0] \
	        + space + problems_dict['problem4'][0] \
	        + space + problems_dict['problem5'][0]
	
	line2 = problems_dict['problem1'][1] + space + problems_dict['problem2'][1] \
	        + space + problems_dict['problem3'][1] \
	        + space + problems_dict['problem4'][1] \
	        + space + problems_dict['problem5'][1]
	
	line3 = '_____    _____    _____    _____    _____'
	print(line1)
	arranged_problems = line1 + '\n' + line2 + '\n' + line3
	
	print(arranged_problems)
	return arranged_problems


arithmetic_arranger(['1 + 1'])
