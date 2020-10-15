import json
import re


open_list = ["[","{","(",] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Syntax invalid"
    if len(stack) == 0: 
        return "Valid Expression"
    else: 
        return "Syntax invalid"

def json_string(example):

    # Checking whether the string is valid or not
    string_checker = check(example)
    if string_checker == "Syntax invalid":
        print("Syntax invalid")
        return 0
    equal = []
    for i in example:
        if i == '=':
            equal.append(i)
    
    if len(equal)%2 != 0:
        print('Syntax invalid')
        return 0
    example_no_space=example.replace(" ","") # removing white spaces
    print(example_no_space)
    print(example_no_space.find("&"))

    # for main operator with manuplation
    center_operator=None
    if example_no_space[11]=="|":
        center_operator="or"
    elif example_no_space[11]=="&":
        center_operator="and"
    elif example_no_space[11]=="!":
        center_operator="not"
    else:
        pass
        

    #spliting two expression
    first_expresion=example_no_space[1:11]
    second_expression=example_no_space[13:-1]

    #converting the two expression to list
    list_of_expression=list()
    list_of_expression.append(first_expresion)
    list_of_expression.append(second_expression)

    result_list_json=list()
    for i in range(len(list_of_expression)):
        only_alpha=re.findall("[A-Z]",list_of_expression[i]) # taking only alaphas
        #print(only_alpha)

        only_numbers=re.findall("[0-9]",list_of_expression[i])# taking only numbers
        # if len(only_alpha) == 2:
        result_value=dict(zip(only_alpha,only_numbers)) # converting to dict
        only_operator=str(re.findall("[^A-Za-z0-9]",list_of_expression[i])) # finding all opeartors
        results=None
        if only_operator[12]=="&":
            results={"and":result_value}
            result_list_json.append(results)
        if only_operator[12]=="|":
            results={"or":result_value}
            result_list_json.append(results)


    final_result={"query":{center_operator:[result_list_json[0],result_list_json[1]]}}

    #json_object
    json_object=json.dumps(final_result,indent=4)
    print(json_object)

json_string('((A=5&&B=6)||(C=3&D=5))')

