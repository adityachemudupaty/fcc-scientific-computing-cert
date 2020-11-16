import copy


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
		# print(ex)
		if ex[1] != '+' and ex[1] != '-':
			return "Error: Operator must be '+' or '-'."
			# print("Error: Operator must be + or -.")
		# check that operands are actually numbers
		try:
			int(ex[0])
			int(ex[2])
		except:
			return "Error: Numbers must only contain digits."
		# check that operands are 4 characters max
		if (len(ex[0]) >= 5) or (len(ex[2]) >= 5):
			return "Error: Numbers cannot be more than four digits."
	
	# store the problems in a dictionary after separating the problem into three parts
	
	for i in problem_num:
		problems_dict['problem' + str(i)] = problems[i].split()
	
	num_problems = len(problems_dict)
	
	problem_list = [item.split() for item in problems]
	first_op = [item.split()[0] for item in problems]
	operators = [item.split()[1] for item in problems]
	second_op = [item.split()[2] for item in problems]
	
	max_len_list = []
	space = '    '
	for i in range(len(problems)):
		max_len_list.append(([len(first_op[i]), len(second_op[i])]))
	paddings = []
	
	for operand_len in max_len_list:
		paddings.append(max(operand_len))
	
	
	# Generate the lines
	
	# Generate the first line
	fi_line = ''
	fi_line_list = copy.deepcopy(first_op)
	fi_line_i = 0
	while fi_line_i < (len(problems)):
		fi_line = fi_line + ' ' + fi_line_list[fi_line_i].rjust(paddings[fi_line_i]+1, ' ') + space
		fi_line_i += 1
	# print(fi_line)
	
	
	# Generate the second line
	s_line = ''
	s_line_list = copy.deepcopy(second_op)
	s_line_i = 0
	while s_line_i < (len(problems)):
		s_line = s_line + operators[s_line_i] + ' ' + s_line_list[s_line_i].rjust(paddings[s_line_i], ' ') + space
		s_line_i += 1
	# print(s_line)
	
	# Generate the third line
	t_line_unit = '-'
	t_line_list = []
	# Padding tells us what the length of the longer operand
	# We add one to it in order to account for the operator
	for padding in paddings:
		t_line_list.append(t_line_unit * (int(padding) + 2))
	t_line = ''
	
	for item in t_line_list:
		t_line = t_line + item + space
	# print(t_line)
	
	# Generate the fourth line
	soln = 0
	fo_line = ''
	fo_line_i = 0
	for problem in problem_list:
		if problem[1] == '+':
			soln = int(problem[0]) + int(problem[2])
		elif problem[1] == '-':
			soln = int(problem[0]) - int(problem[2])
		fo_line = fo_line + ' ' + str(soln).rjust(paddings[fo_line_i]+1, ' ') + space
		fo_line_i += 1
	# print(fo_line)
	
	if solve == True:
		arranged_problems = fi_line.rstrip() + '\n' + s_line.rstrip() + '\n' + t_line.rstrip() + '\n' + fo_line.rstrip()
	else:
		arranged_problems = fi_line.rstrip() + '\n' + s_line.rstrip() + '\n' + t_line.rstrip()
	
	# print(arranged_problems)
	return arranged_problems


print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"], False))