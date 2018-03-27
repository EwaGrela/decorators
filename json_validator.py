import json 

#decorator
def validate_json(*args):
	def validator(func):
		def inner(data):
			res = func(data)
			keys = sorted(list(json.loads(data).keys()))
			if keys == sorted(list(args)):
				return res
			else:
				raise ValueError			
		return inner
	return validator

#functions
@validate_json("last_name", "first_name")
def process_json(json_data):
    return len(json_data)

@validate_json("name", "surname")
def check_json(data):
    return json.dumps(data)
    
