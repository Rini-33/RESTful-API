import sqlite3
conn = sqlite3.connect("demo.db")
cur  = conn.cursor()
cur.execute('''
            CREATE TABLE Users_table(
                ID INTEGER,
                first_name TEXT,
                last_name TEXT,
                age INTEGER,
                gender TEXT,
                email TEXT,
                phone INTEGER,
                Birth_date DATETIME, 
                Primary Key(first_name) 
            )''')

cur.execute('''
            INSERT INTO Users_ table VALUES 
            (1, 'John', 'Francis', 23, 'Male', 'john123@gamil.com', 9876543219, 1999-04-12),
            (2, 'Jack', 'Johnson', 25, 'Male', 'jack123@gamil.com', 9837774777, 1997-03-13),
            (3, 'Will', 'Wildrick', 28, 'Male', 'will123@gamil.com',8773737777, 1996-02-11),
            (4, 'William', 'Alex', 27, 'Male', 'william23@gamil.com',7889999999, 1995-01-12)''')
print("Success!!Connection has been established between sqlite3 and python")

# #Fetching input from the user
# User_Input = input()
# cur.execute('''SELECT * FROM table where first_name like (%User_Input)''')
conn.commit()
conn.close()