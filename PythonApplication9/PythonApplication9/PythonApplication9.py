#Lec9-1007: �����Լ�
#coding:cp949

#num=[1,2,3,4]
#print(dir(num))


#data=list(enumerate("greenjoa"))
#print(data)


#print(eval('1+2'))
#print(eval('divmod(4,3)'))


#def positive(l):
#    return l%2==0

#print(list(filter(positive, [1,-3,2,0,-5,6])))


#a=3
#print(id(3))
#print(id(a))    #id���� ����.


#print(list(filter(lambda x: x%2==0, [1,-3,2,0,-5,6])))


#a=[1,2,3]
#b=list(a)
#c=a             #����

#print(a)
#print(b)
#print(c)        #��� ����.
#print(id(a))
#print(id(b))    #a�� �ٸ���.
#print(id(c))    #a�� ����.


#def two_times(x): return x*2
#print(list(map(two_times, [1,2,3,4])))


#print(eval(repr("hello".upper())))
#print(eval(str("hello".upper())))   #���� �߻�


#list=[7,4,6,3,2,5,8]
#list.sort()
#print(list)

#print(sorted([7,4,6,3,2,5,8]))
#print(sorted("zero"))
#print(sorted(['a','c','d','e','b']))


#print(list(zip([1,2,3],[4,5,6],[7,8,9])))


#Quiz
data={"ȫ�浿": [80,70,60,92], 
       "��浿": [24,35,18,10], 
        "��浿": [10,20,8,5]}

value=data.values()
key=sorted(data.keys())

for item in value:
    if isinstance(item, list):
        item.sort()
  
print(data["ȫ�浿"])
key.sort()
print(data)