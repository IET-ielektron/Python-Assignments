import json
#Json Format Data

#Expression check


def check_balance(expression):
    special_characters = "!@#$%^*{}[];:.,'"
    bit = ['(',')','|','&']
    open_list = ['(']
    close_list = [')']
    stack = []


    try:
        for i in range(len(expression)):
            if expression[i] in special_characters:
                return False
            if expression[i] == "=":
                if expression[i-1]  in bit or expression[i+1]  in bit:
                    return False
        if expression[-1] == "&" or expression[-1] =="|":
            return False
        if expression.isalpha() or "&" not in expression and "|" not in expression:
            return False


    except Exception as e:
        raise
    try:
        for i in range(len(expression)):
            if expression[i] == "&" :
                if expression[i+1] =="|":
                    return False
                if expression[i+1] =="&" or expression[i-1] =="&":
                    pass
                else:
                    return False

            if expression[i] == "|":
                if expression[i+1] =="&":
                    return False
                if expression[i+1] =="|" or expression[i-1] =="|":
                    pass
                else:
                    return False 

    except Exception as e:
        raise

    try:
        for c in expression:
            if c in open_list:
                stack.append(c)
            elif c in close_list:
                pos = close_list.index(c)
                if len(stack) > 0 and stack[-1] == open_list[pos]:
                    stack.pop()
                else:
                    return False
    except Exception as e:
        raise
    return True if not stack else False

#Logic Expression
def check_exp(data):
    d = {}
    d['query'] = {}
    setup = len(data) / 2
    exp = check_balance(data)
    try:
        if exp:
            for i in range(len(data)):
                    if i+1 < len(data):
                        try:
                            if data[i] == ")" and data[i+1] == "|" and data[i+2] == "|":
                                d['query']['or'] = []
                                for j in range(len(data)):
                                    if (data[j] == "&" and data[j+1] == '&') or (data[j] == "|" and data[j+1] == '|'):
                                        if (data[j-1] != ")" and data[j+2] != '('):
                                            if data[j] =="|":
                                                op = "or"
                                            else:
                                                op = "and"
                                            if data[j-2] =="=" and data[j+3] =="=":
                                                d['query']['or'].append({op:{str(data[j-3]):(data[j-1]), str(data[j+2]):(data[j+4])}})
                                            else:
                                                return "Invalid Format"
                                        if (data[j-5] == "(" and data[j+6] != ")" and data[j-4] != "(" ):
                                        
                                            if data[j] =="|":
                                                op = "or"           
                                            else:
                                                op = "and"      
                                            d['query']['or'].append({op:{str(data[j-4]):(data[j-2])}})
                                        if (j+6) < (len(data)):
                                            if (data[j-5] != "(" and data[j+6] == ")" and data[j+6] != ")"):
                                                if data[j] =="|":
                                                    op = "or"           
                                                else:
                                                    op = "and"      
                                                d['query']['or'].append({op:{str(data[j+3]):(data[j+5])}})  
                        except Exception as e:
                            raise


                        else:
                            try:
                                if setup == 5:
                                    for j in range(len(data)):
                                        if (data[j] == "|" and data[j+1] == '|') or (data[j] == "&" and data[j+1] == '&'):
                                            if data[j] =="|":
                                                op = "or"
                                            else:
                                                op = "and"
                                            d['query'][op] = []
                                            d['query'][op].append({str(data[j-3]):(data[j-1]), str(data[j+2]):(data[j+4])}) 
                            except Exception as e:
                                raise

                        try:
                            if data[i] == ")" and data[i+1] == "&" and data[i+2] == "&":
                                d['query']['and'] = []
                                for j in range(len(data)):
                                    if (data[j] == "|" and data[j+1] == '|') or (data[j] == "&" and data[j+1] == '&'):
                                        if (data[j-1] != ")" and data[j+2] != '('):
                                    
                                            if data[j] =="|":
                                                op = "or"
                                            else:
                                                op = "and"
                                            if data[j-2] =="=" and data[j+3] =="=":
                                                d['query']['and'].append({op:{str(data[j-3]):(data[j-1]), str(data[j+2]):(data[j+4])}})
                                            else:
                                                return "Invalid Format"

                                        if (data[j-5] == "(" and data[j+6] == ")"):
                                            if data[j] =="|":
                                                op = "or"
                                            else:
                                                op = "and"      
                                            d['query']['and'].append({op:{str(data[j-4]):(data[j-2]), str(data[j+3]):(data[j+5])}})
                                        if (data[j-5] == "(" and data[j+6] != ")" and data[j-4] != "(" ):
                                            print(data[j-4])
                                            if data[j] =="|":
                                                op = "or"           
                                            else:
                                                op = "and"      
                                            d['query']['and'].append({op:{str(data[j-4]):(data[j-2])}})


                                        if (j+6) < (len(data)):
                                        
                                            if (data[j-5] != "(" and data[j+6] == ")" and data[j+6] != ")"):
                                                if data[j] =="|":
                                                    op = "or"           
                                                else:
                                                    op = "and"      
                                                d['query']['and'].append({op:{str(data[j+3]):(data[j+5])}})                                                  
                        except Exception as e:
                            raise

                        else:
                            try:
                                if setup == 5:
                                    for j in range(len(data)):
                                        if (data[j] == "|" and data[j+1] == '|') or (data[j] == "&" and data[j+1] == '&'):
                                            if data[j] =="|":
                                                op = "or"
                                            else:
                                                op = "and"
                                            d['query'][op] = []
                                            d['query'][op].append({str(data[j-3]):(data[j-1]), str(data[j+2]):(data[j+4])})
                            except Exception as e:
                                raise

            json_object = json.dumps(d, indent = 4)    
            return json_object
        else:
            return "Invalid Format"

    except Exception as e:
        raise


#get the expression from user((A=2 && B=3) || (C=4 && D=5))

user = input("Enter the Expression\n")                          #(A=2 && B=3) || (C=4 && D=5)   
data = user.replace(" ","")
try:
    if (len(data) != 0):
        print(check_exp(data))
    else:
        print("Empty Format")

except Exception as e:
    raise
