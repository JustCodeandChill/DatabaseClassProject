from tkinter import *;
import sqlite3;
import tkinter.messagebox as msg;

connect = sqlite3.connect('database2.db');
# cursor move around dtbase

c = connect.cursor();
sql = "INSERT INTO Patient values (?,?,?,?)"

# Empty list for latter append
ids  = []
# tkinter window
class Application:
    def __init__(self, master):
        gray = "#edede8";
        black = "black"
        w = 0;
        h = 100;

        self.master = master;

        # creating the frame in mater
        self.left = Frame(master, width=800, height=720, bg=gray)
        self.left.pack(side=LEFT);

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT);

        # label for window
        self.heading = Label(self.left, text="ABC Hospital", font=('calibri 40 bold'), fg=black, bg=gray)
        self.heading.place(x=0, y=0)

        self.pId = Label(self.left, text="Patient Id", font=('calibri 18 '), fg=black, bg=gray)
        self.pId.place(x=w, y=h)
        h += 50;

        self.name = Label(self.left, text="Patient Name", font=('calibri 18 '), fg=black, bg=gray)
        self.name.place(x=w, y=h)
        h += 50;

        self.SSN = Label(self.left, text="Patient SSN", font=('calibri 18 '), fg=black, bg=gray)
        self.SSN.place(x=w, y=h)
        h += 50;

        self.room = Label(self.left, text="Room patient stay", font=('calibri 18'), fg=black, bg=gray)
        self.room.place(x=w, y=h)
        h += 50;

        # Entry all label
        x = 250;
        h = 110
        self.id_entry = Entry(self.left, width=40);
        self.id_entry.place(x=x, y=h);
        h += 50

        self.name_entry = Entry(self.left, width=40);
        self.name_entry.place(x=x, y=h);
        h += 50

        self.SSN_entry = Entry(self.left, width=40);
        self.SSN_entry.place(x=x, y=h);
        h += 50

        self.roomId_entry = Entry(self.left, width=40);
        self.roomId_entry.place(x=x, y=h);
        h += 50

        self.search = Button(self.left, text="Search patient", width=20, height=2, bg='#35eb2f',
                             command=self.add_patient);
        self.search.place(x=x, y=h)

        self.search = Button(self.right, text="Clear", width=20, height=2, bg='#35eb2f', command=self.destroy_All);
        self.search.place(x=90, y=h)

        #displaying the logs in our right frame
        self.box = Text(self.right, width=50, height = 20);
        self.box.place(x=0, y=40)
    # reating the object
    def add_patient(self):
        # getting input value
        self.pId = self.id_entry.get()
        self.SSN = self.SSN_entry.get()
        self.name = self.name_entry.get()
        self.room = self.roomId_entry.get()

        params = (self.pId, self.SSN, self.name, self.room);
        #
        if (self.isEmpty(self.pId) or self.isEmpty(self.SSN) or self.isEmpty(self.name_entry) or self.isEmpty(
                self.room)):
            msg.showinfo("Warning", "Stop doing that")
        else:

            c.execute(sql, params)
            connect.commit()
            msg.showinfo("Successful", "The " + str(self.name) + " has been added to the table")
            print('Successful added to the table')
            sql2 = "SELECT id FROM Patient"
            self.result = c.execute(sql2)
            for self.row in self.result:
                self.id = self.row[0]
                ids.append(self.id)
            print(ids)
            self.box.insert(END, "The " + str(self.name) + " has been added to the\n")


    def isEmpty(self, a):
        if a == '':
            return True
        else:
            return False

    def destroy_All(self):
        for child in self.left.winfo_children():
            child.destroy()

    def create_right_side(self):
        self.patientPart = Label()


root = Tk();
b = Application(root);

# resolution for window
root.geometry("1200x720+0+0");

# preventing the resize feature
root.resizable(False, False);

# end the loop
root.mainloop();
