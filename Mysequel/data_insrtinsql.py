import mysql.connector as pysql
import random
mycon=pysql.connect(host="localhost",user="root",passwd="Hritik@MySQL",database="menangrie")
enames=['harendra','ashish','sumit','anil','mayank','tarun','anuj','shantanu','shikhar','dave','Rohit','Arpit','Harsh','Abhishek','Aditya','Emiway','Jimin','Lisa','RM','Malik','Tasheen']
dict1={9:'Yash Sir',10:'Saurabh Sir',11:'Rameez Sir',12:'Gautam Sir'}
rolist=[]
cur=mycon.cursor()
for i in range(20):
    clas=random.randint(9,12)
    cls_teacher=dict1[clas]
    roll=random.randint(0,50)
    while roll in rolist:
        roll=random.randint(0,50)
    else:
        rolist.append(roll)
    name=enames[random.randint(0,len(enames)-1)]
    moblist=[0,1,2,3,4,5,6,7,8,9]
    mob=''
    for i in range(10):
        st=str(random.choice(moblist))
        mob+=st
    mobile=int(mob)
    sex='m'
    grade=random.choice(['A','B','C','A+'])
    marks1=random.randint(0,80)
    marks2=random.randint(0,70)
    marks3=random.randint(0,70)
    marks4=random.randint(0,80)
    marks5=random.randint(0,70)
    st="insert into {} values({},'{}',{},'{}',{},{},{},{},{},{})".format('students',roll,name,clas,cls_teacher,mobile,marks1,marks2,marks3,marks4,marks5)
    cur.execute(st)

mycon.commit()