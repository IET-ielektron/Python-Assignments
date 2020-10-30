import json
import re

q = str(input('please enter the string: '))
try:
    if q.endswith('))') != True and q.startswith('((') != True:
        s = list(q)
        if s[int(len(q) / 2)] == '&':
            q1 = q.index('&&', (int((len(q) / 2) - 2)), (int((len(q) / 2) + 2)))
            z1 = q[:q1]
            z2 = q[q1 + 2:]
            z = [z1, z2]
            output = {}
            output["query"] = {}
            data = []
            for i in z:
                i = i.strip()
                if i.endswith(')') == True and i.startswith('(') == True:
                    i = i[1:-1]
                    try:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('||')))
                        d = {}
                        d["or"] = Dict
                        data.append(d)

                    except Exception:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('&&')))
                        d = {}
                        d["and"] = Dict
                        data.append(d)
                    output["query"]["and"] = data
                else:
                    output["query"] = "Please check your Input"
                    breakpoint
        else:
            q1 = q.index('||', (int((len(q) / 2) - 2)), (int((len(q) / 2) + 2)))
            z1 = q[:q1]
            z2 = q[q1 + 2:]
            z = [z1, z2]
            output = {}
            output["query"] = {}
            data = []
            for i in z:
                i = i.strip()
                if i.endswith(')') == True and i.startswith('(') == True:
                    i = i[1:-1]
                    try:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('||')))
                        d = {}
                        d["or"] = Dict
                        data.append(d)
                    except Exception:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('&&')))
                        d = {}
                        d["and"] = Dict
                        data.append(d)
                    output["query"]["or"] = data
                else:
                    output["query"] = "Please check your Input"
                    break
    else:
        q = q[1:-1]
        s = list(q)
        if s[int(len(q) / 2)] == '&':
            q1 = q.index('&&', (int((len(q) / 2) - 2)), (int((len(q) / 2) + 2)))
            z1 = q[:q1]
            z2 = q[q1 + 2:]
            z = [z1, z2]
            output = {}
            output["query"] = {}
            data = []
            for i in z:
                i = i.strip()
                if i.endswith(')') == True and i.startswith('(') == True:
                    i = i[1:-1]
                    try:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('||')))
                        d = {}
                        d["or"] = Dict
                        data.append(d)
                    except Exception:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('&&')))
                        d = {}
                        d["and"] = Dict
                        data.append(d)
                    output["query"]["and"] = data
                else:
                    output["query"] = "Please check your Input"
                    breakpoint
        else:
            q1 = q.index('||', (int((len(q) / 2) - 2)), (int((len(q) / 2) + 2)))
            z1 = q[:q1]
            z2 = q[q1 + 2:]
            z = [z1, z2]
            output = {}
            output["query"] = {}
            data = []
            for i in z:
                i = i.strip()
                if i.endswith(')') == True and i.startswith('(') == True:
                    i = i[1:-1]
                    try:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('||')))
                        d = {}
                        d["or"] = Dict
                        data.append(d)
                    except Exception:
                        Dict = dict((x.strip(), int(y.strip()))
                                    for x, y in (element.split('=')
                                                 for element in i.split('&&')))
                        d = {}
                        d["and"] = Dict
                        data.append(d)
                    output["query"]["or"] = data
                else:
                    output["query"] = "Please check your Input"
                    break
    # the output in json format
    print(json.dumps(output))
except Exception:
    print('Please check your Input')
# { "query": { "or": [ { "and": { "A": 2, "B": 3 } }, { "and": { "C": 4, "D": 5 } } ] } }
