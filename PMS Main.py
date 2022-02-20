import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from db import Database
from tkcalendar import DateEntry
from decimal import *

TWOPLACES = Decimal(10) ** -2

db = Database("PAYROLL.db")

log = Tk()
log.title("ADMIN LOGIN")
log.geometry("1580x700+0+0")
log.config(background="#f1dcfa")
log.resizable(width=FALSE, height=FALSE)

icon = PhotoImage(file='NicePng_accounting-icon-png_3032132.png')
log.iconphoto(True, icon)

main_label = Label(log, font=('Tw Cen MT Condensed Extra Bold', 47),
                   text=" PAYROLL MANAGEMENT SYSTEM", fg="#f0cb7d", bg="#7b0cab", compound=CENTER, height=2,
                   width=55)
main_label.place(x=0, y=0)

username_label = Label(log, text="USER NAME", font=("Consolas", 14, 'bold'), fg="#7b0cab", bg="#f1dcfa")
username_label.place(x=600, y=280)
password_label = Label(log, text="PASSWORD", font=("Consolas", 14, 'bold'), fg="#7b0cab", bg="#f1dcfa")
password_label.place(x=600, y=350)

name_entry = Entry(log, font=("Consolas", 14), width=30)
name_entry.place(x=710, y=280)
password_entry = Entry(log, font=("Consolas", 14), width=30, show="•")
password_entry.place(x=710, y=350)


