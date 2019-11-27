from tkinter import *
import tkinter.messagebox as msg
import sqlite3

connect = sqlite3.connect('database2.db')
c = connect.cursor()


class Application:
    def __init__(self, master):
        self.master = master
        self.heading = Label(master, text='Update Patient', fg='steelblue', font=('calibri 40 bold'))
        self.heading.place(x=150, y=0)

        # saerch criteria
        self.name = Label(master, text='Enter Patient Name', font=('calibri 18 bold'))
        self.name.place(x=0, y=60)

        self.name_entry = Entry(master, width=40)
        self.name_entry.place(x=240, y=68)

        self.search = Button(master, text='Search', width=17, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=120)

        self.search = Button(master, text='Delete', width=17, height=1, bg='steelblue', command=self.delete_db)
        self.search.place(x=490, y=120)

        # function to search

    def search_db(self):
        self.input = self.name_entry.get()
        print('In search DB')
        sql = "SELECT * from Patient Where name like ?"
        self.result = c.execute(sql, (self.input,))
        print(self.result)
        for self.row in self.result:
            self.id = self.row[0]
            self.name = self.row[1]
            self.SSN = self.row[2]
            self.room = self.row[3]

        #creating upfate from
        self.uname = Label(self.master, text="NAME", font=('calibri 18 bold'))
        self.uname.place(x=30, y=180)

        self.uSSN = Label(self.master, text="SSN", font=('calibri 18 bold'))
        self.uSSN.place(x=30, y=220)

        self.uroom = Label(self.master, text="ROOM", font=('calibri 18 bold'))
        self.uroom.place(x=30, y=260)
        print('In search DB')

        # entry for each label + fill in the blank
        self.entr2 = Entry(self.master, width=10)
        self.entr2.place(x=300, y=180)
        self.entr2.insert(END, str(self.name))

        self.entr3 = Entry(self.master, width=10)
        self.entr3.place(x=300, y=220)
        self.entr3.insert(END, str(self.SSN))

        self.entr4 = Entry(self.master, width=10)
        self.entr4.place(x=300, y=260)
        self.entr4.insert(END, str(self.room))

        self.update = Button(self.master, text="Update", width=20,height=2,bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

    def update_db(self):
        #declraing the variabel\ #update id
        self.var2 = self.entr2.get()
        self.var3 = self.entr3.get()
        self.var4 = self.entr4.get()

        query = "UPDATE Patient SET name=?, SSN=?, rId=? where id = ?"
        c.execute(query, (self.var2, self.var3, self.var4,self.id))
        connect.commit()
        msg.showinfo("Success","Update " + str(self.name) + ".")

    def delete_db(self):
        sql2 = "DELETE FROM Patient where name like ?"
        self.var2 = self.entr2.get()
        print(self.entr2.get())
        c.execute(sql2, (self.var2,))
        connect.commit()
        msg.showinfo("Delete", "Delete tho")
        self.entr2.destroy()
        self.entr3.destroy()
        self.entr4.destroy()
root = Tk()
b = Application(root)
root.geometry('1200x720+0+0')
root.mainloop()
