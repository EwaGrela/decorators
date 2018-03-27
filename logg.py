import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

#decorator:
def log_this(logger, **kwargs):
	def inner(func):
		def functor(*args, **kwargs2):
			all_arg = tuple([str(x) for x in args] + [str(x)+"="+str(y) for (x,y) in kwargs2.items()])
			res = func(*args, **kwargs2)
			logger.log(kwargs["level"], kwargs["format"], func.__name__, all_arg, res)
			return res
		return functor
	return inner

#functions:
@log_this(logger, level=logging.INFO, format='%s: %s -> %s')
def my_func(a, b, c=None, d=False):
    return 'Wow!'


@log_this(logger, level=logging.DEBUG, format='%s: %s = %s')
def new_func(a, b=None, c=True):
	return a**3

#calling functions to test them and see results:
print(my_func(1, 2, c=False,d=True))
print(new_func(5, c=False))