def try_login():
    if name_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror("Error in Input", "Please Fill All the Details")
        return

    if db.credential(name_entry.get(), password_entry.get()):
        company_id = db.credential(name_entry.get(), password_entry.get())
        name_entry.delete(0, END)
        password_entry.delete(0, END)
        log.withdraw()

        class App(Tk):
            def __init__(self):
                super(App, self).__init__()

                self.title("PAYROLL MANAGEMENT SYSTEM")
                self.config(background="#f1dcfa")
                self.minsize(width=1580, height=700)
                self.resizable(width=FALSE, height=FALSE)

                tab_control = ttk.Notebook(self)

                self.tab1 = ttk.Frame(tab_control)
                tab_control.add(self.tab1, text="Employee's Information")
                tab_control.pack(expand=1, fill="both")

                self.tab2 = ttk.Frame(tab_control)
                tab_control.add(self.tab2, text="Payroll")
                tab_control.pack(expand=1, fill="both")

                self.tab3 = ttk.Frame(tab_control)
                tab_control.add(self.tab3, text="View Records")
                tab_control.pack(expand=1, fill="both")

                self.widgets()

            def widgets(self):
                # ======= SETTING MAIN COLOR BACKGROUNDS==========

                lbl_payroll_main = Label(self.tab1, bg="#f1dcfa", compound=LEFT, height=700, width=1580)
                lbl_payroll_main.place(x=0, y=0)

                lbl_payroll_main = Label(self.tab2, bg="#f1dcfa", compound=LEFT, height=700, width=1580)
                lbl_payroll_main.place(x=0, y=0)

                lbl_payroll_main = Label(self.tab3, bg="#f1dcfa", compound=LEFT, height=700, width=1580)
                lbl_payroll_main.place(x=0, y=0)

                # =============================== TAB 1 - EMPLOYEE'S INFORMATION =======================================
                def log_out():
                    log_out_confirm = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
                    if log_out_confirm == 1:
                        app.destroy()
                        log.deiconify()

                def confirm_exit():
                    exit_system = messagebox.askyesno("System", "Do you want to exit the system?")
                    if exit_system == 1:
                        exit()

                lbl_payroll_main = Label(self.tab1, font=('Tw Cen MT Condensed Extra Bold', 47),
                                         text=" PAYROLL MANAGEMENT SYSTEM", fg="#f0cb7d", bg="#7b0cab", compound=CENTER,
                                         height=2, width=55)
                lbl_payroll_main.place(x=0, y=0)

                lbl_emp_heading = Label(self.tab1, font=('Tw Cen MT Condensed Extra Bold', 25),
                                        text="EMPLOYEE'S INFORMATION", fg="white",
                                        bg="#7b0cab", compound=LEFT, width=25, height=1)
                lbl_emp_heading.place(x=70, y=150)

                btn_log_out = Button(self.tab1, text="Log Out", command=log_out, width=15, height=2,
                                     font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa",
                                     activebackground="#f1dcfa",
                                     activeforeground="#7b0cad", relief=FLAT)
                btn_log_out.place(x=10, y=600)

                btn_exit = Button(self.tab1, text="Exit", command=confirm_exit, width=15, height=2,
                                  font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa", activebackground="#f1dcfa",
                                  activeforeground="#7b0cad", relief=FLAT)
                btn_exit.place(x=1410, y=600)

                btn_log_out = Button(self.tab2, text="Log Out", command=log_out, width=15, height=2,
                                     font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa",
                                     activebackground="#f1dcfa",
                                     activeforeground="#7b0cad", relief=FLAT)
                btn_log_out.place(x=10, y=600)

                btn_exit = Button(self.tab2, text="Exit", command=confirm_exit, width=15, height=2,
                                  font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa", activebackground="#f1dcfa",
                                  activeforeground="#7b0cad", relief=FLAT)
                btn_exit.place(x=1410, y=600)

                btn_log_out = Button(self.tab3, text="Log Out", command=log_out, width=15, height=2,
                                     font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa",
                                     activebackground="#f1dcfa",
                                     activeforeground="#7b0cad", relief=FLAT)
                btn_log_out.place(x=10, y=600)

                btn_exit = Button(self.tab3, text="Exit", command=confirm_exit, width=15, height=2,
                                  font=("Consolas", 14, "bold"), fg="#7b0cab", bg="#f1dcfa", activebackground="#f1dcfa",
                                  activeforeground="#7b0cad", relief=FLAT)
                btn_exit.place(x=1410, y=600)

                company_name = db.company_name(company_id)

                # ==================================== LABEL WIDGETS ===================================================

                lbl_emp_id_e = Label(self.tab1, text="Employee ID", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_emp_id_e = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_f_name = Label(self.tab1, text="First Name", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_f_name = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_m_name = Label(self.tab1, text="Middle Name", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_m_name = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_l_name = Label(self.tab1, text="Last Name", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_l_name = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_gender = Label(self.tab1, text="Gender", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                combo_gender = ttk.Combobox(self.tab1, font=("Consolas", 14), width=28, state="readonly")
                combo_gender['values'] = ("Male", "Female")

                lbl_department = Label(self.tab1, text="Department", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                combo_department = ttk.Combobox(self.tab1, font=("Consolas", 14), width=28, state="readonly")
                combo_department['values'] = ("HR", "Accounting", "Payroll", "IT", "Marketing", "Audit", "Legal")

                lbl_pos = Label(self.tab1, text="Position", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_pos = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_reg_rate = Label(self.tab1, text="Regular Rate", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_reg_rate = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_phone = Label(self.tab1, text="Phone Number", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_phone = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_email = Label(self.tab1, text="Email", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_email = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_h_no = Label(self.tab1, text="House No.", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_h_no = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_street_name = Label(self.tab1, text="Street Name", font=("Consolas", 14), bg="#f1dcfa",
                                        fg="#7b0cab")
                txt_street_name = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_subdivision = Label(self.tab1, text="Subdivision", font=("Consolas", 14), bg="#f1dcfa",
                                        fg="#7b0cab")
                txt_subdivision = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_barangay = Label(self.tab1, text="Barangay", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_barangay = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_city = Label(self.tab1, text="City", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_city = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                lbl_zip = Label(self.tab1, text="ZIP Code", font=("Consolas", 14), bg="#f1dcfa", fg="#7b0cab")
                txt_zip = Entry(self.tab1, font=("Consolas", 14), width=30, fg="black")

                # ====================================== FUNCTIONS =====================================================

                def clear_data_emp():
                    txt_emp_id_e.delete(0, END)
                    txt_f_name.delete(0, END)
                    txt_m_name.delete(0, END)
                    txt_l_name.delete(0, END)
                    combo_gender.set('')
                    combo_department.set('')
                    txt_pos.delete(0, END)
                    txt_reg_rate.delete(0, END)
                    txt_phone.delete(0, END)
                    txt_email.delete(0, END)
                    txt_h_no.delete(0, END)
                    txt_street_name.delete(0, END)
                    txt_subdivision.delete(0, END)
                    txt_barangay.delete(0, END)
                    txt_city.delete(0, END)
                    txt_zip.delete(0, END)
                    return

                def back_employee_menu(lbl_enter_id, txt_enter_id, btn_enter_id, btn_back_emp, btn_submit_emp,
                                       btn_clear_emp):
                    lbl_enter_id.place_forget()
                    txt_enter_id.place_forget()
                    btn_enter_id.place_forget()

                    txt_emp_id_e.config(state=NORMAL)
                    txt_f_name.config(state=NORMAL)
                    txt_m_name.config(state=NORMAL)
                    txt_l_name.config(state=NORMAL)
                    combo_gender.config(state=NORMAL)
                    combo_department.config(state=NORMAL)
                    txt_pos.config(state=NORMAL)
                    txt_reg_rate.config(state=NORMAL)
                    txt_phone.config(state=NORMAL)
                    txt_email.config(state=NORMAL)
                    txt_h_no.config(state=NORMAL)
                    txt_street_name.config(state=NORMAL)
                    txt_subdivision.config(state=NORMAL)
                    txt_barangay.config(state=NORMAL)
                    txt_city.config(state=NORMAL)
                    txt_zip.config(state=NORMAL)

                    clear_data_emp()

                    lbl_emp_id_e.place_forget()
                    txt_emp_id_e.place_forget()
                    lbl_f_name.place_forget()
                    txt_f_name.place_forget()
                    lbl_m_name.place_forget()
                    txt_m_name.place_forget()
                    lbl_l_name.place_forget()
                    txt_l_name.place_forget()
                    lbl_gender.place_forget()
                    combo_gender.place_forget()

                    lbl_department.place_forget()
                    combo_department.place_forget()
                    lbl_pos.place_forget()
                    txt_pos.place_forget()
                    lbl_reg_rate.place_forget()
                    txt_reg_rate.place_forget()
                    lbl_phone.place_forget()
                    txt_phone.place_forget()
                    lbl_email.place_forget()
                    txt_email.place_forget()
                    lbl_h_no.place_forget()
                    txt_h_no.place_forget()
                    lbl_street_name.place_forget()
                    txt_street_name.place_forget()
                    lbl_subdivision.place_forget()
                    txt_subdivision.place_forget()
                    lbl_barangay.place_forget()
                    txt_barangay.place_forget()
                    lbl_city.place_forget()
                    txt_city.place_forget()
                    lbl_zip.place_forget()
                    txt_zip.place_forget()

                    btn_back_emp.place_forget()
                    btn_submit_emp.place_forget()
                    btn_clear_emp.place_forget()

                    btn_add_emp.place(x=690, y=220)
                    btn_edit_emp.place(x=690, y=350)
                    btn_delete_emp.place(x=690, y=480)

                def add_employee(btn_add_emp, btn_edit_emp, btn_delete_emp):
                    btn_add_emp.place_forget()
                    btn_edit_emp.place_forget()
                    btn_delete_emp.place_forget()

                    insert_emp_id = db.next_emp_id()
                    txt_emp_id_e.delete(0, END)
                    txt_emp_id_e.insert(0, insert_emp_id)
                    txt_emp_id_e.config(state=DISABLED)

                    lbl_emp_id_e.place(x=270, y=230)
                    txt_emp_id_e.place(x=440, y=230)
                    lbl_f_name.place(x=270, y=270)
                    txt_f_name.place(x=440, y=270)
                    lbl_m_name.place(x=270, y=310)
                    txt_m_name.place(x=440, y=310)
                    lbl_l_name.place(x=270, y=350)
                    txt_l_name.place(x=440, y=350)
                    lbl_gender.place(x=270, y=390)
                    combo_gender.place(x=440, y=390)
                    lbl_department.place(x=270, y=430)
                    combo_department.place(x=440, y=430)
                    lbl_pos.place(x=270, y=470)
                    txt_pos.place(x=440, y=470)
                    lbl_reg_rate.place(x=270, y=510)
                    txt_reg_rate.place(x=440, y=510)
                    lbl_phone.place(x=830, y=230)
                    txt_phone.place(x=1000, y=230)
                    lbl_email.place(x=830, y=270)
                    txt_email.place(x=1000, y=270)
                    lbl_h_no.place(x=830, y=310)
                    txt_h_no.place(x=1000, y=310)
                    lbl_street_name.place(x=830, y=350)
                    txt_street_name.place(x=1000, y=350)
                    lbl_subdivision.place(x=830, y=390)
                    txt_subdivision.place(x=1000, y=390)
                    lbl_barangay.place(x=830, y=430)
                    txt_barangay.place(x=1000, y=430)
                    lbl_city.place(x=830, y=470)
                    txt_city.place(x=1000, y=470)
                    lbl_zip.place(x=830, y=510)
                    txt_zip.place(x=1000, y=510)

                    btn_back_emp.place(x=350, y=590)
                    btn_submit_emp.config(text="Add")
                    btn_submit_emp.config(command=add_emp_database)
                    btn_submit_emp.place(x=700, y=590)
                    btn_clear_emp.place(x=1050, y=590)

                def add_emp_database():

                    if txt_f_name.get() == "" or txt_l_name.get() == "" or combo_gender.get() == "" \
                            or combo_department.get() == "" or txt_pos.get() == "" or txt_reg_rate.get() == "":
                        messagebox.showerror("Error in Input", "Please Fill the Details")
                        return

                    if combo_department.get() == "HR":
                        department_id = 1
                    elif combo_department.get() == "Accounting":
                        department_id = 2
                    elif combo_department.get() == "Payroll":
                        department_id = 3
                    elif combo_department.get() == "IT":
                        department_id = 4
                    elif combo_department.get() == "Marketing":
                        department_id = 5
                    elif combo_department.get() == "Audit":
                        department_id = 6
                    else:
                        department_id = 7

                    regular_rate = float(txt_reg_rate.get())
                    overtime_rate = regular_rate + (1 / 2 * regular_rate)

                    # output null values on database

                    middle_name = txt_m_name.get()
                    if txt_m_name.get() == "":
                        middle_name = None

                    phone_no = txt_phone.get()
                    if txt_phone.get() == "":
                        phone_no = None

                    email = txt_email.get()
                    if txt_email.get() == "":
                        email = None

                    house_no = txt_h_no.get()
                    if txt_h_no.get() == "":
                        house_no = None

                    street_name = txt_street_name.get()
                    if txt_street_name.get() == "":
                        street_name = None

                    subdivision = txt_subdivision.get()
                    if txt_subdivision.get() == "":
                        subdivision = None

                    barangay = txt_barangay.get()
                    if txt_barangay.get() == "":
                        barangay = None

                    city = txt_city.get()
                    if txt_city.get() == "":
                        city = None

                    zip_code = txt_zip.get()
                    if txt_zip.get() == "":
                        zip_code = None

                    db.insert_emp(txt_emp_id_e.get(), company_id, txt_f_name.get(), middle_name, txt_l_name.get(),
                                  combo_gender.get(), department_id, txt_pos.get(), txt_reg_rate.get(), overtime_rate,
                                  phone_no, email, house_no, street_name, subdivision, barangay, city, zip_code)

                    messagebox.showinfo("Success", "Record Inserted")

                    insert_emp_id = db.next_emp_id()
                    txt_emp_id_e.config(state=NORMAL)
                    txt_emp_id_e.delete(0, END)
                    txt_emp_id_e.insert(0, insert_emp_id)
                    txt_emp_id_e.config(state=DISABLED)

                    clear_data_emp()

                def edit_emp_id(btn_add, btn_edit, btn_delete):
                    btn_add.place_forget()
                    btn_edit.place_forget()
                    btn_delete.place_forget()

                    lbl_enter_id.place(x=610, y=280)
                    txt_enter_id.place(x=610, y=320)

                    btn_enter_id.place(x=700, y=400)
                    btn_enter_id.config(command=lambda: update_employee(lbl_enter_id, txt_enter_id, btn_enter_id))
                    btn_back_emp.place(x=15, y=600)

                def update_employee(lbl_enter_id, txt_enter_id, btn_enter_id):

                    if txt_enter_id.get() == "":
                        messagebox.showerror("Error in Input", "Please enter Employee ID")
                        return

                    if (int(txt_enter_id.get()),) not in db.validate_emp_id():
                        messagebox.showerror("Error in Input", "This is not an employee of the company")
                        return

                    lbl_enter_id.place_forget()
                    txt_enter_id.place_forget()
                    btn_enter_id.place_forget()

                    (employee_id, company_id, first_name, middle_name, last_name, gender, department_id, position,
                     regular_rate, overtime_rate, phone, email, house_no, street_name, subdivision, barangay,
                     city, zip_code) = db.fetch_emp(txt_enter_id.get())

                    if department_id == 1:
                        department_name = "HR"
                    elif department_id == 2:
                        department_name = "Accounting"
                    elif department_id == 3:
                        department_name = "Payroll"
                    elif department_id == 4:
                        department_name = "IT"
                    elif department_id == 5:
                        department_name = "Marketing"
                    elif department_id == 6:
                        department_name = "Audit"
                    else:
                        department_name = "Legal"

                    lbl_emp_id_e.place(x=270, y=230)
                    txt_emp_id_e.place(x=440, y=230)
                    txt_emp_id_e.config(state=NORMAL)
                    txt_emp_id_e.delete(0, END)
                    txt_emp_id_e.insert(0, employee_id)
                    txt_emp_id_e.config(state=DISABLED)

                    lbl_f_name.place(x=270, y=270)
                    txt_f_name.place(x=440, y=270)
                    txt_f_name.insert(0, first_name)

                    lbl_m_name.place(x=270, y=310)
                    txt_m_name.place(x=440, y=310)
                    if middle_name is not None:
                        txt_m_name.insert(0, middle_name)

                    lbl_l_name.place(x=270, y=350)
                    txt_l_name.place(x=440, y=350)
                    txt_l_name.insert(0, last_name)

                    lbl_gender.place(x=270, y=390)
                    combo_gender.place(x=440, y=390)
                    combo_gender.set(gender)

                    lbl_department.place(x=270, y=430)
                    combo_department.place(x=440, y=430)
                    combo_department.set(department_name)

                    lbl_pos.place(x=270, y=470)
                    txt_pos.place(x=440, y=470)
                    txt_pos.insert(0, position)

                    lbl_reg_rate.place(x=270, y=510)
                    txt_reg_rate.place(x=440, y=510)
                    txt_reg_rate.insert(0, regular_rate)

                    lbl_phone.place(x=830, y=230)
                    txt_phone.place(x=1000, y=230)
                    if phone is not None:
                        txt_phone.insert(0, phone)

                    lbl_email.place(x=830, y=270)
                    txt_email.place(x=1000, y=270)
                    if email is not None:
                        txt_email.insert(0, email)

                    lbl_h_no.place(x=830, y=310)
                    txt_h_no.place(x=1000, y=310)
                    if house_no is not None:
                        txt_h_no.insert(0, house_no)

                    lbl_street_name.place(x=830, y=350)
                    txt_street_name.place(x=1000, y=350)
                    if street_name is not None:
                        txt_street_name.insert(0, street_name)

                    lbl_subdivision.place(x=830, y=390)
                    txt_subdivision.place(x=1000, y=390)
                    if subdivision is not None:
                        txt_subdivision.insert(0, subdivision)

                    lbl_barangay.place(x=830, y=430)
                    txt_barangay.place(x=1000, y=430)
                    if barangay is not None:
                        txt_barangay.insert(0, barangay)

                    lbl_city.place(x=830, y=470)
                    txt_city.place(x=1000, y=470)
                    if city is not None:
                        txt_city.insert(0, city)

                    lbl_zip.place(x=830, y=510)
                    txt_zip.place(x=1000, y=510)
                    if zip_code is not None:
                        txt_zip.insert(0, zip_code)

                    btn_back_emp.place(x=350, y=590)
                    btn_submit_emp.config(text="Update")
                    btn_submit_emp.config(command=update_emp_database)
                    btn_submit_emp.place(x=700, y=590)
                    btn_clear_emp.place(x=1050, y=590)

                def update_emp_database():

                    if txt_f_name.get() == "" or txt_l_name.get() == "" or combo_gender.get() == "" \
                            or combo_department.get() == "" or txt_pos.get() == "" or txt_reg_rate.get() == "":
                        messagebox.showerror("Error in Input", "Please Fill the Details")
                        return

                    if combo_department.get() == "HR":
                        department_id = 1
                    elif combo_department.get() == "Accounting":
                        department_id = 2
                    elif combo_department.get() == "Payroll":
                        department_id = 3
                    elif combo_department.get() == "IT":
                        department_id = 4
                    elif combo_department.get() == "Marketing":
                        department_id = 5
                    elif combo_department.get() == "Audit":
                        department_id = 6
                    else:
                        department_id = 7

                    regular_rate = float(txt_reg_rate.get())
                    overtime_rate = regular_rate + (1 / 2 * regular_rate)

                    # if nothing is entered, null will be displayed on the database
                    middle_name = txt_m_name.get()
                    if txt_m_name.get() == "":
                        middle_name = None

                    phone_no = txt_phone.get()
                    if txt_phone.get() == "":
                        phone_no = None

                    email = txt_email.get()
                    if txt_email.get() == "":
                        email = None

                    house_no = txt_h_no.get()
                    if txt_h_no.get() == "":
                        house_no = None

                    street_name = txt_street_name.get()
                    if txt_street_name.get() == "":
                        street_name = None

                    subdivision = txt_subdivision.get()
                    if txt_subdivision.get() == "":
                        subdivision = None

                    barangay = txt_barangay.get()
                    if txt_barangay.get() == "":
                        barangay = None

                    city = txt_city.get()
                    if txt_city.get() == "":
                        city = None

                    zip_code = txt_zip.get()
                    if txt_zip.get() == "":
                        zip_code = None

                    db.update_emp(txt_emp_id_e.get(), company_id, txt_f_name.get(), middle_name, txt_l_name.get(),
                                  combo_gender.get(), department_id, txt_pos.get(), txt_reg_rate.get(), overtime_rate,
                                  phone_no, email, house_no, street_name, subdivision, barangay, city, zip_code)

                    messagebox.showinfo("Success", "Record Updated")

                def delete_emp_id(btn_add_emp, btn_edit_emp, btn_delete_emp):
                    btn_add_emp.place_forget()
                    btn_edit_emp.place_forget()
                    btn_delete_emp.place_forget()

                    lbl_enter_id.place(x=610, y=280)
                    txt_enter_id.place(x=610, y=320)
                    btn_enter_id.place(x=700, y=400)
                    btn_enter_id.config(command=lambda: delete_employee(lbl_enter_id, txt_enter_id, btn_enter_id))
                    btn_back_emp.place(x=15, y=600)

                def delete_employee(lbl_enter_id, txt_enter_id, btn_enter_id):
                    if txt_enter_id.get() == "":
                        messagebox.showerror("Error in Input", "Please enter Employee ID")
                        return

                    if (int(txt_enter_id.get()),) not in db.validate_emp_id():
                        messagebox.showerror("Error in Input", "This is not an employee of the company")
                        return

                    lbl_enter_id.place_forget()
                    txt_enter_id.place_forget()
                    btn_enter_id.place_forget()

                    (employee_id, company_id, first_name, middle_name, last_name, gender, department_id, position,
                     regular_rate, overtime_rate, phone, email, house_no, street_name, subdivision, barangay,
                     city, zip_code) = db.fetch_emp(txt_enter_id.get())

                    if department_id == 1:
                        department_name = "HR"
                    elif department_id == 2:
                        department_name = "Accounting"
                    elif department_id == 3:
                        department_name = "Payroll"
                    elif department_id == 4:
                        department_name = "IT"
                    elif department_id == 5:
                        department_name = "Marketing"
                    elif department_id == 6:
                        department_name = "Audit"
                    else:
                        department_name = "Legal"

                    lbl_emp_id_e.place(x=270, y=230)
                    txt_emp_id_e.place(x=440, y=230)
                    txt_emp_id_e.config(state=NORMAL)
                    txt_emp_id_e.delete(0, END)
                    txt_emp_id_e.insert(0, employee_id)
                    txt_emp_id_e.config(state=DISABLED)

                    lbl_f_name.place(x=270, y=270)
                    txt_f_name.place(x=440, y=270)
                    txt_f_name.insert(0, first_name)
                    txt_f_name.config(state=DISABLED)

                    lbl_m_name.place(x=270, y=310)
                    txt_m_name.place(x=440, y=310)
                    if middle_name is not None:
                        txt_m_name.insert(0, middle_name)
                    txt_m_name.config(state=DISABLED)

                    lbl_l_name.place(x=270, y=350)
                    txt_l_name.place(x=440, y=350)
                    txt_l_name.insert(0, last_name)
                    txt_l_name.config(state=DISABLED)

                    lbl_gender.place(x=270, y=390)
                    combo_gender.place(x=440, y=390)
                    combo_gender.set(gender)
                    combo_gender.config(state=DISABLED)

                    lbl_department.place(x=270, y=430)
                    combo_department.place(x=440, y=430)
                    combo_department.set(department_name)
                    combo_department.config(state=DISABLED)

                    lbl_pos.place(x=270, y=470)
                    txt_pos.place(x=440, y=470)
                    txt_pos.insert(0, position)
                    txt_pos.config(state=DISABLED)

                    lbl_reg_rate.place(x=270, y=510)
                    txt_reg_rate.place(x=440, y=510)
                    txt_reg_rate.insert(0, regular_rate)
                    txt_reg_rate.config(state=DISABLED)

                    lbl_phone.place(x=830, y=230)
                    txt_phone.place(x=1000, y=230)
                    if phone is not None:
                        txt_phone.insert(0, phone)
                    txt_phone.config(state=DISABLED)

                    lbl_email.place(x=830, y=270)
                    txt_email.place(x=1000, y=270)
                    if email is not None:
                        txt_email.insert(0, email)
                    txt_email.config(state=DISABLED)

                    lbl_h_no.place(x=830, y=310)
                    txt_h_no.place(x=1000, y=310)
                    if house_no is not None:
                        txt_h_no.insert(0, house_no)
                    txt_h_no.config(state=DISABLED)

                    lbl_street_name.place(x=830, y=350)
                    txt_street_name.place(x=1000, y=350)
                    if street_name is not None:
                        txt_street_name.insert(0, street_name)
                    txt_street_name.config(state=DISABLED)

                    lbl_subdivision.place(x=830, y=390)
                    txt_subdivision.place(x=1000, y=390)
                    if subdivision is not None:
                        txt_subdivision.insert(0, subdivision)
                    txt_subdivision.config(state=DISABLED)

                    lbl_barangay.place(x=830, y=430)
                    txt_barangay.place(x=1000, y=430)
                    if barangay is not None:
                        txt_barangay.insert(0, barangay)
                    txt_barangay.config(state=DISABLED)

                    lbl_city.place(x=830, y=470)
                    txt_city.place(x=1000, y=470)
                    if city is not None:
                        txt_city.insert(0, city)
                    txt_city.config(state=DISABLED)

                    lbl_zip.place(x=830, y=510)
                    txt_zip.place(x=1000, y=510)
                    if zip_code is not None:
                        txt_zip.insert(0, zip_code)
                    txt_zip.config(state=DISABLED)

                    btn_back_emp.place(x=450, y=590)
                    btn_submit_emp.place(x=800, y=590)
                    btn_submit_emp.config(text="Delete")
                    btn_submit_emp.config(command=delete_emp_database)

                def delete_emp_database():
                    db.remove_emp(txt_emp_id_e.get())
                    txt_emp_id_e.config(state=NORMAL)
                    txt_f_name.config(state=NORMAL)
                    txt_m_name.config(state=NORMAL)
                    txt_l_name.config(state=NORMAL)
                    txt_pos.config(state=NORMAL)
                    txt_reg_rate.config(state=NORMAL)
                    txt_phone.config(state=NORMAL)
                    txt_email.config(state=NORMAL)
                    txt_h_no.config(state=NORMAL)
                    txt_street_name.config(state=NORMAL)
                    txt_subdivision.config(state=NORMAL)
                    txt_barangay.config(state=NORMAL)
                    txt_city.config(state=NORMAL)
                    txt_zip.config(state=NORMAL)

                    clear_data_emp()

                    txt_emp_id_e.config(state=DISABLED)
                    txt_f_name.config(state=DISABLED)
                    txt_m_name.config(state=DISABLED)
                    txt_l_name.config(state=DISABLED)
                    txt_pos.config(state=DISABLED)
                    txt_reg_rate.config(state=DISABLED)
                    txt_phone.config(state=DISABLED)
                    txt_email.config(state=DISABLED)
                    txt_h_no.config(state=DISABLED)
                    txt_street_name.config(state=DISABLED)
                    txt_subdivision.config(state=DISABLED)
                    txt_barangay.config(state=DISABLED)
                    txt_city.config(state=DISABLED)
                    txt_zip.config(state=DISABLED)

                    messagebox.showinfo("Success", "Record Deleted")

                # ===================================== EMPLOYEE BUTTONS ===============================================
                lbl_enter_id = Label(self.tab1, text="Enter Employee ID", font=("Consolas", 17), bg="#f1dcfa",
                                     fg="#7b0cab")

                txt_enter_id = Entry(self.tab1, font=("Consolas", 17), width=30, fg="black")
                btn_enter_id = Button(self.tab1, text="Submit", width=20, height=2, font=("Consolas", 14, "bold"),
                                      fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)

                btn_back_emp = Button(self.tab1, text="Back",
                                      command=lambda: back_employee_menu(btn_back_emp, btn_submit_emp, btn_clear_emp,
                                                                         lbl_enter_id, txt_enter_id, btn_enter_id),
                                      width=17, height=2, font=("Consolas", 14, "bold"), fg="#f0cb7d", bg="#7b0cab",
                                      relief=GROOVE)

                btn_submit_emp = Button(self.tab1, width=17, height=2, font=("Consolas", 14, "bold"),
                                        fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)

                btn_clear_emp = Button(self.tab1, text="Clear Details", command=clear_data_emp,
                                       width=17, height=2, font=("Consolas", 14, "bold"),
                                       fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)

                # ====================================== TAB 1 - EMPLOYEE MENU =========================================

                btn_add_emp = Button(self.tab1, text="Add Employee",
                                     command=lambda: add_employee(btn_add_emp, btn_edit_emp, btn_delete_emp),
                                     width=25, height=3, font=("Consolas", 14, "bold"),
                                     fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)
                btn_add_emp.place(x=690, y=220)

                btn_edit_emp = Button(self.tab1, text="Edit Employee",
                                      command=lambda: edit_emp_id(btn_add_emp, btn_edit_emp, btn_delete_emp),
                                      width=25, height=3, font=("Consolas", 14, "bold"),
                                      fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)
                btn_edit_emp.place(x=690, y=350)

                btn_delete_emp = Button(self.tab1, text="Delete Employee",
                                        command=lambda: delete_emp_id(btn_add_emp, btn_edit_emp, btn_delete_emp),
                                        width=25, height=3, font=("Consolas", 14, "bold"),
                                        fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)
                btn_delete_emp.place(x=690, y=480)

                # ==================================== TAB 2 - PAYROLL =================================================

                lbl_payroll_main = Label(self.tab2, font=('Tw Cen MT Condensed Extra Bold', 47),
                                         text=" PAYROLL MANAGEMENT SYSTEM", fg="#f0cb7d", bg="#7b0cab", compound=CENTER,
                                         height=2, width=55)
                lbl_payroll_main.place(x=0, y=0)

                lbl_payroll_heading = Label(self.tab2, font=('Tw Cen MT Condensed Extra Bold', 25),
                                            text="PAYROLL", fg="white", bg="#7b0cab", compound=LEFT, width=25, height=1)
                lbl_payroll_heading.place(x=70, y=150)

                # ==================================== PAYROLL LABEL WIDGETS ===========================================

                lbl_ref_num = Label(self.tab2, text="Reference Number", font=('Consolas', 14), fg="#7b0cab",
                                    bg="#f1dcfa")
                txt_ref_num = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_date = Label(self.tab2, text="Date", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_date = DateEntry(self.tab2, font=('Consolas', 14), bd=5, width=45, borderwidth=2,
                                     date_pattern='mm/dd/yyyy')
                txt_date.delete(0, END)

                lbl_emp_id_p = Label(self.tab2, text="Employee ID", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_emp_id_p = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_hours_worked = Label(self.tab2, text="Hours Worked", font=('Consolas', 14), fg="#7b0cab",
                                         bg="#f1dcfa")
                txt_hours_worked = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_sss = Label(self.tab2, text="SSS", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_sss = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_hdmf = Label(self.tab2, text="HDMF", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_hdmf = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_philhealth = Label(self.tab2, text="PhilHealth", font=('Consolas', 14,), fg="#7b0cab",
                                       bg="#f1dcfa")
                txt_philhealth = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_wtax = Label(self.tab2, text="Withholding Tax", font=('Consolas', 14), fg="#7b0cab",
                                 bg="#f1dcfa")
                txt_wtax = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                lbl_basic_pay = Label(self.tab2, text="Basic Pay", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_basic_pay = Entry(self.tab2, font=('COnsolas', 14), width=24, justify='left')

                lbl_ot_pay = Label(self.tab2, text="Overtime Pay", font=('Consolas', 14), fg="#7b0cab",
                                   bg="#f1dcfa")
                txt_ot_pay = Entry(self.tab2, font=('COnsolas', 14), width=24, justify='left')

                lbl_total_ded = Label(self.tab2, text="Total Deductions", font=('Consolas', 14), fg="#7b0cab",
                                      bg="#f1dcfa")
                txt_total_ded = Entry(self.tab2, font=('COnsolas', 14), width=24, justify='left')

                lbl_net_pay = Label(self.tab2, text="Net Pay", font=('Consolas', 14), fg="#7b0cab", bg="#f1dcfa")
                txt_net_pay = Entry(self.tab2, font=('Consolas', 14), width=24, justify='left')

                # ======================================= PAY SLIP =====================================================

                payslip = Label(self.tab2, text="Pay Slip", font=('Consolas', 14, 'bold'), fg="#7b0cab",
                                bg="#f1dcfa")
                txt_payslip = Text(self.tab2, height=21, width=54, font=('Consolas', 13), fg="#7b0cab",
                                   bg="white")

                # ====================================== FUNCTIONS =====================================================

                def compute_salary():
                    if (int(txt_emp_id_p.get()),) not in db.validate_emp_id():
                        messagebox.showerror("Error in Input", "Employee ID entered not an employee of the company")
                        return

                    txt_basic_pay.config(state=NORMAL)
                    txt_ot_pay.config(state=NORMAL)
                    txt_total_ded.config(state=NORMAL)
                    txt_net_pay.config(state=NORMAL)
                    txt_payslip.config(state=NORMAL)
                    btn_submit_payroll.config(state=NORMAL)
                    btn_payslip.config(state=NORMAL)

                    txt_basic_pay.delete(0, END)
                    txt_ot_pay.delete(0, END)
                    txt_total_ded.delete(0, END)
                    txt_net_pay.delete(0, END)

                    hours_worked = float(txt_hours_worked.get())

                    global employee_name, regular_rate, overtime_rate
                    employee_name, regular_rate, overtime_rate = db.fetch_rate(txt_emp_id_p.get())

                    sss = float(txt_sss.get())
                    hdmf = float(txt_hdmf.get())
                    phil_health = float(txt_philhealth.get())
                    withholding_tax = float(txt_wtax.get())

                    txt_sss.delete(0, END)
                    txt_hdmf.delete(0, END)
                    txt_philhealth.delete(0, END)
                    txt_wtax.delete(0, END)

                    txt_sss.insert(0, Decimal(sss).quantize(TWOPLACES))
                    txt_hdmf.insert(0, Decimal(hdmf).quantize(TWOPLACES))
                    txt_philhealth.insert(0, Decimal(phil_health).quantize(TWOPLACES))
                    txt_wtax.insert(0, Decimal(withholding_tax).quantize(TWOPLACES))

                    total_deductions = sss + hdmf + phil_health + withholding_tax
                    txt_total_ded.insert(0, Decimal(total_deductions).quantize(TWOPLACES))

                    if hours_worked <= 160:
                        basic_pay = hours_worked * regular_rate
                        txt_basic_pay.insert(0, Decimal(basic_pay).quantize(TWOPLACES))
                        txt_ot_pay.insert(0, Decimal(0.00).quantize(TWOPLACES))

                        net_pay = basic_pay - total_deductions
                        txt_net_pay.insert(0, Decimal(net_pay).quantize(TWOPLACES))

                    elif hours_worked > 160:
                        basic_pay = 160 * regular_rate
                        overtime_pay = ((hours_worked - 160) * overtime_rate)
                        txt_basic_pay.insert(0, Decimal(basic_pay).quantize(TWOPLACES))
                        txt_ot_pay.insert(0, Decimal(overtime_pay).quantize(TWOPLACES))

                        net_pay = (basic_pay + overtime_pay) - total_deductions
                        txt_net_pay.insert(0, Decimal(net_pay).quantize(TWOPLACES))

                    txt_basic_pay.config(state=DISABLED)
                    txt_ot_pay.config(state=DISABLED)
                    txt_total_ded.config(state=DISABLED)
                    txt_net_pay.config(state=DISABLED)

                    return

                def clear_data_payroll():
                    txt_ref_num.delete(0, END)
                    txt_date.delete(0, END)
                    txt_emp_id_p.delete(0, END)
                    txt_hours_worked.delete(0, END)
                    txt_sss.delete(0, END)
                    txt_hdmf.delete(0, END)
                    txt_philhealth.delete(0, END)
                    txt_wtax.delete(0, END)

                    txt_basic_pay.config(state=NORMAL)
                    txt_ot_pay.config(state=NORMAL)
                    txt_total_ded.config(state=NORMAL)
                    txt_net_pay.config(state=NORMAL)

                    txt_basic_pay.delete(0, END)
                    txt_ot_pay.delete(0, END)
                    txt_total_ded.delete(0, END)
                    txt_net_pay.delete(0, END)

                    txt_basic_pay.config(state=DISABLED)
                    txt_ot_pay.config(state=DISABLED)
                    txt_total_ded.config(state=DISABLED)
                    txt_net_pay.config(state=DISABLED)

                    txt_payslip.delete("1.0", END)

                    return

                def view_payslip():

                    global employee_name, regular_rate, overtime_rate
                    employee_name, regular_rate, overtime_rate = db.fetch_rate(txt_emp_id_p.get())
                    txt_payslip.config(state=NORMAL)
                    txt_payslip.delete("1.0", END)
                    txt_payslip.insert(END, "  Employee ID :\t\t" + txt_emp_id_p.get() + "\n\n")
                    txt_payslip.insert(END, "  Employee Name :\t\t" + employee_name + "\n\n")
                    txt_payslip.insert(END, "  Hours Worked :\t\t" + txt_hours_worked.get() + " hours\n\n")
                    txt_payslip.insert(END, "  Rate per hour :\t\t" + str(regular_rate) + "\n\n")
                    txt_payslip.insert(END, "  Basic Pay :\t\t" + txt_basic_pay.get() + "\n\n")
                    txt_payslip.insert(END, "  Overtime Pay :\t\t" + txt_ot_pay.get() + "\n\n")
                    txt_payslip.insert(END, "  SSS Premium :\t\t" + txt_sss.get() + "\n\n")
                    txt_payslip.insert(END, "  HDMF Premium :\t\t" + txt_hdmf.get() + "\n\n")
                    txt_payslip.insert(END, "  PHILHEALTH Premium :\t\t" + txt_philhealth.get() + "\n\n")
                    txt_payslip.insert(END, "  TAX :\t" + txt_wtax.get() + "\n\n")
                    txt_payslip.insert(END, "  Net Pay :\t" + txt_net_pay.get() + "\n\n")

                def back_payroll_menu(lbl_enter_ref_num, txt_enter_ref_num, btn_enter_ref_num, btn_compute,
                                      btn_submit_payroll, btn_clear_payroll, btn_payslip, btn_back_payroll):
                    lbl_enter_ref_num.place_forget()
                    txt_enter_ref_num.place_forget()
                    btn_enter_ref_num.place_forget()

                    btn_log_out.place(x=10, y=600)
                    txt_ref_num.config(state=NORMAL)
                    txt_date.config(state=NORMAL)
                    txt_emp_id_p.config(state=NORMAL)
                    txt_hours_worked.config(state=NORMAL)
                    txt_sss.config(state=NORMAL)
                    txt_hdmf.config(state=NORMAL)
                    txt_philhealth.config(state=NORMAL)
                    txt_wtax.config(state=NORMAL)
                    txt_basic_pay.config(state=NORMAL)
                    txt_ot_pay.config(state=NORMAL)
                    txt_total_ded.config(state=NORMAL)
                    txt_net_pay.config(state=NORMAL)
                    txt_payslip.config(state=NORMAL)

                    clear_data_payroll()

                    txt_ref_num.config(state=DISABLED)
                    txt_basic_pay.config(state=DISABLED)
                    txt_ot_pay.config(state=DISABLED)
                    txt_total_ded.config(state=DISABLED)
                    txt_net_pay.config(state=DISABLED)

                    lbl_ref_num.place_forget()
                    txt_ref_num.place_forget()
                    lbl_date.place_forget()
                    txt_date.place_forget()
                    lbl_emp_id_p.place_forget()
                    txt_emp_id_p.place_forget()
                    lbl_hours_worked.place_forget()
                    txt_hours_worked.place_forget()
                    lbl_sss.place_forget()
                    txt_sss.place_forget()
                    lbl_hdmf.place_forget()
                    txt_hdmf.place_forget()
                    lbl_philhealth.place_forget()
                    txt_philhealth.place_forget()
                    lbl_wtax.place_forget()
                    txt_wtax.place_forget()
                    lbl_basic_pay.place_forget()
                    txt_basic_pay.place_forget()
                    lbl_ot_pay.place_forget()
                    txt_ot_pay.place_forget()
                    lbl_total_ded.place_forget()
                    txt_total_ded.place_forget()
                    lbl_net_pay.place_forget()
                    txt_net_pay.place_forget()

                    payslip.place_forget()
                    txt_payslip.place_forget()

                    btn_compute.place_forget()
                    btn_submit_payroll.place_forget()
                    btn_clear_payroll.place_forget()
                    btn_payslip.place_forget()
                    btn_back_payroll.place_forget()

                    btn_add_payroll.place(x=690, y=220)
                    btn_edit_payroll.place(x=690, y=350)
                    btn_delete_payroll.place(x=690, y=480)

                def add_payroll(btn_add_payroll, btn_edit_payroll, btn_delete_payroll):
                    btn_add_payroll.place_forget()
                    btn_edit_payroll.place_forget()
                    btn_delete_payroll.place_forget()
                    btn_log_out.place_forget()

                    global insert_reference_no
                    insert_reference_no = db.next_reference_no()
                    txt_ref_num.config(state=NORMAL)
                    txt_ref_num.delete(0, END)
                    txt_ref_num.insert(0, insert_reference_no)
                    txt_ref_num.config(state=DISABLED)

                    lbl_ref_num.place(x=70, y=220)
                    txt_ref_num.place(x=270, y=220)
                    lbl_date.place(x=70, y=260)
                    txt_date.place(x=270, y=260, width=245)
                    lbl_emp_id_p.place(x=70, y=300)
                    txt_emp_id_p.place(x=270, y=300)
                    lbl_hours_worked.place(x=70, y=340)
                    txt_hours_worked.place(x=270, y=340)
                    lbl_sss.place(x=70, y=380)
                    txt_sss.place(x=270, y=380)
                    lbl_hdmf.place(x=70, y=420)
                    txt_hdmf.place(x=270, y=420)
                    lbl_philhealth.place(x=70, y=460)
                    txt_philhealth.place(x=270, y=460)
                    lbl_wtax.place(x=70, y=500)
                    txt_wtax.place(x=270, y=500)
                    lbl_basic_pay.place(x=560, y=220)
                    txt_basic_pay.place(x=760, y=220)
                    txt_basic_pay.config(state=DISABLED)
                    lbl_ot_pay.place(x=560, y=260)
                    txt_ot_pay.place(x=760, y=260)
                    txt_ot_pay.config(state=DISABLED)
                    lbl_total_ded.place(x=560, y=300)
                    txt_total_ded.place(x=760, y=300)
                    txt_total_ded.config(state=DISABLED)
                    lbl_net_pay.place(x=560, y=340)
                    txt_net_pay.place(x=760, y=340)
                    txt_net_pay.config(state=DISABLED)

                    payslip.place(x=1245, y=185)
                    txt_payslip.place(x=1050, y=220)
                    txt_payslip.config(state=DISABLED)

                    btn_back_payroll.place(x=30, y=580)
                    btn_compute.place(x=230, y=580)
                    btn_submit_payroll.place(x=430, y=580)
                    btn_submit_payroll.config(text='Add to Payroll')
                    btn_submit_payroll.config(command=add_payroll_database)
                    btn_submit_payroll.config(state=DISABLED)
                    btn_clear_payroll.place(x=630, y=580)
                    btn_payslip.place(x=830, y=580)
                    btn_payslip.config(state=DISABLED)

                def add_payroll_database():

                    if txt_emp_id_p.get() == "" or txt_hours_worked.get() == "" \
                            or txt_sss.get() == "" or txt_hdmf.get() == "" or txt_philhealth.get() == "" \
                            or txt_wtax.get() == "":
                        messagebox.showerror("Error in Input", "Please Fill the Details")
                        return

                    db.insert_payroll(txt_ref_num.get(), txt_date.get(), txt_emp_id_p.get(), txt_hours_worked.get(),
                                      txt_sss.get(), txt_hdmf.get(), txt_philhealth.get(), txt_wtax.get(),
                                      txt_basic_pay.get(), txt_ot_pay.get(), txt_net_pay.get())

                    messagebox.showinfo("Success", "Record Inserted")

                    display_all()

                    insert_reference_no = db.next_reference_no()
                    txt_ref_num.config(state=NORMAL)
                    txt_ref_num.delete(0, END)
                    txt_ref_num.insert(0, insert_reference_no)
                    txt_ref_num.config(state=DISABLED)

                    clear_data_payroll()
                    txt_payslip.config(state=DISABLED)
                    btn_payslip.config(state=DISABLED)
                    btn_submit_payroll.config(state=DISABLED)

                def edit_ref_no(btn_add_payroll, btn_edit_payroll, btn_delete_payroll):
                    btn_add_payroll.place_forget()
                    btn_edit_payroll.place_forget()
                    btn_delete_payroll.place_forget()

                    lbl_enter_ref_num.place(x=610, y=280)
                    txt_enter_ref_num.place(x=610, y=320)
                    btn_enter_ref_num.place(x=700, y=400)
                    btn_enter_ref_num.config(command=lambda: update_payroll(lbl_enter_ref_num, txt_enter_ref_num,
                                                                            btn_enter_ref_num))
                    btn_back_payroll.place(x=15, y=600)

                def update_payroll(lbl_enter_ref_num, txt_enter_ref_num, btn_enter_ref_num):
                    if txt_enter_ref_num.get() == "":
                        messagebox.showerror("Error in Input", "Please enter Reference Number")
                        return

                    if (int(txt_enter_ref_num.get()),) not in db.validate_reference_no():
                        messagebox.showerror("Error in Input", "This reference number does not belong to the company")
                        return

                    lbl_enter_ref_num.place_forget()
                    txt_enter_ref_num.place_forget()
                    btn_enter_ref_num.place_forget()

                    (reference_no, date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax, basic_pay,
                     overtime_pay, net_pay) = db.fetch_ref_no(txt_enter_ref_num.get())

                    total_deductions = sss + hdmf + philhealth + withholding_tax

                    lbl_ref_num.place(x=70, y=220)
                    txt_ref_num.place(x=270, y=220)
                    txt_ref_num.config(state=NORMAL)
                    txt_ref_num.delete(0, END)
                    txt_ref_num.insert(0, reference_no)
                    txt_ref_num.config(state=DISABLED)

                    lbl_date.place(x=70, y=260)
                    txt_date.place(x=270, y=260, width=245)
                    txt_date.delete(0, END)
                    txt_date.insert(0, date)

                    lbl_emp_id_p.place(x=70, y=300)
                    txt_emp_id_p.place(x=270, y=300)
                    txt_emp_id_p.config(state=NORMAL)
                    txt_emp_id_p.delete(0, END)
                    txt_emp_id_p.insert(0, employee_id)
                    txt_emp_id_p.config(state=DISABLED)

                    lbl_hours_worked.place(x=70, y=340)
                    txt_hours_worked.place(x=270, y=340)
                    txt_hours_worked.delete(0, END)
                    txt_hours_worked.insert(0, hours_worked)

                    lbl_sss.place(x=70, y=380)
                    txt_sss.place(x=270, y=380)
                    txt_sss.delete(0, END)
                    txt_sss.insert(0, Decimal(sss).quantize(TWOPLACES))

                    lbl_hdmf.place(x=70, y=420)
                    txt_hdmf.place(x=270, y=420)
                    txt_hdmf.delete(0, END)
                    txt_hdmf.insert(0, Decimal(hdmf).quantize(TWOPLACES))

                    lbl_philhealth.place(x=70, y=460)
                    txt_philhealth.place(x=270, y=460)
                    txt_philhealth.delete(0, END)
                    txt_philhealth.insert(0, Decimal(philhealth).quantize(TWOPLACES))

                    lbl_wtax.place(x=70, y=500)
                    txt_wtax.place(x=270, y=500)
                    txt_wtax.delete(0, END)
                    txt_wtax.insert(0, Decimal(withholding_tax).quantize(TWOPLACES))

                    lbl_basic_pay.place(x=560, y=220)
                    txt_basic_pay.place(x=760, y=220)
                    txt_basic_pay.config(state=NORMAL)
                    txt_basic_pay.delete(0, END)
                    txt_basic_pay.insert(0, Decimal(basic_pay).quantize(TWOPLACES))
                    txt_basic_pay.config(state=DISABLED)

                    lbl_ot_pay.place(x=560, y=260)
                    txt_ot_pay.place(x=760, y=260)
                    txt_ot_pay.config(state=NORMAL)
                    txt_ot_pay.delete(0, END)
                    txt_ot_pay.insert(0, Decimal(overtime_pay).quantize(TWOPLACES))
                    txt_ot_pay.config(state=DISABLED)

                    lbl_total_ded.place(x=560, y=300)
                    txt_total_ded.place(x=760, y=300)
                    txt_total_ded.config(state=NORMAL)
                    txt_total_ded.delete(0, END)
                    txt_total_ded.insert(0, Decimal(total_deductions).quantize(TWOPLACES))
                    txt_total_ded.config(state=DISABLED)

                    lbl_net_pay.place(x=560, y=340)
                    txt_net_pay.place(x=760, y=340)
                    txt_net_pay.config(state=NORMAL)
                    txt_net_pay.delete(0, END)
                    txt_net_pay.insert(0, Decimal(net_pay).quantize(TWOPLACES))
                    txt_net_pay.config(state=DISABLED)

                    payslip.place(x=1245, y=185)
                    txt_payslip.place(x=1050, y=220)

                    btn_back_payroll.place(x=30, y=580)
                    btn_compute.place(x=230, y=580)
                    btn_submit_payroll.place(x=430, y=580)
                    btn_submit_payroll.config(text='Update Payroll')
                    btn_submit_payroll.config(command=update_payroll_database)
                    btn_submit_payroll.config(state=DISABLED)

                    btn_clear_payroll.place(x=630, y=580)
                    btn_payslip.place(x=830, y=580)

                def update_payroll_database():
                    if txt_emp_id_p.get() == "" or txt_hours_worked.get() == "" \
                            or txt_sss.get() == "" or txt_hdmf.get() == "" or txt_philhealth.get() == "" \
                            or txt_wtax.get() == "":
                        messagebox.showerror("Error in Input", "Please Fill the Details")
                        return

                    db.update_payroll(txt_ref_num.get(), txt_date.get(), txt_emp_id_p.get(), txt_hours_worked.get(),
                                      txt_sss.get(), txt_hdmf.get(), txt_philhealth.get(), txt_wtax.get(),
                                      txt_basic_pay.get(), txt_ot_pay.get(), txt_net_pay.get())

                    messagebox.showinfo("Success", "Record Updated")

                    display_all()

                def delete_ref_no(btn_add_payroll, btn_edit_payroll, btn_delete_payroll):
                    btn_add_payroll.place_forget()
                    btn_edit_payroll.place_forget()
                    btn_delete_payroll.place_forget()

                    lbl_enter_ref_num.place(x=610, y=280)
                    txt_enter_ref_num.place(x=610, y=320)

                    btn_enter_ref_num.config(command=lambda: delete_payroll(lbl_enter_ref_num, txt_enter_ref_num,
                                                                            btn_enter_ref_num))
                    btn_enter_ref_num.place(x=700, y=400)
                    btn_back_payroll.place(x=15, y=600)

                def delete_payroll(lbl_enter_ref_num, txt_enter_ref_num, btn_enter_ref_num):
                    if txt_enter_ref_num.get() == "":
                        messagebox.showerror("Error in Input", "Please enter Reference Number")
                        return

                    if (int(txt_enter_ref_num.get()),) not in db.validate_reference_no():
                        messagebox.showerror("Error in Input", "This reference number does not belong to the company")
                        return

                    lbl_enter_ref_num.place_forget()
                    txt_enter_ref_num.place_forget()
                    btn_enter_ref_num.place_forget()

                    (reference_no, date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax, basic_pay,
                     overtime_pay, net_pay) = db.fetch_ref_no(txt_enter_ref_num.get())

                    total_deductions = sss + hdmf + philhealth + withholding_tax

                    lbl_ref_num.place(x=70, y=220)
                    txt_ref_num.place(x=270, y=220)
                    txt_ref_num.config(state=NORMAL)
                    txt_ref_num.delete(0, END)
                    txt_ref_num.insert(0, reference_no)
                    txt_ref_num.config(state=DISABLED)

                    lbl_date.place(x=70, y=260)
                    txt_date.place(x=270, y=260, width=245)
                    txt_date.delete(0, END)
                    txt_date.insert(0, date)
                    txt_date.config(state=DISABLED)

                    lbl_emp_id_p.place(x=70, y=300)
                    txt_emp_id_p.place(x=270, y=300)
                    txt_emp_id_p.config(state=NORMAL)
                    txt_emp_id_p.delete(0, END)
                    txt_emp_id_p.insert(0, employee_id)
                    txt_emp_id_p.config(state=DISABLED)

                    lbl_hours_worked.place(x=70, y=340)
                    txt_hours_worked.place(x=270, y=340)
                    txt_hours_worked.delete(0, END)
                    txt_hours_worked.insert(0, hours_worked)
                    txt_hours_worked.config(state=DISABLED)

                    lbl_sss.place(x=70, y=380)
                    txt_sss.place(x=270, y=380)
                    txt_sss.delete(0, END)
                    txt_sss.insert(0, Decimal(sss).quantize(TWOPLACES))
                    txt_sss.config(state=DISABLED)

                    lbl_hdmf.place(x=70, y=420)
                    txt_hdmf.place(x=270, y=420)
                    txt_hdmf.delete(0, END)
                    txt_hdmf.insert(0, Decimal(hdmf).quantize(TWOPLACES))
                    txt_hdmf.config(state=DISABLED)

                    lbl_philhealth.place(x=70, y=460)
                    txt_philhealth.place(x=270, y=460)
                    txt_philhealth.delete(0, END)
                    txt_philhealth.insert(0, Decimal(philhealth).quantize(TWOPLACES))
                    txt_philhealth.config(state=DISABLED)

                    lbl_wtax.place(x=70, y=500)
                    txt_wtax.place(x=270, y=500)
                    txt_wtax.delete(0, END)
                    txt_wtax.insert(0, Decimal(withholding_tax).quantize(TWOPLACES))
                    txt_wtax.config(state=DISABLED)

                    lbl_basic_pay.place(x=560, y=220)
                    txt_basic_pay.place(x=760, y=220)
                    txt_basic_pay.config(state=NORMAL)
                    txt_basic_pay.delete(0, END)
                    txt_basic_pay.insert(0, Decimal(basic_pay).quantize(TWOPLACES))
                    txt_basic_pay.config(state=DISABLED)

                    lbl_ot_pay.place(x=560, y=260)
                    txt_ot_pay.place(x=760, y=260)
                    txt_ot_pay.config(state=NORMAL)
                    txt_ot_pay.delete(0, END)
                    txt_ot_pay.insert(0, Decimal(overtime_pay).quantize(TWOPLACES))
                    txt_ot_pay.config(state=DISABLED)

                    lbl_total_ded.place(x=560, y=300)
                    txt_total_ded.place(x=760, y=300)
                    txt_total_ded.config(state=NORMAL)
                    txt_total_ded.delete(0, END)
                    txt_total_ded.insert(0, Decimal(total_deductions).quantize(TWOPLACES))
                    txt_total_ded.config(state=DISABLED)

                    lbl_net_pay.place(x=560, y=340)
                    txt_net_pay.place(x=760, y=340)
                    txt_net_pay.config(state=NORMAL)
                    txt_net_pay.delete(0, END)
                    txt_net_pay.insert(0, Decimal(net_pay).quantize(TWOPLACES))
                    txt_net_pay.config(state=DISABLED)

                    payslip.place(x=1245, y=185)
                    txt_payslip.place(x=1050, y=220)
                    txt_payslip.delete("1.0", END)

                    btn_back_payroll.place(x=30, y=580)
                    btn_submit_payroll.place(x=430, y=580)
                    btn_submit_payroll.config(text='Delete Payroll')
                    btn_submit_payroll.config(command=delete_payroll_database)
                    btn_submit_payroll.config(state=NORMAL)

                    btn_payslip.place(x=830, y=580)
                    btn_payslip.config(state=NORMAL)

                def delete_payroll_database():
                    db.delete_payroll(txt_ref_num.get())
                    txt_ref_num.config(state=NORMAL)
                    txt_date.config(state=NORMAL)
                    txt_emp_id_p.config(state=NORMAL)
                    txt_hours_worked.config(state=NORMAL)
                    txt_sss.config(state=NORMAL)
                    txt_hdmf.config(state=NORMAL)
                    txt_philhealth.config(state=NORMAL)
                    txt_wtax.config(state=NORMAL)
                    txt_basic_pay.config(state=NORMAL)
                    txt_ot_pay.config(state=NORMAL)
                    txt_total_ded.config(state=NORMAL)
                    txt_net_pay.config(state=NORMAL)

                    clear_data_payroll()

                    txt_ref_num.config(state=DISABLED)
                    txt_date.config(state=DISABLED)
                    txt_emp_id_p.config(state=DISABLED)
                    txt_hours_worked.config(state=DISABLED)
                    txt_sss.config(state=DISABLED)
                    txt_hdmf.config(state=DISABLED)
                    txt_philhealth.config(state=DISABLED)
                    txt_wtax.config(state=DISABLED)
                    txt_basic_pay.config(state=DISABLED)
                    txt_ot_pay.config(state=DISABLED)
                    txt_total_ded.config(state=DISABLED)
                    txt_net_pay.config(state=DISABLED)
                    txt_payslip.config(state=DISABLED)

                    messagebox.showinfo("Success", "Record Deleted")
                    display_all()

                # ==================================== BUTTONS =========================================================
                lbl_enter_ref_num = Label(self.tab2, text="Enter Reference Number", font=("Consolas", 17),
                                          bg="#f1dcfa", fg="#7b0cab")

                txt_enter_ref_num = Entry(self.tab2, font=("Consolas", 17), width=30, fg="black")

                btn_enter_ref_num = Button(self.tab2, text="Submit", width=20, height=2,
                                           font=("Consolas", 14, "bold"), fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)

                btn_compute = Button(self.tab2, text='Compute', command=compute_salary, padx=16, pady=16,
                                     font=('Consolas', 14, 'bold'), width=15, height=1, fg="#f0cb7d",
                                     bg="#7b0cab", relief=GROOVE)

                btn_submit_payroll = Button(self.tab2, padx=16, pady=16, font=('Consolas', 14, 'bold'), width=15,
                                            height=1, fg="#f0cb7d", bg="#7b0cab", relief=GROOVE)

                btn_clear_payroll = Button(self.tab2, text='Clear Details', command=clear_data_payroll, padx=16,
                                           pady=16, font=('Consolas', 14, 'bold'), width=15, height=1, fg="#f0cb7d",
                                           bg="#7b0cab", relief=GROOVE)

                btn_payslip = Button(self.tab2, text='View Payslip', command=view_payslip, padx=16, pady=16,
                                     font=('Consolas', 14, 'bold'), width=15, height=1, fg="#f0cb7d", bg="#7b0cab",
                                     relief=GROOVE)

                btn_back_payroll = Button(self.tab2, text='Back', padx=16, pady=16,
                                          command=lambda: back_payroll_menu(lbl_enter_ref_num, txt_enter_ref_num,
                                                                            btn_enter_ref_num, btn_compute,
                                                                            btn_submit_payroll, btn_clear_payroll,
                                                                            btn_payslip, btn_back_payroll),
                                          font=('Consolas', 14, 'bold'), width=15, height=1, fg="#f0cb7d", bg="#7b0cab",
                                          relief=GROOVE)

                # ============================================== TAB 2 - PAYROLL MENU ==================================

                btn_add_payroll = Button(self.tab2, text="Add Payroll Item",
                                         command=lambda: add_payroll(btn_add_payroll, btn_edit_payroll,
                                                                     btn_delete_payroll),
                                         width=25, height=3, font=("Consolas", 14, "bold"), fg="#f0cb7d", bg="#7b0cab",
                                         relief=GROOVE)
                btn_add_payroll.place(x=690, y=220)

                btn_edit_payroll = Button(self.tab2, text="Edit Payroll Item",
                                          command=lambda: edit_ref_no(btn_add_payroll, btn_edit_payroll,
                                                                      btn_delete_payroll),
                                          width=25, height=3, font=("Consolas", 14, "bold"), fg="#f0cb7d", bg="#7b0cab",
                                          relief=GROOVE)
                btn_edit_payroll.place(x=690, y=350)

                btn_delete_payroll = Button(self.tab2, text="Delete Payroll Item",
                                            command=lambda: delete_ref_no(btn_add_payroll, btn_edit_payroll,
                                                                          btn_delete_payroll),
                                            width=25, height=3, font=("Consolas", 14, "bold"), fg="#f0cb7d",
                                            bg="#7b0cab", relief=GROOVE)
                btn_delete_payroll.place(x=690, y=480)

                # ====================================== FUNCTIONS =====================================================

                def display_all():
                    tv.delete(*tv.get_children())
                    for row in db.fetch_record(company_id):
                        tv.insert("", END, values=row)

                def search_name():
                    global name_entered, search, flag_name
                    if flag_name:
                        search = Toplevel(log)
                        search.title("Filter Records by Name")
                        search.geometry("400x200")
                        search.config(background="#f1dcfa")
                        flag_name = 0

                        # Create label frame
                        search_frame = LabelFrame(search, text="Enter Employee Name", font=('Consolas', 14),
                                                  fg="#7b0cab", bg="#f1dcfa")
                        search_frame.pack(padx=10, pady=10)

                        # Add entry box
                        name_entered = Entry(search_frame, font=('Consolas', 14), width=24)
                        name_entered.pack(pady=20, padx=20)

                        # Add button
                        search_button = Button(search, text="Search Name", cursor="hand2",
                                               font=("Consolas", 12, "bold"), fg="#f0cb7d", bg="#7b0cab", relief=GROOVE,
                                               command=filter_name, width=15, height=1)
                        search_button.pack(padx=20, pady=20)

                        search.protocol('WM_DELETE_WINDOW', close_name)

                def close_name():
                    global flag_name
                    flag_name = 1
                    search.destroy()

                def filter_name():
                    input_name = name_entered.get()
                    # close the search box
                    global flag_name
                    flag_name = 1
                    search.destroy()

                    # Clear the Treeview
                    tv.delete(*tv.get_children())
                    for row in db.fetch_name(company_id, input_name):
                        tv.insert("", END, values=row)

                def search_date():
                    global date_entered, search, flag_date
                    if flag_date:
                        search = Toplevel(log)
                        search.title("Filter Records by Date")
                        search.geometry("400x200")
                        search.config(background="#f1dcfa")
                        flag_date = 0

                        # Create label frame
                        search_frame = LabelFrame(search, text="Enter Date", font=('Consolas', 14),
                                                  fg="#7b0cab", bg="#f1dcfa")
                        search_frame.pack(padx=10, pady=10)

                        # Add entry box
                        date_entered = Entry(search_frame, font=('Consolas', 14), width=24)
                        date_entered.pack(pady=20, padx=20)

                        # Add button
                        search_button = Button(search, text="Search Date", cursor="hand2",
                                               font=("Consolas", 12, "bold"), fg="#f0cb7d", bg="#7b0cab", relief=GROOVE,
                                               command=filter_date, width=15, height=1)
                        search_button.pack(padx=20, pady=20)

                        search.protocol('WM_DELETE_WINDOW', close_date)

                def close_date():
                    global flag_date
                    flag_date = 1
                    search.destroy()

                def filter_date():
                    input_date = date_entered.get()
                    # close the search box
                    global flag_date
                    flag_date = 1
                    search.destroy()

                    # Clear the Treeview
                    tv.delete(*tv.get_children())
                    for row in db.fetch_date(company_id, input_date):
                        tv.insert("", END, values=row)

                # ========================================= TAB 3 - VIEW RECORDS ======================================
                global flag_date, flag_name
                flag_date = 1
                flag_name = 1

                lbl_payroll_main = Label(self.tab3, font=('Tw Cen MT Condensed Extra Bold', 47),
                                         text=" PAYROLL MANAGEMENT SYSTEM", fg="#f0cb7d", bg="#7b0cab", compound=CENTER,
                                         height=2, width=55)
                lbl_payroll_main.place(x=0, y=0)

                lbl_records_heading = Label(self.tab3, font=('Tw Cen MT Condensed Extra Bold', 25), text="VIEW RECORDS",
                                            fg="white", bg="#7b0cab", compound=LEFT, width=25, height=1)
                lbl_records_heading.place(x=70, y=150)

                lbl_payroll = Label(self.tab3, font=('Consolas', 20, 'bold'), text="P A Y R O L L", fg="#7b0cab",
                                    bg="#f1dcfa", width=19, height=1)
                lbl_payroll.place(x=680, y=168)

                lbl_company_name = Label(self.tab3, font=('Consolas', 14, 'bold'), text="Company Name", fg="white",
                                         bg="#7b0cab", width=26, height=6)
                lbl_company_name.place(x=1260, y=94)

                txt_company_name = Entry(self.tab3, font=('Consolas', 14, 'bold'), width=24, justify='center',
                                         bg='#d29cff', fg="black")
                txt_company_name.place(x=1270, y=180)
                txt_company_name.insert(0, company_name)
                txt_company_name.config(state=DISABLED)

                btn_search_name = Button(self.tab3, text="Search Name", command=search_name, width=15, height=2,
                                         font=("Consolas", 12, "bold"), fg="#f0cb7d", bg="#7b0cab", relief=RAISED)
                btn_search_name.place(x=500, y=605)

                btn_search_date = Button(self.tab3, text="Search Date", width=15, height=2, command=search_date,
                                         font=("Consolas", 12, "bold"), fg="#f0cb7d", bg="#7b0cab", relief=RAISED)
                btn_search_date.place(x=960, y=605)

                btn_display_all = Button(self.tab3, text="Display All", command=display_all, cursor="hand2",
                                         font=("Consolas", 12, "bold"), fg="#f0cb7d", bg="#7b0cab", width=24, height=2,
                                         relief=RAISED)
                btn_display_all.place(x=690, y=605)

                # ====================================== TABLE =========================================================
                tree_frame = Frame(self.tab3, bg="#ecf0f1")
                tree_frame.place(x=20, y=220, width=1540, height=370)
                style = ttk.Style()
                style.configure("mystyle.Treeview", font=('Consolas', 13),
                                rowheight=50, foreground="#7b0cab")  # Modify the font of the body
                style.configure("mystyle.Treeview.Heading", font=('Consolas', 13, 'bold'))
                scroll = tkinter.Scrollbar(tree_frame, orient=VERTICAL)
                tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview",
                                  yscrollcommand=scroll.set)

                scroll.pack(side=RIGHT, fill=Y)
                scroll.config(command=tv.yview)

                tv.heading("1", text="Reference Number")
                tv.column("1", width=15)
                tv.heading("2", text="Date")
                tv.column("2", width=3)
                tv.heading("3", text="Employee ID")
                tv.column("3", width=10)
                tv.heading("4", text="Employee Name")
                tv.heading("5", text="Basic Pay")
                tv.column("5", width=5)
                tv.heading("6", text="Overtime Pay")
                tv.column("6", width=1)
                tv.heading("7", text="Total Deductions")
                tv.column("7", width=1)
                tv.heading("8", text="Net Pay")
                tv.column("8", width=1)
                tv['show'] = 'headings'
                tv.pack(fill=BOTH, expand=1)
                display_all()

        app = App()
        app.mainloop()

    else:
        messagebox.showwarning("Login failed", "Please try again.")


def cancel_login():
    log.destroy()


login_button = Button(text="Login", font=("Consolas", 14, 'bold'), fg="#f0cb7d", bg="#7b0cab", relief=GROOVE,
                      command=try_login, padx=28, pady=11)
login_button.place(x=670, y=500)

cancel_button = Button(text="Cancel", font=("Consolas", 14, 'bold'), fg="#f0cb7d", bg="#7b0cab", relief=GROOVE,
                       command=cancel_login, padx=25, pady=11)
cancel_button.place(x=840, y=500)

log.mainloop()
