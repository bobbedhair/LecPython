#Lec2-0907

data=['a', 'b', 'c', ['abcd', 'efg']]
#print(data[0])
#print(data[-1])
#print(data[3])
#print(data[3][1])
#print(data[3][2][0])

#b=[1,2,3]
#c=['life', 'is', 'too', 'short']
#f=b+c
#print(f)
#print(b*3)


#guests=['a','b','c','d']
#guests[0]='greenjoa'
#guests[1]=['greenjoa1', 'greenjoa2']
#guests[1:3]=['greenjoa1', 'greenjoa2']

#guests.insert(2,'e')   #2번째 index에 e 추가
#guests.append('greenjoa2') #맨 뒤(-1)에 추가
#print(guests)


#id=['aaa', 'bbb', 'ccc']
#id.insert(1, '111') #id에 비번 추가
#id.insert(3, '222')
#id.insert(5, '333')
#id.insert(2, ['예은', '010']) #정보리스트 추가
#id.insert(5, ['채은', '019'])
#id.insert(8, ['단희', '011'])
#print(id)


#for steps in data :  
#    if isinstance(steps, list) :  
#       for step in steps :
#           print(step)
#    else :
#        print(steps)     #들여쓰기 중요!

#nEntries=len(data)
#for steps in range(nEntries) :
#    print(data[steps])

#for guest in data :
#    print(guest)

scores=[85,62,63,45,90]
scores.sort()
scores.reverse()
print(scores)
top3=scores[0:3]
print(top3)

scores.extend([50,60])
print(scores)
scores.append([55,65])  #리스트 그대로 삽입(2차형태)
print(scores)

#리스트는 값 변경 가능, 튜플은 불가능!
t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=('a','b',('ab','cd'))
print(t5)