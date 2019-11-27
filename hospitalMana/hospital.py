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

a, b, c = [1, 2, 3]
print(a, b, c)


class Application:
    def __init__(self, master):
        # Variables
        self.input_checker = Checker()
        print(self.input_checker.is_valid_doctorId('D02'))

        # Divide the canvas into 2 parts: Left for showing information, Right for showing menu
        self.master = master
        self.left = Frame(master, width=800, height=720, bg=gray)
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=410, height=720, bg=blue)
        self.right.pack(side=RIGHT)

        # Working with men
        self.create_menu()
        self.name = Label(self.left, text='asd', font='Calibri 28 bold')
        self.name.place(x=0, y=50)

    def create_menu(self):
        self.create_patient_options()  # Line 112 start with CRUD Patient table
        self.create_doctor_options()  # Line 365 start with CRUD Doctor table
        self.create_nurse_options()

    def create_patient_options(self):
        self.PatientOptions = self.create_right_heading('Patient', 10, 0)

        self.searchPatient = self.create_right_option('search', 10, 50)
        self.searchPatient.configure(command=self.search_patient)

        self.updatePatient = self.create_right_option('update', 150, 50)
        self.updatePatient.configure(command=self.update_patient)

        self.deletePatient = self.create_right_option('delete', 290, 50)
        self.deletePatient.configure(command=self.delete_patient)

        self.addPatient = self.create_right_option('add', 10, 120)
        self.addPatient.configure(command=self.add_patient)

        # self.showPatientRecord = self.create_right_option('show record', 150, 120)
        # self.showPatientBill = self.create_right_option('show bill', 290, 120)

    def create_doctor_options(self):
        self.DoctorOptions = self.create_right_heading('Doctor', 10, 200)

        self.searchDoctor = self.create_right_option('search', 10, 250)
        self.searchDoctor.configure(command=self.search_doctor)

        self.updateDoctor = self.create_right_option('update', 150, 250)
        self.updateDoctor.configure(command=self.update_doctor)
        #
        self.deleteDoctor = self.create_right_option('delete', 290, 250)
        self.deleteDoctor.configure(command=self.delete_doctor)
        # #
        self.addDoctor = self.create_right_option('add', 10, 320)
        self.addDoctor.configure(command=self.add_doctor)

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

    # CRUD Operation with Patient Table
    def search_patient(self):
        self.destroy_left_side()
        self.render_search_patient_GUI()

    def render_search_patient_GUI(self):
        self.sp_heading = self.create_left_heading('Search Patient', 10, 10, gray)
        text = "This option allows user to find patient based on ID"
        self.sp_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.sp_patient_id = self.create_left_heading(text="Patient ID", x=10, y=100, font='Calibri 18 bold')
        self.sp_patient_id_entry = self.create_left_entry(x=180, y=110)

        self.search_button = self.create_left_option('SEARCH', 10, 160)
        self.search_button.configure(command=self.search_patient_basedon_id)

    def search_patient_basedon_id(self):
        # Render the result on screen
        self.render_search_patient_info()
        self.render_search_patient_phone()
        self.render_search_patient_address()

    def render_search_patient_info(self):
        # Doing the search query on Patient table
        c1 = connect.cursor()
        sql = "SELECT * FROM main.Patient WHERE pId=?"
        params = (str(self.sp_patient_id_entry.get()),)
        result = c1.execute(sql, params)
        connect.commit()

        # start from x=10, y= 240 Each time y+= 50 x=180, y=240
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

        # Insert founded value in the entry
        for row in result:
            self.info_patient_id_entry.insert(END, str(row[0]))
            self.info_patient_name_entry.insert(END, str(row[1] + " " + row[2]))
            self.info_patient_gender_entry.insert(END, str(row[3]))
            self.info_patient_SSN_entry.insert(END, str(row[4]))
            self.info_patient_bDay_entry.insert(END, str(row[5]))
            self.info_patient_room_entry.insert(END, str(row[8]))

    def render_search_patient_phone(self):
        self.info_patient_phone_number = self.create_left_heading(text="Patient Phone", x=10, y=530,
                                                                  font='Calibri 18 bold')
        self.info_patient_phone_number_entry = self.create_left_entry(x=180, y=540)

        # Doing the search query on Patient phone table
        cx = connect.cursor()
        params = (str(self.sp_patient_id_entry.get()))
        phone_number_sql = 'select * from main.Patient_phoneNumber WHERE pId like ?'
        phone_number = cx.execute(phone_number_sql, (params,))

        connect.commit()
        for row in phone_number:
            self.info_patient_phone_number_entry.insert(END, str(row[0]))
        cx.close()

    def render_search_patient_address(self):
        self.info_patient_address_number = self.create_left_heading(text="Patient address", x=10, y=580,
                                                                    font='Calibri 18 bold')
        self.info_patient_address_number_entry = self.create_left_entry(x=180, y=590)

        # Doing the search query on Patient phone
        z = connect.cursor()
        params = (str(self.sp_patient_id_entry.get()))
        address_number_sql = "select * from main.Patient_address WHERE pId like ?"
        address_number = z.execute(address_number_sql, (params,))
        connect.commit()

        for row1 in address_number:
            self.info_patient_address_number_entry.insert(END, str(row1[0]))

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

        self.add_patient_name = self.create_left_heading(text="Patient First, Last Name", x=10, y=180,
                                                         font='Calibri 12 bold')
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
        params = (
            self.ap_pId, self.ap_fName, self.ap_lName, self.ap_gender, self.ap_SSN, self.ap_bDay, self.ap_patientDoctor,
            self.ap_patientNurse, self.ap_room,)
        c.execute(add_patient_sql, params)
        connect.commit()

        msg.showinfo("Success", "Successfully add " + self.ap_pId + " to the table")
        self.ap_annouce = self.create_left_heading(text="Successfully add " + self.ap_pId + " to the table", x=10,
                                                   y=450, font='Calibri 12 bold')

    def delete_patient(self):
        self.destroy_left_side()
        self.render_delete_patient_GUI()

    def render_delete_patient_GUI(self):
        self.dp_heading = self.create_left_heading('Delete Patient', 10, 10, gray)
        text = "This option allows user to delete patient based on ID"
        self.dp_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.dp_patient_id = self.create_left_heading(text="Patient ID", x=10, y=100, font='Calibri 18 bold')
        self.dp_patient_id_entry = self.create_left_entry(x=180, y=110)

        self.delete_button = self.create_left_option('DELETE', 10, 160)
        self.delete_button.configure(command=self.delete_patient_basedon_id)

    def delete_patient_basedon_id(self):
        delete_sql = "DELETE FROM Patient where Patient.pId like ?"
        self.dp_pId = str(self.dp_patient_id_entry.get())
        print(self.dp_pId)
        params = (str(self.dp_pId),)

        c.execute(delete_sql, params)
        connect.commit()
        msg.showinfo("Delete", "Delete " + self.dp_pId + " From the list of Patient")
        self.ap_annouce = self.create_left_heading(
            text="Successfully delete " + self.dp_pId + " From the list of Patient", x=10, y=280,
            font='Calibri 12 bold')

    def update_patient(self):
        self.destroy_left_side()
        self.render_update_patient_GUI()

    def render_update_patient_GUI(self):
        self.up_heading = self.create_left_heading('Search Patient', 10, 10, gray)
        text = "This option allows user to update information about patient based on ID"
        self.up_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.up_patient_id = self.create_left_heading(text="Patient ID", x=10, y=100, font='Calibri 18 bold')
        self.up_patient_id_entry = self.create_left_entry(x=180, y=110)

        self.update_button = self.create_left_option('SEARCH', 10, 160)
        self.update_button.configure(command=self.update_patient_basedon_id)

    def update_patient_basedon_id(self):
        self.render_update_title_and_entry()

    def render_update_title_and_entry(self):
        self.up_patient_name = self.create_left_heading(text="Patient First, Last Name", x=10, y=220,
                                                        font='Calibri 12 bold')
        self.up_patient_fname_entry = self.create_left_entry(x=180, y=215)
        self.up_patient_lname_entry = self.create_left_entry(x=450, y=215)

        self.up_patient_gender = self.create_left_heading(text="Patient Gender", x=10, y=245, font='Calibri 12 bold')
        self.up_patient_gender_entry = self.create_left_entry(x=180, y=245)

        self.up_patient_SSN = self.create_left_heading(text="Patient SSN", x=10, y=270, font='Calibri 12 bold')
        self.up_patient_SSN_entry = self.create_left_entry(x=180, y=270)

        self.up_patient_bDay = self.create_left_heading(text="Patient BirthDay", x=10, y=295, font='Calibri 12 bold')
        self.up_patient_bDay_entry = self.create_left_entry(x=180, y=295)

        self.up_patient_room = self.create_left_heading(text="Patient Room", x=10, y=320, font='Calibri 12 bold')
        self.up_patient_room_entry = self.create_left_entry(x=180, y=320)

        self.up_patient_doctor = self.create_left_heading(text="Patient's Doctor", x=10, y=345, font='Calibri 12 bold')
        self.up_patient_doctor_entry = self.create_left_entry(x=180, y=345)

        self.up_patient_nurse = self.create_left_heading(text="Patient's Nurse", x=10, y=370, font='Calibri 12 bold')
        self.up_patient_nurse_entry = self.create_left_entry(x=180, y=370)

        self.update_button = self.create_left_option('UPDATE', 10, 400)
        self.update_button.configure(command=self.update_patient_to_Patient_Table)

    def update_patient_to_Patient_Table(self):
        # get values
        self.up_pId = str(self.up_patient_id_entry.get())
        self.up_fName = str(self.up_patient_fname_entry.get())
        self.up_lName = str(self.up_patient_lname_entry.get())
        self.up_gender = str(self.up_patient_gender_entry.get())
        self.up_bDay = str(self.up_patient_bDay_entry.get())
        self.up_SSN = str(self.up_patient_SSN_entry.get())
        self.up_room = str(self.up_patient_room_entry.get())
        self.up_patientDoctor = str(self.up_patient_doctor_entry.get())
        self.up_patientNurse = str(self.up_patient_nurse_entry.get())

        query = "UPDATE Patient SET firstName=?, lastName=?, gender=?, bDay=?, SSN=?, pId=?, nId=?, rId=? where pId = ?"
        params = (self.up_fName, self.up_lName, self.up_gender, self.up_bDay, self.up_SSN, self.up_patientDoctor,
                  self.up_patientNurse, self.up_room, self.up_pId,)
        c.execute(query, params)
        connect.commit()
        msg.showinfo("Success", "Update " + self.up_pId + ".")
        self.up_annouce = self.create_left_heading(
            text="Successfully update " + self.up_pId + " From the list of Patient", x=10, y=460,
            font='Calibri 12 bold')

    # CRUD Operation on Doctor Table
