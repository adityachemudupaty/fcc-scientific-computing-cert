def arithmetic_arranger(problems):
    



    #Check length of the problems list.
    #If len of problems list is greater than 5, then return 'Error: Too many problems.'
    if len(problems) > 5:
        return('Error: Too many problems.')

    #Change the strings received to sequence of ints and operand
    for i in range(len(problems)):
        problem_split = problems[i].split()
        
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
