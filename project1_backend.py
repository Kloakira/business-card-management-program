import mysql.connector


def NamecardData():#建表
        con = mysql.connector.connect(# 打开数据库连接
            host="localhost",
            user="root",
            passwd="root",
            database="project")
        cur=con.cursor()# 使用cursor()方法获取操作游标
        cur.execute("CREATE TABLE IF NOT EXISTS namecard(id integer primary key AUTO_INCREMENT,Name VARCHAR(50) character set utf8 ,Workplace VARCHAR(50) character set utf8,Position VARCHAR(50) character set utf8,Mail VARCHAR(50),Mobile VARCHAR(50),Type VARCHAR(50) character set utf8)")
        con.commit()# 提交到数据库执行
        con.close()# 关闭数据库连接
''' 
    =================================    
        addNCRec 插入
        viewData 打印
        deleteRec 根据指定的名字删除
        searchData 根据指定的名字查找
        dataUpdate 更新
        classifyData 分类统计
        sort 排序
    =================================
'''
def addNCRec(Name,Workplace,Position,Mail,Mobile,Type):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("INSERT INTO namecard VALUES(NULL,%s,%s,%s,%s,%s,%s)",(Name,Workplace,Position,Mail,Mobile,Type))
        con.commit()
        con.close() 
def viewData():
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("select Name,Workplace,Position,Mail,Mobile,Type from namecard")
        row=cur.fetchall()#fetchall(): 接收全部的返回结果行.
        con.close()       
        return row
def deleteRec(Name):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("DELETE FROM namecard WHERE Name=%s",(Name,))
        con.commit()
        con.close()         
def searchData(Name):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT Name,Workplace,Position,Mail,Mobile,Type FROM namecard WHERE Name=%s",(Name,))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,Name="",Workplace="",Position="",Mail="",Mobile="",Type=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("UPDATE namecard SET %s,Name=%s,Workplace=%s,Position=%s,Mail=%s,Mobile=%s Type=%s WHERE id=%s",(Name,Workplace,Position,Mail,Mobile,Type))
        con.commit()
        con.close()    
def classifyData():#分类统计（各行业所拥有的名片数）
        con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT Type , COUNT(*) FROM namecard GROUP BY Type")
        row=cur.fetchall()
        con.close()       
        return row
def sortData():#根据Type即名片（行业）类型排序
        con = mysql.connector.connect(host="localhost",user="root",passwd="root")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT Name,Workplace,Position,Mail,Mobile,Type FROM namecard ORDER BY Type ASC")
        row=cur.fetchall()
        con.close()       
        return row