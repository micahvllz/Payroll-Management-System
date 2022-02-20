import sqlite3
import functools


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    # Check the User table from DB
    def credential(self, username, password):
        self.cur.execute("select company_id from user where username = ? and password = ?", (username, password))
        global company, company_id
        company = self.cur.fetchone()
        if company:
            company_id = functools.reduce(lambda sub, elem: sub * 10 + elem, company)
            return company_id
        else:
            return None

    def company_name(self, company_id):
        self.cur.execute("select company_name from company where company_id = ?", (company_id,))
        company_name = self.cur.fetchone()
        return company_name

    def next_emp_id(self):
        self.cur.execute("select employee_id from employee where company_id = ? order by employee_id desc limit 1",
                         company)
        emp_id = functools.reduce(lambda sub, elem: sub * 10 + elem, self.cur.fetchone())
        return emp_id + 1

    def validate_emp_id(self):
        self.cur.execute("select employee_id from employee where company_id = ?", company)
        employee_ids = self.cur.fetchall()
        return employee_ids

    # Insert Function
    def insert_emp(self, employee_id, company_id, first_name, middle_name, last_name, gender, department_id, position,
                   regular_rate, overtime_rate, phone_no, email, house_no, street_name, subdivision, barangay, city,
                   zip_code):
        self.cur.execute("insert into employee values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (employee_id, company_id, first_name, middle_name, last_name, gender, department_id,
                          position, regular_rate, overtime_rate, phone_no, email, house_no, street_name,
                          subdivision, barangay, city, zip_code))
        self.con.commit()

    # Fetch All Data of the Employee
    def fetch_emp(self, employee_id):
        self.cur.execute("select * from employee where employee_id =?", (employee_id,))
        data = self.cur.fetchone()
        return data

    # Update a Record in DB
    def update_emp(self, employee_id, company_id, first_name, middle_name, last_name, gender, department_id, position,
                   regular_rate, overtime_rate, phone_no, email, house_no, street_name, subdivision, barangay, city,
                   zip_code):
        self.cur.execute(
            "update employee set company_id=?, first_name=?, middle_name=?, last_name=?, gender=?,"
            "department_id=?, position=?, regular_rate=?, overtime_rate=?, phone_no=?, email=?, house_no=?,"
            "street_name=?, subdivision=?, barangay=?, city=?, zip_code=? where employee_id=?",
            (company_id, first_name, middle_name, last_name, gender, department_id, position, regular_rate,
             overtime_rate, phone_no, email, house_no, street_name, subdivision, barangay, city, zip_code, employee_id))
        self.con.commit()

    # Delete a Record in DB
    def remove_emp(self, employee_id):
        self.cur.execute("delete from employee where employee_id=?", (employee_id,))
        self.con.commit()

    def next_reference_no(self):
        self.cur.execute("select reference_no from salary order by reference_no desc limit 1")
        reference_no = functools.reduce(lambda sub, elem: sub * 10 + elem, self.cur.fetchone())
        return reference_no + 1

    def validate_reference_no(self):
        self.cur.execute("select reference_no from salary where employee_id like ?", (str(company_id) + '%%%',))
        reference_nos = self.cur.fetchall()
        return reference_nos

    # Insert Function
    def insert_payroll(self, reference_no, date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax,
                       basic_pay, overtime_pay, net_pay):
        self.cur.execute("insert into salary values (?,?,?,?,?,?,?,?,?,?,?)",
                         (reference_no, date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax,
                          basic_pay, overtime_pay, net_pay))
        self.con.commit()

    # Fetch Data of the Employee
    def fetch_rate(self, employee_id):
        self.cur.execute("select first_name || ' ' || last_name as 'employee_name', "
                         "regular_rate, overtime_rate from employee where employee_id =?", (employee_id,))
        rate = self.cur.fetchone()
        return rate

    # Fetch All Data of the Selected Reference No
    def fetch_ref_no(self, reference_no):
        self.cur.execute("select * from salary where reference_no =?", (reference_no,))
        payroll_data = self.cur.fetchone()
        return payroll_data

    # Update a Record in DB
    def update_payroll(self, reference_no, date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax,
                       basic_pay, overtime_pay, net_pay):
        self.cur.execute(
            "update salary set date=?, employee_id=?, hours_worked=?, sss=?, hdmf=?, philhealth=?, withholding_tax=?,"
            "basic_pay=?, overtime_pay=?, net_pay=? "
            "where reference_no=?", (date, employee_id, hours_worked, sss, hdmf, philhealth, withholding_tax, basic_pay,
                                     overtime_pay, net_pay, reference_no))
        self.con.commit()

    # Delete a Record in DB
    def delete_payroll(self, reference_no):
        self.cur.execute("delete from salary where reference_no=?", (reference_no,))
        self.con.commit()

    # Fetch Payroll Record
    def fetch_record(self, company_id):
        self.cur.execute("select s.reference_no, s.date, s.employee_id,"
                         "e.first_name || ' ' || e.last_name as 'Employee Name', "
                         "s.basic_pay, s.overtime_pay, "
                         "s.sss + hdmf + philhealth + withholding_tax as 'Total Deductions', "
                         "s.net_pay "
                         "from salary as s "
                         "left outer join employee as e "
                         "on s.employee_id = e.employee_id "
                         "where s.employee_id like ? order by date",
                         (str(company_id) + '%%%',))
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Fetch Payroll Record Filtered by Name
    def fetch_name(self, company_id, full_name):
        self.cur.execute("select s.reference_no, s.date, s.employee_id,"
                         "e.first_name || ' ' || e.last_name as 'Employee Name', "
                         "s.basic_pay, s.overtime_pay, "
                         "s.sss + hdmf + philhealth + withholding_tax as 'Total Deductions', "
                         "s.net_pay "
                         "from salary as s "
                         "left outer join employee as e "
                         "on s.employee_id = e.employee_id "
                         "where s.employee_id like ? and e.first_name || ' ' || e.last_name like ?"
                         "order by date",
                         (str(company_id) + '%%%', full_name))
        filtered_name = self.cur.fetchall()
        # print(rows)
        return filtered_name

    # Fetch Payroll Record Filtered by Date
    def fetch_date(self, company_id, date):
        self.cur.execute("select s.reference_no, s.date, s.employee_id,"
                         "e.first_name || ' ' || e.last_name as 'Employee Name', "
                         "s.basic_pay, s.overtime_pay, "
                         "s.sss + hdmf + philhealth + withholding_tax as 'Total Deductions', "
                         "s.net_pay "
                         "from salary as s "
                         "left outer join employee as e "
                         "on s.employee_id = e.employee_id "
                         "where s.employee_id like ? and date like ?"
                         "order by date",
                         (str(company_id) + '%%%', date))
        filtered_date = self.cur.fetchall()
        # print(rows)
        return filtered_date
