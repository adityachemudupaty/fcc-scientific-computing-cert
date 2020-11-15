def arithmetic_arranger(problems, solve = False):

    # problems is a list
    # if too many problems are passed, then return an error

    if len(problems) > 5:
        return("Error: Too many problems.")
    
    problems_dict = {}
    problem_num = range(len(problems))

    
    # create a dict to store the problems
    # separate each problem into its parts
    for i in problem_num:
        problems_dict['problem' + str(i)] = problems[i].split(' ', 1)
    
        






















    #return arranged_problems

arithmetic_arranger(['1 + 1'])
