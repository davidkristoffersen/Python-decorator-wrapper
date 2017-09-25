#!/usr/bin/env python3
import sys
from decorator import *

class Func_par():	
	def __init__(self, args):
		for key, val in args.items(): exec("self." + key + " = " + str(val))

	def parent(self):
		print("In parent")

class Func(Func_par):
	def __init__(self, args):
		super().__init__(args)

	def child(self):
		print("In child")

def decor1(self, *args, **kwargs):
	if self.cond: print("\ndecor1 enter: " + str(self.f.__name__))
	res = self.f(*args, **kwargs)
	if self.cond: print("decor1 exit: " + str(self.f.__name__))
	return res

def decor2():
	if cond: print("\ndecor2 enter: " + str(f.__name__))
	f()
	if cond: print("decor2 exit: " + str(f.__name__))

def decor3():
	if cond: print("decor3 enter: " + str(f.__name__))
	f()
	if cond: print("decor3 exit: " + str(f.__name__))

if __name__ == "__main__":
	cond = bool(int(sys.argv[1]))

	decor_lib_addraw("decor1", globals())
	decor_lib_add("decor2", globals())
	decor_lib_add("decor3", globals())

	decs = {"decor1": cond, "decor2": not cond, "decor3": cond}
	f = Func(args = decs)
	decorate(f, 'f', decs, globals())

	f.child()
	f.parent()
