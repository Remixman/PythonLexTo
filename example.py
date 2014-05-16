#!/usr/bin/python
#-*-coding: utf-8 -*-

from LexTo import LexTo


lexto = LexTo()
text = "อยากรู้เรื่องยาคูลท์ ถามสาวยาคูลท์สิคะ".decode("utf-8")
words, types = lexto.tokenize(text)

print words
print types
