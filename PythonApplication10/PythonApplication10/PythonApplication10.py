#coding: cp949
#Lec10-1012: �����Լ�

import os
import sys

#os.system("python test.py a b c")



#���̽� ����� ����Ǿ� �ִ� ��ġ
#print(sys.path)
#sys.path.append("���")



#��ü�� ���¸� �״�� �����Ͽ� ���Ͽ� �����ϰ� �ҷ��´�.
#class Student:
#    def __init__(self, name, age):
#        self.name=name
#        self.age=age

#    def show(self):
#        print("�̸�: "+self.name+", ����: "+self.age)

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



#print(os.environ)   #�ý��� ȯ�溯�� ��(��ųʸ� ��ü�� ��ȯ)



#print(os.getcwd())  #���� ���丮�� ��ġ ��ȯ
#os.chdir('..')      #���� ���丮�� ��ġ ����
#print(os.getcwd())



#���̽��� ������ �ʰ� �����Ѵ�. �����Ҷ� ������ ��ġ�߰Ǹ� �̷� �����..
#os.startfile("C:/Users/im-16/Documents/GitHub\python/PythonApplication10/PythonApplication10/test.txt")



#����: 1. ���� ���丮�� 'sample' ���丮�� �����(�̹� ������ X).
#      2. ���� ���丮(����)�� ��� *.txt������ sample ������ ����
#if(os.path.isdir('sample')==False):
#    os.mkdir('sample')  #���� ������ ������ ����

#import shutil

#����, ���� ���丮�� ���ϸ���Ʈ ��ȯ
#for (path, dir, files) in os.walk('.'):
#    for filename in files:
#        #print(filename)
#        if(filename.find("txt") != -1): #���ϸ��� ���ڿ��� �����ϸ�
#            #print(filename)
#            shutil.copy(filename, "./sample/"+filename)    #���� ����
        


#�Է¹��� �����̳� ���丮�� ��θ� ��ȯ
#print(os.path.dirname("c:/python34/python.exe"))



#���丮�� �ִ� ���� ����Ʈ�� ��ȯ
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



#�ӽ� �����̳� ���丮 �����
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
#print(calendar.weekday(1994, 3, 23))    #��:0



#import random
#rlist=random.sample(range(100), 10)
#print(rlist)
#random.shuffle(rlist)
#print(rlist)



#weighted_choices=[('Red', 3), ('Blue', 1), ('Green', 4), ('Yellow', 2)]

##���1
#choice=[]
#for val, cnt in weighted_choices:
#    for i in range(cnt):
#        choice.append(val)
#print(choice)
##���2
#population=[val for val, cnt in weighted_choices for i in range(cnt)]
#print(population)



#���������� �ڵ����� ����
#import webbrowser

#url="http://www.naver.com"
#webbrowser.open_new(url)