##########################################################################
    def search_doctor(self):
        self.destroy_left_side()
        # !!!
        self.render_search_doctor_GUI()  # Create the instruction at the top of the GUI

    def render_search_doctor_GUI(self):
        self.sd_heading = self.create_left_heading('Search Doctor', 10, 10, gray)
        text = "This option allows user to find doctor based on ID"
        self.sd_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Hold x
        self.sd_doctor_id = self.create_left_heading(text="Doctor ID", x=10, y=100, font='Calibri 18 bold')
        self.sd_doctor_id_entry = self.create_left_entry(x=180, y=110)

        self.search_button = self.create_left_option('SEARCH', 10, 160)
        # !!!!
        self.search_button.configure(
            command=self.search_doctor_basedon_id)  # Create the result at the bottom of the GUI

    def search_doctor_basedon_id(self):
        self.create_search_doctor_label_and_entry()
        self.query_and_return_doctor_info()
        self.render_doctor_info_to_entry()

    def create_search_doctor_label_and_entry(self):
        self.info_doctor_id = self.create_left_heading(text="Doctor ID", x=10, y=230, font='Calibri 18 bold')
        self.info_doctor_id_entry = self.create_left_entry(x=180, y=240)

        self.info_doctor_name = self.create_left_heading(text="Doctor Name", x=10, y=280, font='Calibri 18 bold')
        self.info_doctor_name_entry = self.create_left_entry(x=180, y=290)

        self.info_doctor_bDay = self.create_left_heading(text="Doctor Birth Day", x=10, y=330, font='Calibri 18 bold')
        self.info_doctor_bDay_entry = self.create_left_entry(x=180, y=340)

        self.info_doctor_gender = self.create_left_heading(text="Doctor Gender", x=10, y=380, font='Calibri 18 bold')
        self.info_doctor_gender_entry = self.create_left_entry(x=180, y=390)

        self.info_doctor_salary = self.create_left_heading(text="Doctor Salary", x=10, y=430, font='Calibri 18 bold')
        self.info_doctor_salary_entry = self.create_left_entry(x=180, y=440)

        self.info_doctor_bonus = self.create_left_heading(text="Doctor Bonus", x=10, y=480, font='Calibri 18 bold')
        self.info_doctor_bonus_entry = self.create_left_entry(x=180, y=490)

        self.info_doctor_departmentId = self.create_left_heading(text="Department Id", x=10, y=530,
                                                                 font='Calibri 18 bold')
        self.info_doctor_departmentId_entry = self.create_left_entry(x=180, y=540)

    def query_and_return_doctor_info(self):
        # Doing the search query on Patient table
        c2 = connect.cursor()
        sql = "SELECT * FROM Doctor WHERE dID like ?"
        params = (str(self.sd_doctor_id_entry.get()),)
        result = c2.execute(sql, params)
        connect.commit()
        return result

    def render_doctor_info_to_entry(self):
        # Render info to the GUI
        result = self.query_and_return_doctor_info()
        for row in result:
            self.info_doctor_id_entry.insert(END, str(row[0]))
            self.info_doctor_name_entry.insert(END, str(row[1] + " " + row[2]))
            self.info_doctor_bDay_entry.insert(END, str(row[3]))
            self.info_doctor_gender_entry.insert(END, str(row[4]))
            self.info_doctor_salary_entry.insert(END, str(row[5]))
            self.info_doctor_bonus_entry.insert(END, str(row[6]))
            self.info_doctor_departmentId_entry.insert(END, str(row[7]))

