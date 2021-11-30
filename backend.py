import sqlite3
class Database:
  def __init__(self, db):
    self.conn=sqlite3.connect(db)
    self.cur=self.conn.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, firstName text, lastName text, date text, civilId integer)")
    self.conn.commit()
  def insert(self,firstName, lastName, date, civilId):
    self.cur.execute("INSERT INTO customer VALUES (NULL, ?,?,?,?)", (firstName, lastName, date, civilId))
    self.conn.commit()
  def view(self):
    self.cur.execute("SELECT * FROM customer")
    rows=self.cur.fetchall()
    return rows
  def search(self,firstName="", lastName="", date="", civilId=""):
    self.cur.execute("SELECT * FROM customer WHERE firstName=? OR  lastName=? OR date=? OR civilId=?", (firstName, lastName, date, civilId))
    rows=self.cur.fetchall()
    return rows
  def delete(self,id):
    self.cur.execute("DELETE FROM customer WHERE id=?", (id,))
    self.conn.commit()

  def update(self,id, firstName, lastName, date, civilId):
    self.cur.execute("UPDATE customer SET firstName=?,lastName=?, date=?, civilId=? WHERE id=?", (firstName,lastName, date, civilId, id))
    self.conn.commit()
  def __del__(self):
        self.conn.close()

  
  
  
   
  
  
    

# def connect():
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("CREATE TABLE IF NOT EXISTS customer (id INTEGER PRIMARY KEY, firstName text, lastName text, date text, civilId integer)")
#   conn.commit()
#   conn.close()

# def insert(firstName, lastName, date, civilId):
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("INSERT INTO customer VALUES (NULL, ?,?,?,?)", (firstName, lastName, date, civilId))

#   conn.commit()
#   conn.close()

# def view():
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("SELECT * FROM customer")
#   rows=cur.fetchall()
#   conn.close()
#   return rows

# def search(firstName="", lastName="", date="", civilId=""):
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("SELECT * FROM customer WHERE firstName=? OR  lastName=? OR date=? OR civilId=?", (firstName, lastName, date, civilId))
#   rows=cur.fetchall()
#   conn.close()
#   return rows

# def delete(id):
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("DELETE FROM customer WHERE id=?", (id,))

#   conn.commit()
#   conn.close()

# def update(id, firstName, lastName, date, civilId):
#   conn=sqlite3.connect("customers.db")
#   cur=conn.cursor()
#   cur.execute("UPDATE customer SET firstName=?,lastName=?, date=?, civilId=? WHERE id=?", (firstName,lastName, date, civilId, id))

#   conn.commit()
#   conn.close()



# connect()
# insert("Bilal","EizAldeen","6/11/2021",219873283264)
# delete(3)
# update(4, "The moon", "Eiz", "88323", 9838232323)
# print(view())
# print(search(firstName="Bilal"))