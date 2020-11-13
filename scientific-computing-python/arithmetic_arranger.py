def arithmetic_arranger(problems):
    



    #Check length of the problems list.
    #If len of problems list is greater than 5, then return 'Error: Too many problems.'
    if len(problems) > 5:
        return('Error: Too many problems.')

    #Change the strings received to sequence of ints and operand
    for i in range(len(problems)):
        problem_split = problems[i].split()
        
        #Operand should be '+' or '-' only
        if problem_split[1] != '+' or problem_split[1] != '-':
            return('Error: Operand must be "+" or "-" only.')


    return arranged_problems