##########################################################################
    def add_doctor(self):
        self.destroy_left_side()
        self.render_add_doctor_GUI()

    def render_add_doctor_GUI(self):
        self.create_add_doctor_label_and_entry()

    def create_add_doctor_label_and_entry(self):
        # instruction
        self.ad_heading = self.create_left_heading('Add Doctor', 10, 10, gray)
        text = "This option allows user to add information about Doctor. All the input must be fill with correct information"
        text2 = "Example: Id only has 3 character (a Uppercase char and 2-digit num). P for patient, d for doctor, n for nurse"
        self.ad_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 12 bold')
        self.ad_instruction2 = self.create_left_heading(text=text2, x=10, y=90, font='Calibri 12 bold')

        # start x = 10, y = 150 || y += 25
        self.add_doctor_id = self.create_left_heading(text="Doctor ID", x=10, y=150, font='Calibri 12 bold')
        self.add_doctor_id_entry = self.create_left_entry(x=180, y=160)

        self.add_doctor_name = self.create_left_heading(text="Doctor First, Last Name", x=10, y=180,
                                                         font='Calibri 12 bold')
        self.add_doctor_fname_entry = self.create_left_entry(x=180, y=185)
        self.add_doctor_lname_entry = self.create_left_entry(x=450, y=185)

        self.add_doctor_gender = self.create_left_heading(text="Doctor Gender", x=10, y=260, font='Calibri 12 bold')
        self.add_doctor_gender_entry = self.create_left_entry(x=180, y=265)

        self.add_doctor_bDay = self.create_left_heading(text="Doctor BirthDay", x=10, y=230, font='Calibri 12 bold')
        self.add_doctor_bDay_entry = self.create_left_entry(x=180, y=235)

        self.add_doctor_salary = self.create_left_heading(text="Doctor Salary", x=10, y=285, font='Calibri 12 bold')
        self.add_doctor_salary_entry = self.create_left_entry(x=180, y=290)

        self.add_doctor_bonus = self.create_left_heading(text="Doctor Bonus", x=10, y=310, font='Calibri 12 bold')
        self.add_doctor_bonus_entry = self.create_left_entry(x=180, y=315)

        self.add_doctor_departmentId = self.create_left_heading(text="Department", x=10, y=335, font='Calibri 12 bold')
        self.add_doctor_departmentId_entry = self.create_left_entry(x=180, y=340)

        # !!! Functional button
        self.add_button = self.create_left_option('ADD', 10, 380)
        self.add_button.configure(command=self.add_doctor_to_Doctor_Table)

    def add_doctor_to_Doctor_Table(self):
        self.get_added_doctor_info()
        self.add_info_to_doctor_table()

    def get_added_doctor_info(self):
        # get all the value at entry
        self.ad_dID = str(self.add_doctor_id_entry.get())
        self.ad_fName = str(self.add_doctor_fname_entry.get())
        self.ad_lName = str(self.add_doctor_lname_entry.get())
        self.ad_gender = str(self.add_doctor_gender_entry.get())
        self.ad_bDay = str(self.add_doctor_bDay_entry.get())
        self.ad_salary = str(self.add_doctor_salary_entry.get())
        self.ad_bonus = str(self.add_doctor_bonus_entry.get())
        self.ad_departmentId = str(self.add_doctor_departmentId_entry.get())

        #Check condition
        if (self.input_checker.is_valid_doctorId(self.ad_dID) == False):
            self.ad_dID = None
        if (self.input_checker.is_valid_departmentID(self.ad_departmentId) == False):
            self.ad_departmentId = None
        if(self.input_checker.is_valid_gender(self.ad_gender) == False):
            self.ad_gender = 'M'
        if (self.input_checker.is_valid_salary(self.ad_salary) == False):
            self.ad_salary = 0
        if (self.input_checker.is_valid_salary(self.ad_bonus) == False):
            self.ad_bonus = 0

    def add_info_to_doctor_table(self):
        # insert query
        if (self.ad_dID == None or self.ad_departmentId == None):
            msg.showinfo("Failed", "Invalid doctor Id or department Id")
            return

        cursor = connect.cursor()
        add_doctor_sql = "insert into main.Doctor values (?, ?, ?, ?,  ?, ?, ?, ?)"
        params = (
            self.ad_dID, self.ad_fName, self.ad_lName, self.ad_bDay, self.ad_gender, self.ad_salary,  self.ad_bonus,
            self.ad_departmentId, )
        cursor.execute(add_doctor_sql, params)
        connect.commit()

        msg.showinfo("Success", "Successfully add " + self.ad_dID + " to the table")
        self.ap_annouce = self.create_left_heading(text="Successfully add " + self.ad_dID + " to the table", x=10,
                                                   y=450, font='Calibri 12 bold')
