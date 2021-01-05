#front end
from tkinter import *
import tkinter.messagebox
import project1_backend as pb

class Namecard:
    
    def __init__(self,root):
       self.root=root 
       self.root.title("namecard management system")
       self.root.geometry(newGeometry="1175x500+0+0")
       self.root.config(bg="grey")
       #变量赋值
       Name=StringVar()
       Workplace=StringVar() 
       Position=StringVar()
       Mail=StringVar()
       Mobile=StringVar()
       Type=StringVar()
       ###########################FUNCTIONS###############Name Workplace Position Mail Mobile
       pb.NamecardData()
       def iExit():
              iExit=tkinter.messagebox.askyesno("","确定退出？")
              if iExit>0:
                     root.destroy()
                     return
       def clearData():
              self.txtName.delete(0,END)
              self.txtWorkplace.delete(0,END)
              self.txtPosition.delete(0,END)
              self.txtMail.delete(0,END)
              self.txtMobile.delete(0,END) 
              self.txtType.delete(0,END)
       pb.NamecardData()             
       def addData():
              if(len(Name.get())!=0):
                     
                     pb.addNCRec(Name.get(),Workplace.get(),Position.get(),Mail.get(),Mobile.get(),Type.get())
                     Namecardlist.delete(0,END)
                     Namecardlist.insert(END,(Name.get(),Workplace.get(),Position.get(),Mail.get(),Mobile.get(),Type.get()))

       def DisplayData():
              Namecardlist.delete(0,END)
              for row in pb.viewData():
                  Namecardlist.insert(END,row)
       def NamecardRec(event):
              global sd
              searchNC = Namecardlist.curselection()[0]
              sd=Namecardlist.get(searchNC)
              self.txtName.delete(0,END)
              self.txtName.insert(END,sd[0])
              self.txtWorkplace.delete(0,END)
              self.txtWorkplace.insert(END,sd[1])
              self.txtPosition.delete(0,END)
              self.txtPosition.insert(END,sd[2])
              self.txtMail.delete(0,END)
              self.txtMail.insert(END,sd[3])
              self.txtMobile.delete(0,END)  
              self.txtMobile.insert(END,sd[4])   
              self.txtType.delete(0,END)  
              self.txtType.insert(END,sd[5])                        
       def DeleteData():
              if(len(Name.get())!=0):
                     pb.deleteRec(sd[0])
                     clearData()
                     DisplayData()
       def searchDatabase():
              Namecardlist.delete(0,END)
              for row in pb.searchData(Name.get()):
                     Namecardlist.insert(END,row)       
       def update():
              if(len(Name.get())!=0):
                     pb.deleteRec(sd[0])
              if(len(Name.get())!=0):
                     pb.addNCRec(Name.get(),Workplace.get(),Position.get(),Mail.get(),Mobile.get(),Type.get())
                     Namecardlist.delete(0,END)
                     Namecardlist.insert(END,(Name.get(),Workplace.get(),Position.get(),Mail.get(),Mobile.get(),Type.get()))  
       def classify():
              Namecardlist.delete(0,END)
              for row in pb.classifyData():
                  Namecardlist.insert(END,row)
       def sort():
              Namecardlist.delete(0,END)
              for row in pb.sortData():
                  Namecardlist.insert(END,row)

       #####################################FRAMES###################################################################
       MainFrame=Frame(self.root,bg="white")
       MainFrame.grid()  #THIS IS MAIN FRAME OUR WINDOW
       TitFrame=Frame(MainFrame,bd=1,padx=54,pady=6,bg="grey",relief=RIDGE)
       TitFrame.pack(side=TOP)#THIS IS STITLE FRAME
    
       self.lblTit=Label(TitFrame,font=('Arial',47,'bold'),text="NameCard Management System",bg="white",fg="black")
       self.lblTit.grid()

       ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=5,pady=5,bg="grey",relief=RIDGE)
       ButtonFrame.pack(side=BOTTOM)#

       DataFrame=Frame(MainFrame,bd=9,width=1300,height=500,padx=20,pady=20,bg="#666",relief=RIDGE)
       DataFrame.pack(side=BOTTOM)#THIS IS STI
         
       DataFrameLeft=LabelFrame(DataFrame,font=('Arial',12,'bold'),bd=1,width=450,height=500,bg="Ghost White",relief=RIDGE,text="名片信息\n")
       DataFrameLeft.pack(side=LEFT)

       DataFrameRight=LabelFrame(DataFrame,font=('Arial',12,'bold'),bd=1,width=450,height=300,bg="Ghost White",relief=RIDGE,text="名片细节\n")
       DataFrameRight.pack(side=RIGHT)
       ############################################Lables and entry widget #################################################################
       

       self.lblName=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Name:",bg="ghost white")
       self.lblName.grid(row=0,column=0,sticky=W)
       
       self.txtName=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Name,bg="ghost white",width=39)
       self.txtName.grid(row=0,column=1)#Name

       self.lblWorkplace=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Workplace:",bg="ghost white")
       self.lblWorkplace.grid(row=2,column=0,sticky=W)
       
       self.txtWorkplace=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Workplace,bg="ghost white",width=39)
       self.txtWorkplace.grid(row=2,column=1)#Workplace

       self.lblPosition=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Position",bg="ghost white")
       self.lblPosition.grid(row=4,column=0,sticky=W)
       
       self.txtPosition=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Position,bg="ghost white",width=39)
       self.txtPosition.grid(row=4,column=1)#dateof birth

       self.lblMail=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Mail:",bg="ghost white")
       self.lblMail.grid(row=6,column=0,sticky=W)
       
       self.txtMail=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Mail,bg="ghost white",width=39)
       self.txtMail.grid(row=6,column=1)#Mail

       self.lblMobile=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Mobile:",bg="ghost white")
       self.lblMobile.grid(row=8,column=0,sticky=W)
       
       self.txtMobile=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Mobile,bg="ghost white",width=39)
       self.txtMobile.grid(row=8,column=1)#mobile

       self.lblType=Label(DataFrameLeft,font=('Arial',12,'bold'),padx=2,pady=3,text="Type:",bg="ghost white")
       self.lblType.grid(row=10,column=0,sticky=W)

       self.txtType=Entry(DataFrameLeft,font=('Arial',12,'bold'),textvariable=Type,bg="ghost white",width=39)
       self.txtType.grid(row=10,column=1)#mobile
       ###############################List Box and ScrollBar Widget############################################
       scrollbar=Scrollbar(DataFrameRight,orient=VERTICAL)
       scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

       Namecardlist=Listbox(DataFrameRight,width=70,height=10,font=('Arial',12,'bold'),selectbackground='#888', yscrollcommand=scrollbar.set)
       Namecardlist.bind('<<ListboxSelect>>',NamecardRec)
       Namecardlist.grid(row=0,column=0,padx=10,pady=2)
       scrollbar.config(command= Namecardlist.yview)

       #######################################Button Widget####################################################
       self.btnAddData=Button(ButtonFrame,text="添加",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=addData)
       self.btnAddData.grid(row=0,column=0)#ADD NEW

       self.btnDisplay=Button(ButtonFrame,text="全部",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=DisplayData)
       self.btnDisplay.grid(row=0,column=1)#DISPLAY

       self.btnClear=Button(ButtonFrame,text="清除",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=clearData)
       self.btnClear.grid(row=0,column=2)#CLEAR

       self.btnDelete=Button(ButtonFrame,text="删除",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=DeleteData)
       self.btnDelete.grid(row=0,column=3)#DELETE

       self.btnSearch=Button(ButtonFrame,text="查找",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=searchDatabase)
       self.btnSearch.grid(row=0,column=4)#SEARCH

       self.btnUpdate=Button(ButtonFrame,text="更新",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=update)
       self.btnUpdate.grid(row=0,column=5)#UPDATE

       self.btnUpdate=Button(ButtonFrame,text="分类统计",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=classify)
       self.btnUpdate.grid(row=0,column=6)#UPDATE

       self.btnUpdate=Button(ButtonFrame,text="排序",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=sort)
       self.btnUpdate.grid(row=0,column=7)#UPDATE

       self.btnExit=Button(ButtonFrame,text="退出",font=('Arial',20,'bold'),height=1,width=6,fg="#666",command=iExit)
       self.btnExit.grid(row=0,column=8)#EXIT

if __name__=='__main__':
   root=Tk()
   application=Namecard(root)
   root.mainloop()