import datetime
import time
import os
def csv2():
    fo=open("information.csv","r",encoding='UTF-8')
    w=open("information.txt","w",encoding='UTF-8')
    ls=[]
    line = fo.readline()
    i=0
    while line:
        
        line=line.replace("\n","")

        ls.append(line.split(","))
        line = fo.readline()
        
        print(ls)
        
        if not ls:
            break

    
        birth=ls[i][1][6:14]
        
        birth_d = datetime.datetime.strptime(birth, "%Y%m%d")
        today_d = datetime.datetime.now()
        now_y=int(time.strftime("%Y ",time.localtime()))
        birth_t = birth_d.replace(year=today_d.year)
        
        if today_d > birth_t:
            age = today_d.year - birth_d.year
        else:
            age = today_d.year - birth_d.year - 1      
        print(age)


        m=int(ls[i][1][16])
        if m%2==0:
            gender='女'
        else:
            gender='男'
        print(gender)
       
        print(str(ls[i][0]))
       
        w.writelines([str(ls[i][0]),str(age),',',gender,',',ls[i][2]])
        w.writelines(["\n"])

        i+=1

    fo.close()
    w.close()
if __name__ == "__main__":
    csv2() 
   