##########################################################################
    def delete_doctor(self):
        self.destroy_left_side()
        self.render_delete_doctor_GUI()

    def render_delete_doctor_GUI(self):
        self.dd_heading = self.create_left_heading('Delete Doctor', 10, 10, gray)
        text = "This option allows user to delete doctor based on ID"
        self.dd_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.dd_doctor_id = self.create_left_heading(text="Doctor ID", x=10, y=100, font='Calibri 18 bold')
        self.dd_doctor_id_entry = self.create_left_entry(x=180, y=110)

        self.delete_button = self.create_left_option('DELETE', 10, 160)
        self.delete_button.configure(command=self.delete_doctor_basedon_id)

    def delete_doctor_basedon_id(self):
        self.dd_dID = str(self.dd_doctor_id_entry.get())
        if (self.input_checker.is_valid_doctorId(self.dd_dID) == False):
            msg.showinfo("Warning", "Invalid doctorID")
            return

        delete_sql = "DELETE FROM Doctor where dID like ?"
        print(self.dd_dID)
        params = (self.dd_dID,)

        cursor = connect.cursor()
        cursor.execute(delete_sql, params)
        connect.commit()
        msg.showinfo("Delete", "Delete " + self.dd_dID + " From the list of Patient")
        self.ap_annouce = self.create_left_heading(
            text="Successfully delete " + self.self.dd_dID + " From the list of Patient", x=10, y=280,
            font='Calibri 12 bold')

