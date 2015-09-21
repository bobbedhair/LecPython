#Lec5-0916

#filename="greenjoa.txt"
#filename="파일입출력예제1.txt"
filename="파일입출력예제2.txt"
filename2="Monica.txt"

roles=[]
import pickle

#파일 생성 및 열어서 쓰기
#with open(filename, "w+") as myfile:
#    myfile.write("201311189 강령현\n")
#    myfile.write("201311190 강예은\n")
#    myfile.write("201311191 강재구\n")
#    myfile.write("201311192 강현정\n")

#파일 읽기
#with open(filename, "r") as myfile, open(filename2, "w") as monica:
with open(filename, "r") as myfile, open(filename2, "wb") as monica:    #pickle 사용
#    content=myfile.read()
#    print(content)         #전체 출력
#    for line in myfile:    #한 줄씩 띄어서 출력    
#        print(line)

    for content in myfile:
        (role, etc)=content.strip().split(":", 1)   #':'을 기점으로 한번만 분리
        
        #if (role=="Monica"):   #Monica의 대사만 저장
        #    content.strip()
        #    monica.write(etc)
        #    monica.write("\n")
        
        roles.append(role)  #리스트(roles)에 role 저장
    pickle.dump(roles, monica)

with open(filename2, "rb") as monica:
    result=pickle.load(monica)
    print(result)