import sqlite3


# Registration:
def registration(email_id, password):
    try:
        with sqlite3.connect("users.db") as connection:
            cur = connection.cursor()
            cur.execute("INSERT into User_Authentication (Email_ID, Password) values (?,?)", (email_id, password))
            connection.commit()
            cur.close()
            return 1

    except sqlite3.Error as error:
        print(error)
        connection.rollback()
        return 0

    finally:
        connection.close()


# Login: -
def login(email_id, passw):
    try:
        with sqlite3.connect("users.db") as connection:
            cur = connection.cursor()
            cur.execute("SELECT password from User_Authentication where Email_ID = (?)", [email_id])
            rows = cur.fetchone()

            if rows is None:
                return 0

            else:
                temp_password = rows[0]
                connection.commit()
                cur.close()

                if temp_password == passw:
                    return 1

                else:
                    return 0

    except sqlite3.Error as error:
        print(error)
        connection.rollback()
        return 0

    finally:
        connection.close()


# Delete: -
def delete_account(email_id):
    try:
        with sqlite3.connect("users.db") as connection:
            cur = connection.cursor()
            cur.execute("DELETE from User_Authentication where Email_ID = (?)", [email_id])
            connection.commit()
            cur.close()
            return 1

    except sqlite3.Error as error:
        print(error)
        connection.rollback()
        return 0

    finally:
        connection.close()


# Change Password: -
def change_password(email_id, old_password, new_password):
    try:
        with sqlite3.connect("users.db") as connection:
            cur = connection.cursor()
            cur.execute("SELECT password from User_Authentication where Email_ID = (?)", [email_id])
            rows = cur.fetchone()

            if rows is None:
                return 0

            else:
                current_password = rows[0]

                if current_password == old_password:
                    cur.execute('''UPDATE User_Authentication SET Password = ? WHERE Email_ID = ?''',
                                (new_password, email_id))
                    connection.commit()
                    cur.close()
                    return 1

                else:
                    return 0

    except sqlite3.Error as error:
        print(error)
        connection.rollback()
        return 0

    finally:
        connection.close()


if __name__ == '__main__':
    registration("anjaniy01salekar@gmail.com", "password")
    login("anjaniy01salekar@gmail.com")
