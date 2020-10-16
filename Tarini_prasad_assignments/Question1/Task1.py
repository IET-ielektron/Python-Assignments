import json
import re
class ValidationAndQuery:
    def __init__(self, userInputStr):
        self.userInputStr = userInputStr
        self.output = {}
        self.opening_tag_lst = ['[','{','(']
        self.closing_tag_lst = [']','}',')']

    def check_string(self):
        self.numcount = sum(j.isdigit() for j in self.userInputStr)
        self.digitcount = sum(s.isalpha() for s in self.userInputStr)
        lst = []
        for i in self.userInputStr:
            if i in self.opening_tag_lst:
                lst.append(i)
            elif i in self.closing_tag_lst:
                position = self.closing_tag_lst.index(i)
                if ((len(lst) > 0) and
                        (self.opening_tag_lst[position] == lst[len(lst) - 1])):
                    lst.pop()
                else:
                    return False
        if len(lst) == 0 and self.numcount==self.digitcount:
            return True
        else:
            return False

    def str_to_query(self):
        count = 0
        new_string = re.sub(" ","",self.userInputStr)
        self.userInputStr = new_string
        superoperator = ""
        List = []
        outputdict = {}

        for i in range(len(self.userInputStr)):
            if ord(self.userInputStr[i])>=65 and ord(self.userInputStr[i])<=90:
                count +=1
                if count==1:
                    start_index = i
            if self.userInputStr[i] == ')' and count == 2:
                if self.userInputStr[i + 1] == '|' and self.userInputStr[i + 2] == '|':
                    superoperator = "or"
                if self.userInputStr[i + 1] == '&' and self.userInputStr[i + 2] == '&':
                    superoperator = "and"
                end_index = i
                count = 0
                term_output = self.desired_format(start_index, end_index)
                if term_output == "Syntax invalid":
                    return "Syntax invalid"
                List.append(term_output)
        outputdict.update({superoperator: List})
        self.output["query"] = outputdict
        if count > 0 or superoperator == "":
            return "Syntax invalid"
        return json.dumps(self.output,indent=2)


    def desired_format(self, start, end):
        superoperaror = {} ; childoperator = {}; parentKey = ""
        while start < end:
            if self.userInputStr[start] == "=":
                childoperator.update({self.userInputStr[start - 1]: self.userInputStr[start + 1]})
                if self.userInputStr[start + 2] == '&' and self.userInputStr[start + 3] == '&':
                    parentKey = "and"
                if self.userInputStr[start + 2] == '|' and self.userInputStr[start + 3] == '|':
                    parentKey = "or"
            start += 1
        superoperaror[parentKey] = childoperator
        return superoperaror

    def finalResult(self):
        return "Syntax invalid" if self.check_string() is not True else  self.str_to_query()


input_str = "((A=2||B=3)||(C=4&&D=5))"


object = ValidationAndQuery(input_str)
output = object.finalResult()
print("Output :", output)
