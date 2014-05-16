#!/usr/bin/python

import jpype

class LexTo (object):
	def __init__(self):
		jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path=./LongLexTo')
		LongLexTo = jpype.JClass("LongLexTo")
		self.lexto = LongLexTo()
		self.typeString = {}
		self.typeString[0] = "unknown"
		self.typeString[1] = "known"
		self.typeString[2] = "ambiguous"
		self.typeString[3] = "English/Digits"
		self.typeString[4] = "special"

	def tokenize(self, line):
		self.lexto.wordInstance(line)
		typeList = self.lexto.getTypeList()
		typeList = [self.typeString[n] for n in typeList]

		wordList = []
		self.lexto.lineInstance(line)    
		begin = self.lexto.first()
		while self.lexto.hasNext():
			end = self.lexto.next()
			wordList.append( line[begin:end] )
			begin = end

		return wordList, typeList
