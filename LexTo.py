#!/usr/bin/python
# -*- coding: utf-8 -*-

import jpype
import os

class LexTo (object):
	def __init__(self):
		filePath = os.path.abspath(os.path.dirname(__file__))
		jpype.startJVM(jpype.getDefaultJVMPath(), '-ea', '-Djava.class.path=%s/LongLexTo' % (filePath))
		
		LongLexTo = jpype.JClass("LongLexTo")
		self.lexto = LongLexTo('%s/lexitron.txt' % (filePath))
		self.typeString = {}
		self.typeString[0] = "unknown"
		self.typeString[1] = "known"
		self.typeString[2] = "ambiguous"
		self.typeString[3] = "English/Digits"
		self.typeString[4] = "special"

	def tokenize(self, line):
		line = line.strip()
	
		self.lexto.wordInstance(line)
		typeList = self.lexto.getTypeList()
		typeList = [self.typeString[n.value] for n in typeList]

		wordList = []  
		begin = self.lexto.first()
		while self.lexto.hasNext():
			end = self.lexto.next()
			wordList.append( line[begin:end] )
			begin = end

		return wordList, typeList
