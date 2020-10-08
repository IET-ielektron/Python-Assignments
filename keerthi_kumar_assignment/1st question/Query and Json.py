

class Validation:
    #global variable
    entered_str = None

    def __init__(self,entered_str):
        self.entered_str = entered_str
        self.result = {}
        
    def start_program(self):
        status = self.is_valid()
        if status is True:
            return self.convert_to()
        else:
            return "Syntax invalid"  
        
    def is_valid(self):
        # initialize stack
        stack = []
        # Iterating over the entire string
        for p in self.entered_str:
          # If the input string contains an opening parenthesis(three tpe of open strings),
          # push to the stack.
          if p == '(' or p == '[' or p == '{':
              stack.append(p)
          else:
            # stack cannot be empty if a closing parenthis is occured
            if not stack:
              print(self.entered_str, "contains invalid paren")
              return
            else:
              # If the input string contains a closing bracket,
              # then pop the corresponding opening parenthesis if
              # present.
              top = stack[-1]
              if p == ')' and top == '(' or p == ']' and top == '[' or p == '}' and top == '{':
                stack.pop()
        # Checking the status of the stack to determine the validity of the string.
        if not stack:
            return True
        else:
            return False

    #convert query string to json
    def convert_to(self):
        count = 0
        # replce white space
        _str = self.entered_str.replace(" ", "")
        self.entered_str = _str
        _key = ""
        _list = []
        _res_dict = {}
        for i,char in enumerate(self.entered_str):
            #check for alphabets with upper case
            if ord(char) >= 65 and ord(char) <= 90:
                count +=1
                if count == 1:
                    first = i
            if char == ')' and count == 2:
                try:
                    if self.entered_str[i+1] == '|' and self.entered_str[i+2] == '|':
                        _key = "or"
                    if self.entered_str[i+1] == '&' and self.entered_str[i+2] == '&':
                        _key = "and"
                except:
                    return "Syntax invalid"
                last = i
                count = 0
                output = self.json(first,last)
                if output == "Syntax invalid":
                    return "Syntax invalid"
                _list.append(output)
        # json body
        _res_dict.update({_key: _list})
        self.result["query"] = _res_dict
        if count > 0 or _key == "":
            return "Syntax invalid"
        return self.result

    def json(self,first,last):
        _p = {}
        _c  = {}
        _Key = ""
        equals = 0
        
        fir = first
        while fir < last:
            if self.entered_str[fir] == "=":
                equals += 1;
                # print(self.entered_str[fir]);
            fir+=1
                
        if(equals == 2):
            while first < last:
                if self.entered_str[first] == "=":
                    #print(self.entered_str[first]);
                    _c.update({ self.entered_str[first-1] : self.entered_str[first+1] })
                    if self.entered_str[first+2] == '&' and self.entered_str[first+3] == '&':
                        _Key = "and"
                    if self.entered_str[first+2] == '|' and self.entered_str[first+3] == '|':
                        _Key = "or"
                first+=1
            if _Key == "":
                return "Syntax invalid"
            _p[_Key] = _c
        else:
            return "Syntax invalid"
        
        return _p

#valid cases
print("case 1 valid cases")
String = "((A=2 || G=3) && (C=4 || D=9))"
# String = "((A=2 && G=3) || (C=4 && D=9))"
# String = "((L=8 || X=3) && (C=4 && N=9))"


# invalid cases
# print("case 2 invalid cases")
# String = "((A= || G=3) && (B=2 && D=9))"
# String = "((A=2 || G=) && (C 4 && D=9))"
# String = "((A || G=3) && (C=4 || D=9))"
# String = "((A || G=3) &| (C=4 || D)"
# String = "((A=9 || G=3) && C=4 || D=9))"
# String = "((A=9 || G=3 && (C=4 || D=9))"
# String = "(A=9 || G=3) && (C=4 || D=9)"
v1 = Validation(String)
output = v1.start_program()
print("input string : ", String)
print("output  : ", output)
