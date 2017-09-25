#!/usr/bin/env python3

import sys, inspect, re
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
		inner.__dir__ = self.f.__dir__
		return inner

	def __add__(self, func):
		f = eval("inspect.getsourcelines(" + func[0] + ")", func[1])[0]
		def replace(var, b, e, r, new):
			start = var.find(b)
			end = var.find(e)
			if not(start != -1 and end != -1): 
				return var.split('\n')
			var_s = var[:start]
			var_e = var[end:]
			if r == '': var = var[: start + len(b)] + new + var_e
			else: 		var = var_s + var[start:end].replace(r, new) + var_e
			return var.split('\n')
		
		f = ''.join(f).split('\n')
		f = replace(f[0], '(', ':', ')', "self, *args, **kwargs)") + f[1:]

		for idx, line in enumerate(f[1:]):
			f = f[:idx + 1] + replace(f[idx + 1], 'if ', ':', 'cond', "self.cond") + f[idx + 2:]
			f = f[:idx + 1] + replace(f[idx + 1], 'f(', ')', '', "*args, **kwargs") + f[idx + 2:]
			f = f[:idx + 1] + replace(f[idx + 1], '\t', 'f(', '', "res = self.") + f[idx + 2:]
			f = f[:idx + 1] + replace(f[idx + 1], 'str(', 'f.__name__', '', "self.") + f[idx + 2:]

		f.pop()
		f.append("\treturn res")

		exec('\n'.join(f), func[1])
		exec("Decor_lib." + func[0] + " = " + func[0], func[1])

	def __mul__(self, func):
		f = eval("inspect.getsourcelines(" + func[0] + ")", func[1])[0]
		exec('\n'.join(f), func[1])
		exec("Decor_lib." + func[0] + " = " + func[0], func[1])

def decor_lib_add(funcname, globe):
	Decor_lib(True, "add") + (funcname, globe)
def decor_lib_addraw(funcname, globe):
	Decor_lib(True, "add") * (funcname, globe)

if __name__ == "__main__":
	raise BaseException("This program cannot be run as main!")
