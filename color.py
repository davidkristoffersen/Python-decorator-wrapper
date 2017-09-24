#!/usr/bin/env python3

import os

class Colors():
	def __init__(self):
		self.pre 	= "\x1b[38;2;"
		self.post 	= "\x1b[m"
		self.color = { 	"Normal:":	"255;255;255m",
						"red": 		"255;50;50m",
						"blue":		"100;100;255m",
						"green":	"100;255;100m",
						"yellow":	"255;255;100m",
						"cyan":		"100;255;255m",
						"purple":	"255;100;255m",
						"Light:":	"255;255;255m",
						"red_l": 	"255;200;200m",
						"blue_l":	"200;200;255m",
						"green_l":	"200;255;200m",
						"yellow_l":	"255;255;200m",
						"cyan_l":	"200;255;255m",
						"purple_l":	"255;200;255m",
						"Dark:":	"255;255;255m",
						"red_d": 	"255;0;0m",
						"blue_d":	"0;0;255m",
						"green_d":	"0;255;0m",
						"yellow_d":	"255;255;0m",
						"cyan_d":	"0;255;255m",
						"purple_d":	"255;0;255m",
						"Other:":	"255;255;255m",
						"brown":	"150;75;37m",
						"brown_l":	"200;100;50m",
						"brown_d":	"100;50;25m"}
	def colorize(self, col, msg):
		try:
			return	self.pre + self.color[col] + msg + self.post
		except: return msg

	def __str__(self):
		it = 0
		for key, value in self.color.items(): 
			if list(self.color.items())[-1] == (key, value): return self.pre + value + key + self.post
			if list(self.color.items())[it + 1][0][-1] == ":": print(self.pre + value + key + self.post)
			elif list(self.color.items())[0] == (key, value): print(self.pre + value + key + self.post)
			elif key[-1] == ":": print('\n' + self.pre + value + key + self.post)
			else: print(self.pre + value + key + self.post + ', ', end='')
			it += 1

def get(col, msg):
	c = Colors()
	try:
		return	c.pre + c.color[col] + msg + c.post
	except: return msg

if __name__ == "__main__":
	print(os.path.basename(__file__) + " is not valid as main program!\nTerminating")
	exit(1)
