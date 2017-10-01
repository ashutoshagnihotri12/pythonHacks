#!/bin/usr/python
import sys
class MyClass:
	"""A simple example class"""
	i = 12345

	def f(self):
		return 'hello World!'

class Complex:
	def __init__(self,realpart,imagpart): # Special Method
	    self.realpart = realpart
	    self.imagpart = imagpart

class Dog:
	kind = 'canine'

	def __init__(self,name):
		  self.name = name

class Person:
	def __init__(self,initialAge):
		self.age = initialAge

# def amIOld(self):

#def yearPasses(self):

agey = Person(14)
print(agey.age)

M = MyClass()
print(M.i)
print(M.f())

MM = Complex(3.0,-4.5)
print(MM.realpart)
print(MM.imagpart)

d = Dog('Fido')
e = Dog('Buddy')
print(d.name)
print(d.kind)
print(e.name)
print(e.kind)
# t = int(raw_input())
# for i in range(0, t):
# 	age = int(raw_input())
# 	p = Person(age)
# 	p.amIOld()
# 	for j in range(0, 3):
# 		p.yearPasses()
# 		p.amIOld()
# 		print("")