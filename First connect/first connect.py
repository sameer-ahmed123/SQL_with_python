import sqlite3


connect = sqlite3.connect("First connect/data.db")



cursor = connect.cursor()

#this checks if the table already exists if so then deletes data in  the table 'Users' then adds the new data 
table_check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Users'"
if cursor.execute(table_check_query).fetchone():
    cursor.execute("DELETE FROM Users")
    print("Data in the 'Users' table has been deleted.")
else:
    print("The 'Users' table does not exist.")

cursor.execute("""
    CREATE table IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        Address TEXT,
        AGE INTEGER,
        Hobby TEXT
    );
""")

cursor.execute("""
    INSERT INTO Users (name,email,address,AGE,Hobby) 
    VALUES ('SAMEER','sameerkhanjan123@gmail.com','Rawalpindi','20','coding'),
    ('saeed','saeed@gmail.com','pindi','19','sleeping'),
    ('ali','ali123@gmial.com','lahore','14','gaming'),
    ('sadia','sadi123@yahoo.com', 'paris','19','singing')

""")

a = connect.cursor()
a.execute("""
    SELECT * FROM Users Where age = '19'; 
""")

# print(a.fetchall())
rows = a.fetchall()
for row in rows:
    print(row)
connect.commit()