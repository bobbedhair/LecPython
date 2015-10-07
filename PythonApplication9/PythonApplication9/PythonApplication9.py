#Lec9-1007: 내장함수
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
#print(id(a))    #id값이 같다.


#print(list(filter(lambda x: x%2==0, [1,-3,2,0,-5,6])))


#a=[1,2,3]
#b=list(a)
#c=a             #대입

#print(a)
#print(b)
#print(c)        #모두 같다.
#print(id(a))
#print(id(b))    #a와 다르다.
#print(id(c))    #a와 같다.


#def two_times(x): return x*2
#print(list(map(two_times, [1,2,3,4])))


#print(eval(repr("hello".upper())))
#print(eval(str("hello".upper())))   #에러 발생


#list=[7,4,6,3,2,5,8]
#list.sort()
#print(list)

#print(sorted([7,4,6,3,2,5,8]))
#print(sorted("zero"))
#print(sorted(['a','c','d','e','b']))


#print(list(zip([1,2,3],[4,5,6],[7,8,9])))


#Quiz
data={"홍길동": [80,70,60,92], 
       "김길동": [24,35,18,10], 
        "고길동": [10,20,8,5]}

value=data.values()
key=sorted(data.keys())

for item in value:
    if isinstance(item, list):
        item.sort()
  
print(data["홍길동"])
key.sort()
print(data)