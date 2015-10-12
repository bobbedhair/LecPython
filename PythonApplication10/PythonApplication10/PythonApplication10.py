#coding: cp949
#Lec10-1012: 외장함수

import os
import sys

#os.system("python test.py a b c")



#파이썬 모듈이 저장되어 있는 위치
#print(sys.path)
#sys.path.append("경로")



#객체의 형태를 그대로 유지하여 파일에 저장하고 불러온다.
#class Student:
#    def __init__(self, name, age):
#        self.name=name
#        self.age=age

#    def show(self):
#        print("이름: "+self.name+", 나이: "+self.age)

#s1=Student("Yeaeun Kang", "22")
#s1.show()

#import pickle

#f=open("test.txt", "wb")
#data=str("Name: "+s1.name+", Age: "+s1.age)
#pickle.dump(data, f)
#f.close()

#f=open("test.txt", "rb")
#data=pickle.load(f)
#print(data)



#print(os.environ)   #시스템 환경변수 값(딕셔너리 객체로 반환)



#print(os.getcwd())  #현재 디렉토리의 위치 반환
#os.chdir('..')      #현재 디렉토리의 위치 변경
#print(os.getcwd())



#파이썬을 멈추지 않고 실행한다. 과제할때 모듈까지 설치했건만 이런 방법이..
#os.startfile("C:/Users/im-16/Documents/GitHub\python/PythonApplication10/PythonApplication10/test.txt")



#문제: 1. 현재 디렉토리에 'sample' 디렉토리를 만든다(이미 있으면 X).
#      2. 현재 디렉토리(하위)의 모든 *.txt파일을 sample 폴더에 복사
#if(os.path.isdir('sample')==False):
#    os.mkdir('sample')  #기존 폴더가 없으면 생성

#import shutil

#현재, 하위 디렉토리의 파일리스트 반환
#for (path, dir, files) in os.walk('.'):
#    for filename in files:
#        #print(filename)
#        if(filename.find("txt") != -1): #파일명이 문자열을 포함하면
#            #print(filename)
#            shutil.copy(filename, "./sample/"+filename)    #파일 복사
        


#입력받은 파일이나 디렉토리의 경로를 반환
#print(os.path.dirname("c:/python34/python.exe"))



#디렉토리에 있는 파일 리스트를 반환
import glob

#os.chdir("C:\\Python34")
#for i in glob.iglob('*'):
#     print(i)



ndir = nfile = 0 
def traverse(dir, depth): 
    global ndir, nfile 
    for obj in glob.glob(dir + '/*'): 
        if depth == 0: 
            prefix = '|--' 
        else: 
            prefix = '|' + ' ' * depth + '|--' 
            
        if os.path.isdir(obj): 
            ndir += 1 
            print(prefix + os.path.basename(obj)) 
            traverse(obj, depth+1) 
        elif os.path.isfile(obj) : 
            nfile +=1 
            print(prefix + os.path.basename(obj)) 
        else: 
            print(prefix + 'unknown object:',obj) 
            
if __name__ == '__main__': 
    traverse('..', 0) 
    print('\n',ndir,'directories,',nfile, 'files')



#임시 파일이나 디렉토리 만들기
#import tempfile
#import time
#with tempfile.TemporaryFile('w+', delete=True) as fp:
#    fp.write('Hello world!')
#    fp.seek(0)
#    data = fp.read()
#    data2=fp.name
#    print(data)
#    print(data2)
#    time.sleep(5)



#import time

#time1=time.ctime(1234567)
#t=time.strptime(time1)
#print(time1)
#print(t)



#import calendar
#calendar.prcal(2015)
#print(calendar.weekday(1994, 3, 23))    #월:0



#import random
#rlist=random.sample(range(100), 10)
#print(rlist)
#random.shuffle(rlist)
#print(rlist)



#weighted_choices=[('Red', 3), ('Blue', 1), ('Green', 4), ('Yellow', 2)]

##방법1
#choice=[]
#for val, cnt in weighted_choices:
#    for i in range(cnt):
#        choice.append(val)
#print(choice)
##방법2
#population=[val for val, cnt in weighted_choices for i in range(cnt)]
#print(population)



#웹브라우저가 자동으로 실행
#import webbrowser

#url="http://www.naver.com"
#webbrowser.open_new(url)