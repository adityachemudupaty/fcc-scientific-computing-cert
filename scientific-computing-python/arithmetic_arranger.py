def arithmetic_arranger(problems):
    



    #Check length of the problems list.
    #If len of problems list is greater than 5, then return 'Error: Too many problems.'
    if len(problems) > 5:
        return('Error: Too many problems.')
    
    #How many problems?
    problem_number = len(problems)

    #Change the strings received to sequence of ints and operand
    if problem_number == 1:
        problem_split1 = problems[0].split()
    elif problem_number == 2:
        problem_split1 = problems[0].split()
        problem_split2 = problems[1].split()
    elif problem_number == 3:
        problem_split1 = problems[0].split()
        problem_split2 = problems[1].split()
        problem_split3 = problems[2].split()
    elif problem_number == 4:
        problem_split1 = problems[0].split()
        problem_split2 = problems[1].split()
        problem_split3 = problems[2].split()
        problem_split4 = problems[3].split()
    elif problem_number == 5:
        problem_split1 = problems[0].split()   
        problem_split2 = problems[1].split()   
        problem_split3 = problems[2].split()   
        problem_split4 = problems[3].split()
        problem_split5 = problems[4].split() 

    #Operator should be '+' or '-' only
    if problem_split[1] != '+' or problem_split[1] != '-':
        return('Error: Operator must be "+" or "-" only.')
        
    #Operands should contain only digits
    try:
        operator1 = int(problem_split[0])
        operator2 = int(problem_split[2])
    except:
        return('Error: Numbers must contain only digits.')

    #Operands should not be longer than 4 digits
    if operator1 > 9999 or operator2 > 9999:
        return('Error: Numbers cannot be more than four digits.')
        

















    return arranged_problems
