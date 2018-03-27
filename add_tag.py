#decorator:
def add_tag(tag):
	def adder(func):
		def inner_func(*args, **kwargs):
			res = func(*args, **kwargs)
			return f"<{tag}>{res}<{tag}/>"
		return inner_func
	return adder

#functions returning strings:
@add_tag("h1")
def write_something(sth):
	return sth


@add_tag("p")
def say_hello():
	return "hello"


#testing functions:
print(write_something("napisz cokolwiek"))
print(say_hello())
