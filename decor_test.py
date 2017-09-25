#!/usr/bin/env python3
import sys, inspect, re
from color import get as col
from decorator import *

class This():	
	def __init__(self, args):
		self.c = 8
		for key, val in args.items(): exec("self." + key + " = " + str(val))

	def parent(self):
		self.rcr = 9
		print("self.rcr =", self.rcr)

class Cfunc3(This):
	def __init__(self, args):
		super().__init__(args)
		self.x = 2

	def printer(self, d3):
		print("In printer: " + str(d3))
		self.y = 3

	def tester(self):
		self.f = 9
		print("In func4")

def cat(self, *args, **kwargs):
	if self.cond: print(col("green", "\ncat_func enter: ") + str(self.f.__name__))
	res = self.f(*args, **kwargs)
	if self.cond: print(col("red", "cat_func exit: ") + str(self.f.__name__))
	return res

def snake():
	if cond: print(col("green", "\nSnake_func enter: ") + str(f.__name__))
	f()
	if cond: print(col("red", "snake_func exit: ") + str(f.__name__))

def dragon():
	if cond: print(col("green", "\nDragon_func enter: ") + str(f.__name__))
	f()
	if cond: print(col("red", "Dragon_func exit: ") + str(f.__name__))

if __name__ == "__main__":
	d = bool(int(sys.argv[1]))

	decor_lib_add("snake", globals())
	decor_lib_add("dragon", globals())
	decor_lib_addraw("cat", globals())

	decs = {"snake": not d, "cat": not d, "dragon": d}
	t = Cfunc3(args = decs)
	decorate(t, 't', decs, globals())

	t.printer(d)
	t.parent()
