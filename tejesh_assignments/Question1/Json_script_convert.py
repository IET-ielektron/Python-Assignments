import json
from urllib.parse import urlparse, parse_qs
import re

kk=None
kks=None

def check_valid_string(myStr): 
    """
    this will check string is valid
    """
    open_list = ["("] 
    close_list = [")"]
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
                return False
    if len(stack) == 0:         
        return True
    else: 
        return False
		

def get_json_output(nput_string,start,end):
	"""
	this will prepare json
	"""
	_parent = {}
	_child  = {}
	_parentKey = ""
	while start < end:
		if nput_string[start] == "=":
			_child.update({ nput_string[start-1] : nput_string[start+1] })
			if nput_string[start+2] == '&' and nput_string[start+3] == '&':
				_parentKey = "and"
			if nput_string[start+2] == '|' and nput_string[start+3] == '|':
				_parentKey = "or"
		start+=1
		
	if _parentKey == "":
		return "Syntax invalid"
		
	#check invalid params in values
	for i in _child.values():
		if i in [")", "(", "|", "&"]:
			return "Syntax invalid"
			
	_parent[_parentKey] = _child
	return _parent

def string_json_convertion(nput_string):
	'''A function which accepts valid Q string and convert to Q json'''
	terms_count = 0
	# Remove whitespaces in the string .
	new_string = nput_string.replace(" ", "") 
	nput_string = new_string 
	_parentkey = ""
	_parentList = []
	_resultDict = {}
	result = {}
	for i,char in enumerate(nput_string):
		# Get the term count by checking their ascii values.
		# Alphabets in the given expression must be uppercase.  
		if ord(char) >= 65 and ord(char) <= 90:
			terms_count+=1
			if terms_count == 1:
				start_point = i
		if char == ')' and terms_count == 2:         
			try:
				if nput_string[i+1] == '|' and nput_string[i+2] == '|':
					_parentkey = "or"
				if nput_string[i+1] == '&' and nput_string[i+2] == '&':
					_parentkey = "and"
			except Exception as e:
				return "Syntax invalid" 
			end_point   = i
			terms_count = 0
			term_output = get_json_output(nput_string, start_point,end_point)
			if term_output == "Syntax invalid":
				return "Syntax invalid"
			_parentList.append(term_output)
	# design a json
	_resultDict.update({_parentkey: _parentList})
	result["query"] = _resultDict
	
	if terms_count > 0 or _parentkey == "":
		return "Syntax invalid"
	json_object = json.dumps(result, indent = 4) 
	return json_object

	
def process_input_string(input):
	"""
	this will process provided input
	"""
	is_valid = check_valid_string(input)
	if is_valid:
		return string_json_convertion(input)
	else:
		return "Syntax invalid"

string = input ("Enter string :") 
#string = "(( A=5 || B=6) && (C=3 || D=5)"
print(process_input_string(string))