##########################################################################
    def update_doctor(self):
        self.destroy_left_side()
        self.render_update_doctor_GUI()

    def render_update_doctor_GUI(self):
        self.up_heading = self.create_left_heading('Update Doctor', 10, 10, gray)
        text = "This option allows user to update information about doctor based on ID"
        self.up_instruction = self.create_left_heading(text=text, x=10, y=60, font='Calibri 18 bold')

        # x = 10, y =100 and x = 180, y = 110 Giu nguyen x
        self.up_doctor_id = self.create_left_heading(text="Doctor ID", x=10, y=100, font='Calibri 18 bold')
        self.up_doctor_id_entry = self.create_left_entry(x=180, y=110)

        self.update_button = self.create_left_option('SEARCH', 10, 160)
        self.update_button.configure(command=self.update_doctor_basedon_id)

    def update_doctor_basedon_id(self):
        if (self.input_checker.is_valid_doctorId(str(self.up_doctor_id_entry.get())) == False):
            msg.showinfo("Warning", "Invalid doctor Id")
            return
        self.render_update_doctor_title_and_entry()

    def render_update_doctor_title_and_entry(self):
        self.up_doctor_name = self.create_left_heading(text="Doctor First, Last Name", x=10, y=220,
                                                        font='Calibri 12 bold')
        self.up_doctor_fname_entry = self.create_left_entry(x=180, y=215)
        self.up_doctor_lname_entry = self.create_left_entry(x=450, y=215)

        self.up_doctor_gender = self.create_left_heading(text="Doctor Gender", x=10, y=245, font='Calibri 12 bold')
        self.up_doctor_gender_entry = self.create_left_entry(x=180, y=245)

        self.up_doctor_bDay = self.create_left_heading(text="Doctor Birthday", x=10, y=270, font='Calibri 12 bold')
        self.up_doctor_bDay_entry = self.create_left_entry(x=180, y=270)

        self.up_doctor_salary = self.create_left_heading(text="Doctor Salary", x=10, y=295, font='Calibri 12 bold')
        self.up_doctor_salary_entry = self.create_left_entry(x=180, y=295)

        self.up_doctor_bonus = self.create_left_heading(text="Doctor Bonus", x=10, y=320, font='Calibri 12 bold')
        self.up_doctor_bonus_entry = self.create_left_entry(x=180, y=320)

        self.up_doctor_departmentId = self.create_left_heading(text="Department", x=10, y=345, font='Calibri 12 bold')
        self.up_doctor_departmentId_entry = self.create_left_entry(x=180, y=345)

        self.update_button = self.create_left_option('UPDATE', 10, 400)
        self.update_button.configure(command=self.update_doctor_to_Doctor_Table)

    def update_doctor_to_Doctor_Table(self):
        # get values
        self.up_dID = str(self.up_doctor_id_entry.get())
        self.up_fName = str(self.up_doctor_fname_entry.get())
        self.up_lName = str(self.up_doctor_lname_entry.get())
        self.up_gender = str(self.up_doctor_gender_entry.get())
        self.up_bDay = str(self.up_doctor_bDay_entry.get())
        self.up_salary = str(self.up_doctor_salary_entry.get())
        self.up_bonus = str(self.up_doctor_bonus_entry.get())
        self.up_departmentId = str(self.up_doctor_departmentId_entry.get())

        if (self.input_checker.is_valid_departmentID(self.up_departmentId) == False):
            msg.showinfo("Warning", "Invalid department Id")
            return

        if(self.input_checker.is_valid_gender(self.up_gender) == False):
            self.ad_gender = 'M'
        if (self.input_checker.is_valid_salary(self.up_salary) == False):
            self.ad_salary = 0
        if (self.input_checker.is_valid_salary(self.up_bonus) == False):
            self.ad_bonus = 0

        query = "UPDATE Doctor SET firstName=?, lastName=?, birthDay=?, gender=?, salary=?, bonus=?, departmentId=? where dID = ?"
        params = (self.up_fName, self.up_lName, self.up_bDay, self.up_gender, self.up_salary, self.up_bonus,
                  self.up_departmentId, self.up_dID)
        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()
        msg.showinfo("Success", "Update " + self.up_dID + ".")
        self.up_annouce = self.create_left_heading(
            text="Successfully update " + self.up_dID + " From the list of Doctor", x=10, y=460,
            font='Calibri 12 bold')


