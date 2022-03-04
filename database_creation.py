import sqlite3


# Creation: -
def creation():
    con = sqlite3.connect("users.db")

    con.execute("create table User_Authentication (Email_ID TEXT PRIMARY KEY NOT NULL, Password TEXT NOT NULL)")

    print("Table created successfully")

    con.close()


if __name__ == '__main__':
    creation()
