#Lec0909  
 
#dic1={} 
#dic2=dict() 
#dic={'name':'pey', 'phone':'01023975904', 'birth':'1118'} 
#a={1:'hi'} 
#b={'a':[1,2,3]} 
#print(dic['name']) 
 
#c=dic.keys() 
#print(c) 
 
#movie={'ȫ�浿':{'���׶�':5.0, '�ϻ�':4.5}, 
#       '��浿':{'��Ƽ�λ��̵�':4.0, '�մ�':3.5}} 
#print(movie['ȫ�浿']['�ϻ�']) 
#print(movie.get('ȫ�浿').get("�ϻ�")) 
 
#answer=(input('Would you like express shipping? ')).lower(); 
#if answer.upper()=='YES' : 
#    print('That will be an extra $10.') 
 
#a=[(1,2),(3,4),(5,6)] 
#for (first, last) in a: 
#    print(first+last) 
 
for i in range(2,10): 
    for j in range(1,10): 
        print('%d*%d=%d ' %(i,j,i*j), end='') 
    print('') 


#import turtle 
#nSides=3 
#for steps in range(nSides): 
#    turtle.forward(100) 
#    turtle.right(360/nSides) 
#    for moresteps in range(nSides): 
#        turtle.forward(50) 
#        turtle.right(360/nSides) 
 
#import turtle 
#for steps in['red','blue','green','yellow']: 
#    turtle.color(steps) 
#    turtle.forward(100) 
#    turtle.right(90) 
 
 
#prompt=""" 
#1. Add 
#2. Del 
#3. List 
#4. Quit 

#Enter number: """ 

#number=0 
#while number!=4: 
#    print(prompt, end="") 
#    number=int(input())