#!/usr/bin/python
#-*-coding: utf-8 -*-

from LexTo import LexTo


lexto = LexTo()
text = u"อยากรู้เรื่องยาคูลท์ ถามสาวยาคูลท์สิคะ"
words, types = lexto.tokenize(text)

print('|'.join(words))
print('|'.join(types))
