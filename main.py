from tkinter import *
from tkinter import messagebox
import mysql.connector

def insertData():
    id = enterId.get()
    name = enterName.get()
    lastName = enterLastName.get()
    dept = enterDept.get()

    if(id == "" or name == "" or lastName == "" or dept == ""):
        messagebox.showwarning("Cannot Insert","All fields are required!")

    # have to check if id is in database before inserting

    else:
        myDB = mysql.connector.connect(host="",user="",password="",database="")
        myCur = myDB.cursor()
        myCur.execute("insert into User values('"+id+"','"+name+"','"+lastName+"','"+dept+"')")
        myDB.commit()
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterLastName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("Insert Status","Data Inserted Successfully")
        myDB.close()

def updateData():
    id = enterId.get()
    name = enterName.get()
    lastName = enterLastName.get()
    dept = enterDept.get()

    if(id == "" or name == "" or lastName == "" or dept == ""):
        messagebox.showwarning("Cannot Update", "All The Fields Are Required!")
    else:
        myDB = mysql.connector.connect(host="", user="", password="", database="")
        myCur = myDB.cursor()
        myCur.execute("update user set FirstName ='"+name+"', LastName = '"+lastName+"', Department='"+dept+"'where ID = '"+id+"'")
        myDB.commit()
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterLastName.delete(0, "end")
        enterDept.delete(0, "end")

        show()

        messagebox.showinfo("Update Status", "Data Updated Successfully")
        myDB.close()

def getData():

    if (enterId.get()==""):
        messagebox.showwarning("Fetch Status","Please provide the ID to fetch the data!")

    else:
        myDB = mysql.connector.connect(host="", user="", password="", database="")
        myCur = myDB.cursor()
        myCur.execute("select * from user where ID = '"+enterId.get()+"' ")
        rows = myCur.fetchall()

        for row in rows:
            enterName.insert(0,row[1])
            enterLastName.insert(0,row[2])
            enterDept.insert(0,row[3])

        myDB.close()

def deleteData():

    if (enterId.get()==""):
        messagebox.showwarning("Cannot Delete","Please provide the ID to delete the data!")

    else:
        myDB = mysql.connector.connect(host="", user="", password="", database="")
        myCur = myDB.cursor()
        myCur.execute("delete from user where ID ='"+enterId.get()+"'")
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterLastName.delete(0, "end")
        enterDept.delete(0, "end")

        show()

        messagebox.showinfo("Delete Status"," Data Deleted Successfully")
        myDB.close()

def show():
    myDB = mysql.connector.connect(host="", user="", password="", database="")
    myCur = myDB.cursor()
    myCur.execute("select * from user")
    rows = myCur.fetchall()
    showData.delete(0,showData.size())

    for row in rows:
        addData = str(row[0])+' '+row[1]+' '+row[2]+' '+row[3]
        showData.insert(showData.size()+1, addData)

    myDB.close()

def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterLastName.delete(0, "end")
    enterDept.delete(0, "end")

    messagebox.showinfo("Reset Status","Completed")

window = Tk()
window.geometry('400x600')
window.title(" My CRUD App")

Id = Label(window, text= "ID", font= ('helvetica',14))
Id.place(x=20,y=30)

firstName = Label(window, text="First Name",font=('helvetica',14))
firstName.place(x=20,y=60)

lastName = Label(window, text="Last Name",font=('helvetica',14))
lastName.place(x=20,y=90)

Dep = Label(window, text="Department",font=("hevetica",14))
Dep.place(x=20,y=120)

enterId = Entry(window)
enterId.place(x=160,y=30)

enterName = Entry(window)
enterName.place(x=160,y=60)

enterLastName = Entry(window)
enterLastName.place(x=160,y=90)

enterDept = Entry(window)
enterDept.place(x=160,y=120)

insertBtn = Button(window,text="Insert",font=('Sans',12), bg = "white",command=insertData)
insertBtn.place(x=20,y=160)

updateBtn = Button(window,text="Update",font=('Sans',12),bg="white", command=updateData)
updateBtn.place(x=80,y=160)

fetchBtn = Button(window,text="Fetch",font=('Sans',12),bg="white", command=getData)
fetchBtn.place(x=150,y=160)

deleteBtn = Button(window,text="Delete",font=('Sans',12),bg="white", command = deleteData)
deleteBtn.place(x=210,y=160)

resetBtn = Button(window,text="Reset",font=('Sans',12),bg="white", command=resetFields)
resetBtn.place(x=280,y=160)

showData = Listbox(window, height=20,width=38)
showData.place(x=20,y=200)

show()

window.mainloop()
