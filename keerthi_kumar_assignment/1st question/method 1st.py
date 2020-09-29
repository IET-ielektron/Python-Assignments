import re


def isValid(str):
  try:
    # initialize empty stack.
    stack = []
    # Iterating over the entire string
    for p in str:
      # If the input string contains an opening parenthesis(three tpe of open strings),
      # push to the stack.
      if p == '(' or p == '[' or p == '{':
        stack.append(p)
      else:
        # stack cannot be empty if a closing parenthis is occured
        if not stack:
          print(str, "contains invalid paren")
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
      print(str, "contains valid paren")
      # match the entered string with given regex
      data = re.compile(r'[A-Za-z0-9|]')
      # find the matching items and convert to them to list
      list = (re.findall(data, str))
      # print(list)
      # get the inted of the | operator
      list1 = list[0:list.index('|')]
      # print(list1)
      list2 = list[list.index('|') + 2:len(list)]
      # print(list2)
      d1 = {list1[i]: int(list1[i + 1]) for i in range(0, len(list1), 2)}
      # print(d1)
      d2 = {list2[i]: int(list2[i + 1]) for i in range(0, len(list2), 2)}
      # print(d2)
      output = {
        "query":
          {
            "or": [
              {
                "and":
                  {
                    "A": 2, "B": 3

                  }

              },
              {
                "and": {
                  "C": 4, "D": 5
                }
              }
            ]
          }
      }
      output['query']['or'][0]['and'] = d1
      output['query']['or'][1]['and'] = d2
      print(output)
    else:
      print(str, "contains invalid paren")
  except:
    print("please check the string entered")

str2 = "((A=2 && B=3) || (C=4 && D=5))"
isValid(str2)
str3 = " (A=2 && B=3"
isValid(str3)