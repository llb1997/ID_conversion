import datetime
import time
import os
def csv2():
    f = open("information.csv","r",encoding='UTF-8')             # 返回一个文件对象
    
    w=open("information.txt","w",encoding='UTF-8')
    line = f.readline()             # 调用文件的 readline()方法   
    while line:   
        
        line=line.replace("\n","")

        q=line.split(',')
        
        if not line:
            break
        
        birth=q[1][6:14]
            
        birth_d = datetime.datetime.strptime(birth, "%Y%m%d")
        today_d = datetime.datetime.now()
        now_y=int(time.strftime("%Y ",time.localtime()))
        birth_t = birth_d.replace(year=today_d.year)
            
        if today_d > birth_t:
            age = today_d.year - birth_d.year
        else:
            age = today_d.year - birth_d.year - 1      
        print(age)


        m=int(q[1][16])
        if m%2==0:
            gender='女'
        else:
            gender='男'
        print(gender)
        
        
        w.writelines([str(q[0]),',',str(age),',',gender,',',q[2]])
        w.writelines(["\n"])     
        
        line = f.readline()

    f.close()
    w.close()
if __name__ == "__main__":
    csv2() 
   
