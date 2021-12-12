import sqlite3
class Database:
  def __init__(self, db):
    self.conn=sqlite3.connect(db)
    self.cur=self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, name text, email text, phoneNo text)")
    self.cur.execute("CREATE TABLE IF NOT EXISTS document (id INTEGER PRIMARY KEY, customerId text, civilId blob, possesPaper blob, publicLocation blob)")
    self.cur.execute("CREATE TABLE IF NOT EXISTS plan (id INTEGER PRIMARY KEY, employeeId text, customerName text,customerId text, type text, plan blob, created_at timestamp)")
    self.cur.execute("CREATE TABLE IF NOT EXISTS payment (id INTEGER PRIMARY KEY, employeeId text, customerName text, customerId text, type, amount, status BOOLEAN NOT NULL CHECK (status IN (0, 1)),created_at timestamp)")
    self.cur.execute("CREATE TABLE IF NOT EXISTS rukhsah (id INTEGER PRIMARY KEY, employeeId text, customerName text, customerId text, rukhsah blob, status BOOLEAN NOT NULL CHECK (status IN (0, 1)),created_at timestamp)")

    self.cur.execute("CREATE TABLE IF NOT EXISTS appointment (id INTEGER PRIMARY KEY, employeeId text, customerId text, customerName,date string)")
    self.cur.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, type text, status text, employeeId text, customerName text, customerId text, employee_for text, created_at timestamp)")

    self.conn.commit()
  
# -------------Customer-----------------------------
  def insert_customer(self,name, email, phoneNo):
    self.cur.execute("INSERT INTO customer VALUES (NULL,?,?,?)", (name, email, phoneNo))
    self.conn.commit()
  def view_all_customers(self):
    self.cur.execute("SELECT name, email, phoneNo FROM customer")
    rows=self.cur.fetchall()
    return rows
  def view_customer(self, customerId):
    self.cur.execute("SELECT name, email, phoneNo FROM customer WHERE phoneNo=?", (customerId, ))
    rows=self.cur.fetchall()
    
    return rows
  def insert_document(self, customerId, civilId="",possesPaper="", publicLocation=""):
    self.cur.execute("INSERT INTO document VALUES (NULL,?,?,?,?)", (customerId, civilId, possesPaper, publicLocation))
    self.conn.commit()

  def view_document(self, customerId):
    self.cur.execute("SELECT * FROM document WHERE customerId=?", (customerId, ))     
    rows=self.cur.fetchall()
    return rows
  
  
# ----------------------Payments-----------------------------------
  def insert_payment(self, employeeId, customerName, customerId,status, created_at ): 
    self.cur.execute("INSERT INTO payment VALUES (NULL,?,?,?,NULL,NULL,?,?)", (employeeId, customerName, customerId,status, created_at))
    self.conn.commit()

  def update_payment(self, employeeId, customerName, customerId, payment_type, payment_amount, payment_status, created_at):
    self.cur.execute("UPDATE payment SET status=?, type=?, amount=?, created_at=? WHERE customerId=?", (payment_status, payment_type, payment_amount, created_at, customerId))
    self.conn.commit()

  def view_payments(self):
    self.cur.execute("SELECT * FROM payment")
    rows=self.cur.fetchall()
    return rows
  
#-------------Appointments ---------------------------
  def view_all_appointments(self, employeeId):
    self.cur.execute("SELECT  customerId, customerName, date FROM appointment WHERE employeeId=?", (employeeId,))
    rows=self.cur.fetchall()
    return rows
  def view_all_sec_appointments(self):
    self.cur.execute("SELECT  customerId, customerName, date FROM appointment")
    rows=self.cur.fetchall()
    return rows
  def insert_appointment(self,employeeId,customerId, customerName, date):
    self.cur.execute("INSERT INTO appointment VALUES (NULL,?,?,?,?)", (employeeId,customerId, customerName, date))
    self.conn.commit()
  def delete_appointment(self, customerId):
    self.cur.execute("DELETE FROM appointment WHERE customerId=?", (customerId,))
    self.conn.commit()



# ----------------Plan-----------------------------------------
  def insert_plan(self, employeeId, customerName, customerId, type_plan, plan, created_at):
    self.cur.execute("INSERT INTO plan VALUES (NULL,?,?,?,?,?,?)", (employeeId, customerName, customerId, type_plan, plan, created_at))
    self.conn.commit()
  def view_plan(self):
    self.cur.execute("SELECT * FROM plan")     
    rows=self.cur.fetchall()
    return rows
  def view_all_accepted_plans(self, plan_type):
    self.cur.execute("SELECT customerName, customerId, created_at FROM plan WHERE type=?", (plan_type, ))    
    rows=self.cur.fetchall()
    return rows 
  def delete_accepted_plan(self, customerId):
    self.cur.execute("DELETE FROM plan WHERE customerId=? AND type=?", (customerId,'Accepted'))
    self.conn.commit()


#-----------------------Rukhsah-----------------------------
  def insert_rukhsah(self, employeeId, customerName, customerId,status, created_at ): 
    self.cur.execute("INSERT INTO rukhsah VALUES (NULL,?,?,?,NULL,?,?)", (employeeId, customerName, customerId,status, created_at))
    self.conn.commit()
  def update_rukhsah(self, employeeId, customerName, customerId, rukhsah, rukhsah_status, created_at):
    self.cur.execute("UPDATE rukhsah SET status=?, rukhsah=?, created_at=? WHERE customerId=?", (rukhsah_status, rukhsah, created_at, customerId))
    self.conn.commit()
  def view_rukhsahs(self):
    self.cur.execute("SELECT * FROM rukhsah")
    rows=self.cur.fetchall()
    return rows

#-----------------------Task-----------------------------
  def insert_task(self, task_type, task_status, employeeId, customerName, customerId,employee_for, created_at ): 
    self.cur.execute("INSERT INTO task VALUES (NULL,?,?,?,?,?,?,?)", (task_type, task_status, employeeId, customerName, customerId,employee_for, created_at))
    self.conn.commit()
  def update_task(self, task_type, task_status, employeeId, customerName, customerId,employee_for, created_at ): 
    self.cur.execute("UPDATE task SET type=?, status=?, employeeId=?, employee_for=?, created_at=? WHERE customerId=?", (task_type, task_status, created_at, customerId))
    self.conn.commit()

  def view_tasks(self, employeeId): 
    self.cur.execute("SELECT type, customerName, customerId, employee_for, created_at FROM task WHERE status=? AND employee_for=?", ('Not Completed', employeeId ))
    rows=self.cur.fetchall()
    return rows
  def delete_task(self,customerId):
    self.cur.execute("DELETE FROM task WHERE customerId=?", (customerId,))
    self.conn.commit()
  
  def __del__(self):
        self.conn.close()




 
  
    

