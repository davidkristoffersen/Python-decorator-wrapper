#!/usr/bin/env python3

import sys
from color import get as col

class Test_dec(object):
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

	def debug_decor(self, *args, **kwargs):
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
		if self.cond: print(col("green", "\nTest_dec enter: ") + str(self.f.__name__))
		res = self.f(*args, **kwargs)
		if self.cond: print(col("red", "Test_dec exit: ") + str(self.f.__name__))
		return res


class This():	
	def __init__(self, args):
		self.c = 8
		for key, val in args.items(): exec("self." + key + " = " + str(val))
		# print(self.debug_decor, self.pretty)

	def fueoahteoahe(self):
		self.rcr = 9

# @dec2_cond(False)
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

def decor2(x, y):
	# print(dir(x.__self__))
	# print(x.__name__)
	# print(globals())
	# a1 = ''.join([str(key) for key, val in globals().items() if val == x.__self__])"
	# a2 = x.__name__
	# print(a1, a2)
	# exec(a1 + "." + a2 + " =  dec2_cond(" + a1 + ".debug)(" + a1 + "." + a2 + ")", globals())
	# exec(''.join([str(key) for key, val in globals().items() if val == x.__self__]) + "." + x.__name__ + " =  dec2_cond(" + ''.join([str(key) for key, val in globals().items() if val == x.__self__]) + ".debug)(" + ''.join([str(key) for key, val in globals().items() if val ==  x.__self__]) + "." + x.__name__ + ")", globals())
	# decor = lambda x, y: exec(list(x.__self__.__dict__)[0] + "." + x.__name__ + " = " + y.__name__ + "(" + list(x.__self__.__dict__)[0] + "." + x.__name__ + ".debug)(" + list(x.__self__.__dict__)[0] + "." + x.__name__ + ")", globals())
	pass
	
# decor = lambda x, y, z, w: exec(''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + x.__name__ + " = " + z + "(" + ''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + z + ")(" + ''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + x.__name__ + ")", y)
decor = lambda x, y, z, w: exec(w + "." + x + " = Test_dec(" + z[1] + ", '" + z[0] + "')(" + w + "." + x + ")", y)
# decor = lambda x, y, z: exec(''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + x.__name__ + " = Test_dec(" +    ''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + z[0] + ", " + z + ")(" + ''.join([str(key) for key, val in y.items() if val == x.__self__]) + "." + x.__name__ + ")", y)

def decorate(self, name, decs, globe):
	attrs = [getattr(self, func) for func in __getmethods__(self)]
	print("attrs: ", __getmethods__(self))
	print("decs: ", decs)

	# print([[(attr, dec) for dec in decs.keys()] for attr in attrs])
	# [[decor(attr, globe, dec) for dec in decs.keys()] for attr in attrs]
	# for attr in attrs:
		# for dec, cond in decs.items():
			# t = Test_dec(cond, dec)
			# t(eval(str(attr.__self__)))	
			# decor(attr, globe, )
			# pass
		# pass	
	# a = 
	# [[decor(attr, globe, str(eval("Test_dec(val, dec)"))) for dec, val in decs.items()] for attr in attrs]
	# a = ''.join([str(key) for key, val in globe.items() if val == attrs[0].__self__])
	# print([eval("getattr(" + ''.join([str(key) for key, val in globe.items() if val == attr.__self__]) + ", attr.__name__)") for attr in attrs])
	# print(self.__class__)

	[[decor(attr.__name__, globe, (dec, str(cond)), name) for dec, cond in decs.items()] for attr in attrs]

def __getmethods__(self):
	state, res = False, []
	for func in self.__dir__():
		if func[-2:] == "__": state = True
		if state and func[-2:] != "__": res.append(func)
	return res

if __name__ == "__main__":
	d = bool(int(sys.argv[1]))

	# t.func3(3)
	decs = {"debug_decor": d, "pretty": d, "test": not d}
	t = Cfunc3(args = decs)
	# print(t.__dir__())
	# print(__getmethods__(t))

	t.func3(d)

	print("Running decorate")
	# decorate(t, decs, dict(decs, **{'t': t}))
	decorate(t, 't', decs, globals())
	print("\n\nRunning funcions")
	# t.func3 = Test_dec(d, "heh")(t.func3)
	t.func3(d)
	t.func4()
