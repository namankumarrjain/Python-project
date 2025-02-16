import mysql.connector as a 
con=a.connect(host="localhost",user="root")

c=con.cursor()
c.execute("show databases")
d1=c.fetchall()
d2=[] 

for i in d2: 
	d2.append(i[0])

if 'gshop' in d2:
	sql="use gshop"
	c.execute(sql)
else: 
	sql1="create database gshop"
	c.execute(sql1)
	sql2="use gshop"
	c.execute(sql2)
	sql3="""create table gifts(Name varchar(50),cost integer , buy integer , date varchar(20))"""
	c.execute(sql3)

	sql4="""create table customer(Name varchar(20),Gift varchar(25),Payment integer , date varchar(20),phone varchar(20))"""
	c.execute(sql4)

	sql5="""create table bills(Detail varchar(20),cost integer , date varchar(20))""" 
	c.execute(sql5)

	sql6="""create table worker(Name varchar(100),work varchar(20),salary varchar(20))"""
	c.execute(sql6)
	con.commit()