#!/usr/bin/env python3

import sys
from color import get as col

def decorate(self, name, decs, globe):
	attrs = [getattr(self, func) for func in __getmethods__(self)]
	[[decor(attr.__name__, globe, (dec, str(cond)), name) for dec, cond in decs.items()] for attr in attrs]

def __getmethods__(self):
	state, res = False, []
	for func in self.__dir__():
		if func[-2:] == "__": state = True
		if state and func[-2:] != "__": res.append(func)
	return res

decor = lambda x, y, z, w: exec(w + "." + x + " = Decor_lib(" + z[1] + ", '" + z[0] + "')(" + w + "." + x + ")", y)

### Decorator Library ###
class Decor_lib(object):
	def __init__(self, cond, name):
		self.cond = cond
		self.name = name

	def __call__(self, f):
		self.f = f
		def inner(*args, **kwargs):
			return eval("self." + self.name + "(*args, **kwargs)", {'self': self, 'self.f': self.f, 'args': args, 'kwargs': kwargs, "eval('self.name'}": self.name})

		inner.__name__ = self.f.__name__
		inner.__self__ = self.f.__self__
		return inner

	def add_decor(self, func, func_name):
		exec("self." + func_name + " = " + func_name)
		# pass

	def debug(self, *args, **kwargs):
		if self.cond: print(col("green", "\nEnter: ") + str(self.f.__name__))
		res = self.f(*args, **kwargs)
		if self.cond: print(col("red", "Exit: ") + str(self.f.__name__))
		return res

	def pretty(self, *args, **kwargs):
		if self.cond: print(col("green", "\nPretty enter: ") + str(self.f.__name__))
		res = self.f(*args, **kwargs)
		if self.cond: print(col("red", "Pretty exit: ") + str(self.f.__name__))
		return res

	def test(self, *args, **kwargs):
		if self.cond: print(col("green", "\ntest enter: ") + str(self.f.__name__))
		res = self.f(*args, **kwargs)
		if self.cond: print(col("red", "test exit: ") + str(self.f.__name__))
		return res

def dog(self, *args, **kwargs):
	if self.cond: print(col("green", "\nadd_func enter: ") + str(self.f.__name__))
	res = self.f(*args, **kwargs)
	if self.cond: print(col("red", "add_func exit: ") + str(self.f.__name__))
	return res

def add_func():
	dec = Decor_lib(True, "add_decor")
	dec.add_decor(dog, 'dog')
	pass	

### Start of prgram ###
class This():	
	def __init__(self, args):
		self.c = 8
		for key, val in args.items(): exec("self." + key + " = " + str(val))

	def fueoahteoahe(self):
		self.rcr = 9

class Cfunc3(This):
	def __init__(self, args):
		super().__init__(args)
		self.x = 2

	def func3(self, d3):
		print("In func3: " + str(d3))
		self.y = 3

	def func4(self):
		self.f = 9
		print("In func4")


if __name__ == "__main__":
	d = bool(int(sys.argv[1]))
	decs = {"debug": d, "pretty": d, "test": not d}
	t = Cfunc3(args = decs)
	
	decorate(t, 't', decs, globals())
	t.func3(d)
	t.func4()

	print("\n\n=== Testing range ===\n")
	add_func()
