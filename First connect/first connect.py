import sqlite3


connect = sqlite3.connect("data.db")



cursor = connect.cursor()
cursor.execute("""
     DROP table Users;
""")


cursor.execute("""
    CREATE table Users (
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
    VALUES ('SAMEER','sameerkhanjan123@gmail.com','Rawalpindi','20','coding')
""")

connect.commit()