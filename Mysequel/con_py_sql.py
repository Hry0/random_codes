import mysql.connector as pysql
import random
mycon=pysql.connect(host="localhost",user="root",passwd="Hritik@MySQL",database="menangrie")
enames=['harendra','ashish','sumit','anil','mayank','tarun','anuj','shantanu','shikhar','dave lee','marquess','mrwhosethboss']
eco=[]
cur=mycon.cursor()
for i in range(10):
    ecode=random.randint(4,15)
    while ecode in eco:
        ecode=random.randint(4,15)
    else:
        eco.append(ecode)
    ename=enames[ecode-4]
    sex='m'
    grade=random.choice(['A','B','C','A+'])
    gross=random.randint(4000,12000)
    st="insert into {} values({},'{}','{}','{}',{})".format('employee',ecode,ename,sex,grade,gross)
    cur.execute(st)

mycon.commit()

# def yaa(st):
#     cur=mycon.cursor()
#     cur.execute(st)
#     data=cur.fetchall()
#     print(data)
#     for i in (data):
#         for x in i:
#             st="select * from {}".format(x)
#             cur.execute(st)
#             data=cur.fetchall()
#             for row in data:
#                 print(row)


#     st="create table students\
#         (rollno varchar);"
#     cur.execute(st)
# else:
#     print("not connected")

# mycon.close()
