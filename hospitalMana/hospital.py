from tkinter import *
import sqlite3
import tkinter.messagebox as msg

# connect to databse
connect = sqlite3.connect('database.db')
# cursor move around dtbase
c = connect.cursor()

gray = "#edede8"
blue = '#6abbfc'
black = "black"
mint = ""

class Application:
    def __init__(self, master):
        # Variables

        w = 0
        h = 100

        # Divide the canvas into 2 parts: Left for showing information, Right for showing menu
        self.master = master
        self.left = Frame(master, width=800, height=720, bg=gray)
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=410, height=720, bg=blue)
        self.right.pack(side=RIGHT)

        # Working with men
        self.create_menu()
        print(self.searchPatient)
        self.name = Label(self.left, text='asd', font='Calibri 28 bold')
        self.name.place(x=0, y=50)

        self.x = Button(self.left, text='delete', command=self.destroy_left_side)
        self.x.place(x=0, y=100)

        self.y = Button(self.right, text='delete', bg='green', command=self.destroy_left_side)
        self.y.place(x=0, y=300)

    def create_menu(self):
        self.create_patient_options()
        self.create_doctor_options()
        self.create_nurse_options()

    def create_patient_options(self):
        self.PatientOptions = self.create_right_heading('Patient', 10, 0)

        self.searchPatient = self.create_right_option('search', 10, 50)
        self.searchPatient.configure(command=self.search_patient)

        self.updatePatient = self.create_right_option('update', 150, 50)
        self.deletePatient = self.create_right_option('delete', 290, 50)

        self.addPatient = self.create_right_option('add', 10, 120)
        self.addPatient.configure(command=self.add_patient)

        # self.showPatientRecord = self.create_right_option('show record', 150, 120)
        # self.showPatientBill = self.create_right_option('show bill', 290, 120)

    def create_doctor_options(self):
        pass

    def create_nurse_options(self):
        pass

    def create_right_heading(self, text, x, y, bg=blue, fg='black'):
        self.name = Label(self.right, text=text, font='Calibri 28 bold', bg=bg, fg=fg)
        self.name.place(x=x, y=y)
        return self.name

    def create_right_option(self, text, x, y, width=15, height=3, bg=blue, fg='black'):
        self.name = Button(self.right, text=text, width=width, height=height, bg=bg, fg=fg)
        self.name.place(x=x, y=y)
        return self.name

    def create_left_heading(self, text, x, y, bg=gray, fg='black', font='Calibri 28 bold'):
        self.name = Label(self.left, text=text, font=font, bg=bg, fg=fg)
        self.name.place(x=x, y=y)
        return self.name

    def create_left_option(self, text, x, y, width=15, height=3, bg=gray, fg='black'):
        self.name = Button(self.left, text=text, width=width, height=height, bg=bg, fg=fg)
        self.name.place(x=x, y=y)
        return self.name

    def create_left_entry(self, x=10, y=40):
        self.name_entry = Entry(self.left, width=40)
        self.name_entry.place(x=x, y=y)
        return self.name_entry

    # open another .py file
    def callback(self):
        exec(open("./patient.py").read())

    # re-render the information on left side
    def destroy_left_side(self):
        for child in self.left.winfo_children():
            child.destroy()

    # Patient window
    def search_patient(self):
        self.destroy_left_side()
        self.render_search_patient_GUI()

    def render_search_patient_GUI(self):
        self.sp_heading = self.create_left_heading('Search Patient', 10, 10, gray)
        text = "This option allows user to find patient based on ID or name"
        self.sp_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.sp_patient_id = self.create_left_heading(text="Patient ID", x=10, y=100, font='Calibri 18 bold')
        self.sp_patient_id_entry = self.create_left_entry(x=180, y=110)

        self.search_button = self.create_left_option('SEARCH', 10, 160)
        self.search_button.configure(command=self.search_patient_basedon_id_or_name)

    def search_patient_basedon_id_or_name(self):
        #Render the result on screen
        self.render_search_patient_info()
        self.render_search_patient_phone()
        self.render_search_patient_address()

    def render_search_patient_info(self):
        # Doing the search query on Patient table
        sql = 'SELECT * FROM main.Patient WHERE pId=?'
        params = (str(self.sp_patient_id_entry.get()))
        result = c.execute(sql, (params,))
        connect.commit()

        #start from x=10, y= 240 Each time y+= 50 x=180, y=240
        self.info_patient_id = self.create_left_heading(text="Patient ID", x=10, y=230, font='Calibri 18 bold')
        self.info_patient_id_entry = self.create_left_entry(x=180, y=240)

        self.info_patient_name = self.create_left_heading(text="Patient Name", x=10, y=280, font='Calibri 18 bold')
        self.info_patient_name_entry = self.create_left_entry(x=180, y=290)

        self.info_patient_gender = self.create_left_heading(text="Patient Gender", x=10, y=330, font='Calibri 18 bold')
        self.info_patient_gender_entry = self.create_left_entry(x=180, y=340)

        self.info_patient_SSN = self.create_left_heading(text="Patient SSN", x=10, y=380, font='Calibri 18 bold')
        self.info_patient_SSN_entry = self.create_left_entry(x=180, y=390)

        self.info_patient_bDay = self.create_left_heading(text="Patient BirthDay", x=10, y=430, font='Calibri 18 bold')
        self.info_patient_bDay_entry = self.create_left_entry(x=180, y=440)

        self.info_patient_room = self.create_left_heading(text="Patient Room", x=10, y=480, font='Calibri 18 bold')
        self.info_patient_room_entry = self.create_left_entry(x=180, y=490)

        for row in result:
            self.info_patient_id_entry.insert(END, str(row[0]))
            self.info_patient_name_entry.insert(END, str(row[1] +" "+ row[2]))
            self.info_patient_gender_entry.insert(END, str(row[3]))
            self.info_patient_SSN_entry.insert(END, str(row[4]))
            self.info_patient_bDay_entry.insert(END, str(row[5]))
            self.info_patient_room_entry.insert(END, str(row[8]))

    def render_search_patient_phone(self):
        self.info_patient_phone_number = self.create_left_heading(text="Patient Phone", x=10, y=530, font='Calibri 18 bold')
        self.info_patient_phone_number_entry = self.create_left_entry(x=180, y=540)

        # Doing the search query on Patient phone
        cx = connect.cursor()
        params = (str(self.sp_patient_id_entry.get()))
        phone_number_sql = 'select * from main.Patient_phoneNumber WHERE pId like ?'
        phone_number = cx.execute(phone_number_sql, (params,))

        connect.commit()
        print(phone_number)
        for row in phone_number:
            self.info_patient_phone_number_entry.insert(END, str(row[0]))
        cx.close()

    def render_search_patient_address(self):
        self.info_patient_address_number = self.create_left_heading(text="Patient address", x=10, y=580, font='Calibri 18 bold')
        self.info_patient_address_number_entry = self.create_left_entry(x=180, y=590)

        # Doing the search query on Patient phone
        z = connect.cursor()
        params = (str(self.sp_patient_id_entry.get()))
        address_number_sql = "select * from main.Patient_address WHERE pId like ?"
        address_number = z.execute(address_number_sql, (params,))
        connect.commit()

        for row1 in address_number:
            self.info_patient_address_number_entry .insert(END, str(row1[0]))

    # add_patient
    def add_patient(self):
        self.destroy_left_side()
        self.render_add_patient_GUI()

    def render_add_patient_GUI(self):
        # instruction
        self.ap_heading = self.create_left_heading('Add Patient', 10, 10, gray)
        text = "This option allows user to add information about Patient. All the input must be fill with correct information"
        text2 = "Example: Id only has 3 character (a Uppercase char and 2-digit num). P for patient, d for doctor, n for nurse"
        self.ap_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 12 bold')
        self.ap_instruction2 = self.create_left_heading(text=text2, x=10, y=90, font='Calibri 12 bold')

        # start x = 10, y = 150 || y += 25
        self.add_patient_id = self.create_left_heading(text="Patient ID", x=10, y=150, font='Calibri 12 bold')
        self.add_patient_id_entry = self.create_left_entry(x=180, y=160)

        self.add_patient_name = self.create_left_heading(text="Patient First, Last Name", x=10, y=180, font='Calibri 12 bold')
        self.add_patient_fname_entry = self.create_left_entry(x=180, y=185)
        self.add_patient_lname_entry = self.create_left_entry(x=450, y=185)

        self.add_patient_gender = self.create_left_heading(text="Patient Gender", x=10, y=205, font='Calibri 12 bold')
        self.add_patient_gender_entry = self.create_left_entry(x=180, y=210)

        self.add_patient_SSN = self.create_left_heading(text="Patient SSN", x=10, y=260, font='Calibri 12 bold')
        self.add_patient_SSN_entry = self.create_left_entry(x=180, y=265)

        self.add_patient_bDay = self.create_left_heading(text="Patient BirthDay", x=10, y=230, font='Calibri 12 bold')
        self.add_patient_bDay_entry = self.create_left_entry(x=180, y=235)

        self.add_patient_room = self.create_left_heading(text="Patient Room", x=10, y=285, font='Calibri 12 bold')
        self.add_patient_room_entry = self.create_left_entry(x=180, y=290)

        self.add_patient_doctor = self.create_left_heading(text="Patient's Doctor", x=10, y=310, font='Calibri 12 bold')
        self.add_patient_doctor_entry = self.create_left_entry(x=180, y=315)

        self.add_patient_nurse = self.create_left_heading(text="Patient's Nurse", x=10, y=335, font='Calibri 12 bold')
        self.add_patient_nurse_entry = self.create_left_entry(x=180, y=340)

        self.create_button = self.create_left_option('ADD', 10, 380)
        self.create_button.configure(command=self.add_patient_to_Patient_Table)

    def add_patient_to_Patient_Table(self):
        # get all the value at entry
        self.ap_pId = str(self.add_patient_id_entry.get())
        self.ap_fName = str(self.add_patient_fname_entry.get())
        self.ap_lName = str(self.add_patient_lname_entry.get())
        self.ap_gender = str(self.add_patient_gender_entry.get())
        self.ap_bDay = str(self.add_patient_bDay_entry.get())
        self.ap_SSN = str(self.add_patient_SSN_entry.get())
        self.ap_room = str(self.add_patient_room_entry.get())
        self.ap_patientDoctor = str(self.add_patient_doctor_entry.get())
        self.ap_patientNurse = str(self.add_patient_nurse_entry.get())

        # insert query
        add_patient_sql = "insert into main.Patient values (?, ?, ?, ?,  ?, ?, ?, ?, ?)"
        params = (self.ap_pId, self.ap_fName, self.ap_lName, self.ap_gender,  self.ap_SSN, self.ap_bDay, self.ap_patientDoctor, self.ap_patientNurse, self.ap_room, )
        c.execute(add_patient_sql, params)
        connect.commit()

        msg.showinfo("Success", "Successfully add " + self.ap_pId + " to the table")
        self.ap_annouce = self.create_left_heading(text="Successfully add " + self.ap_pId + " to the table", x=10, y=450, font='Calibri 12 bold')

root = Tk()
b = Application(root)

root.geometry("1210x720+0+0")
root.resizable(False, False)

root.mainloop()