class Checker:
    def __init__(self):
        pass

    def is_valid_doctorId(self, id):
        if (len(id) != 3):
            return False
        if (id[0] != 'D' or id[1].isnumeric()!= True or id[2].isnumeric()!= True):
            return False
        return True

    def is_valid_patientId(self, id):
        if (len(id) != 3):
            return False
        if (id[0] != 'P' or id[1].isnumeric()!= True or id[2].isnumeric()!= True):
            return False
        return True

    def is_valid_nurseId(self, id):
        if (len(id) != 3):
            return False
        if (id[0] != 'N' or id[1].isnumeric()!= True or id[2].isnumeric()!= True):
            return False
        return True

    def is_valid_departmentID(self,id):
        valid_ids = ('CRD', 'ERD', 'NED', 'ICU', 'GYD', 'GEN')
        if (len(id) != 3):
            return False
        for valid_id in valid_ids:
            if (id == valid_id):
                return True
        return  False

    def is_valid_salary(self,number):
        if (number.isnumeric() == True and float(number) > 0):
            return True
        return False

    def isempty(self, string):
        if (string == None or string == ""):
            return True
        return False

    def is_valid_gender(self,gender):
        if (len(gender) != 1):
            return False
        if (gender == 'F' or gender == 'M'):
            return True
        return False
root = Tk()
b = Application(root)

root.geometry("1210x720+0+0")
root.resizable(False, False)

root.mainloop()
