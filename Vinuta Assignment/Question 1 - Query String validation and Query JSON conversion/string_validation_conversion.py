import re
import json
s=input(str())
cnt1=0
cnt2=0
for i in s:
    if i=='(':
        cnt1+=1
    if i==')':
        cnt2+=1
#check balanced paranthesis
if cnt1==cnt2:
    ''' get logic operator between 2 conditions '''
    string1=s.split(')')

    for index, i in enumerate(string1[0]):
        #check '&' operator
        if i=='&':
        #if & operator exists, check whether next element contains & operator
            if string1[0][index+1] == '&':
                s1='and'

        #check '|' operator
        if i=='|':
        #if | operator exists, check whether next element contains | operator
            if string1[0][index+1] == '|':
                s1='or' 
    try:
        #check for && operator
        if string1[1].strip()[0] == '&' and string1[1].strip()[1] == '&':
            s2='and'

        #check for || operator
        if string1[1].strip()[0] == '|' and string1[1].strip()[1] == '|':
            s2='or'
        string2=string1[1][2:]
        ''' get logic operator inside each condition '''
        for i in string2:
            if i == '&':
                s3='and'
            if i == '|':
                s3='or'
        m=string1[0].split('=')
        a=m[0][-1]
        #search integers value
        b=int(re.search(r'\d+',m[1]).group(0))
        c=m[1][-1]
        
        #search integers value
        d=int(re.search(r'\d+',m[2]).group(0))
    
        string3=string1[1][2:]
        n=string3.split('=')
        
        #get alphabet which will be used as key in result
        e=n[0][-1]
        
        #search integers value
        f=int(re.search(r'\d+',n[1]).group(0))
        g=n[1][-1]
        
        #search integers value
        h=int(re.search(r'\d+',n[2]).group(0))
        
        #arrange the string in required pattern
        string={'query':{s2:[{s1:{a:b,c:d}},{s3:{e:f,g:h}}]}}
        
        #convert string to json and tab space
        json_object=json.dumps(string,indent=4)
        print(json_object)
    except Exception as e:
        print("Syntax invalid")
else:
    print("Syntax invalid")
    
