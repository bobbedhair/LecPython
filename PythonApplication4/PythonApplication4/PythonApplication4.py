#Lec0914

#coding:cp949

#def sum_and_mul(a,b):
#    return a+b,a*b

#sum, mul=sum_and_mul(10,30)
#print(sum, mul)


#def printData(data, level=0):
#    for item in data:
#        if isinstance(item, list):
##            for items in item:
##                print(items)
#            printData(item, level+1)   #재귀
#        else:
#            for i in range(level):
#                print("\t", end='')
#            print(item)
           
#import printData

#data=["홍길동", ["베테랑", ["류승완","황정민","유아인"]], 
# "고길동", ["암살", "손님"]]

##printData(data)
#printData.printData(data)

import os

#help(os.mkdir)

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")