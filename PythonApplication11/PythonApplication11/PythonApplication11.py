#coding: cp949
#Lec11-1014: 정규표현식1

import re

#pattern=re.compile("d")

#result=pattern.search("dog")
#print(result)

#result2=pattern.search("dog", 1)
#print(result2)



#멀티라인 출력 옵션
#str='''sample1.
#sample2.
#sample3.'''
##p=re.compile("^.*", re.S)   #시작 문장부터
#p=re.compile(".*$")   #마지막 문장
#result=p.search(str)
#print(result.group())



#group 사용하기
#str=" abc 1234 xyz "
#pattern=re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*")
#result=pattern.match(str)
#print(result.group(1))
#print(result.group(2))



#fullmatch 사용하기
#pattern=re.compile("o[gh]")
#result1=pattern.fullmatch("dog")
#result2=pattern.fullmatch("ogre")
#result3=pattern.fullmatch("doggie", 1, 3)   #0부터 2까지
#print(result1)
#print(result2)
#print(result3)



#split 사용하기
#pattern=re.compile("\W+")
#result=pattern.split("words, words, words.")
#result2=pattern.split("words, words, words.", 1)
#print(result)
#print(result2)

#pattern = re.compile("x*")
#result = pattern.split('axbc')
#print(result)



#탐욕적인 매칭
#str= '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)   #만족되는 순간 더 이상X
#print(result.group(1))



#주민등록번호 정규식 문제
id="940323-2019123"
pattern=re.compile("\d{6}-\d{7}")
result=pattern.fullmatch(id)
print(result)
#print(result.group(1))
#print(result.group(2))