from ctypes.wintypes import BOOLEAN
from pydoc import describe
import sqlite3 as lite

# functionlity goes here
class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con: 
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , description TEXT, price TEXT, is_private BOOLEAN NOT DEFAULT 1 )")
        except Exception:
            print("Unable to create a DB !")
    # TODO: read data
    def insert_data(self, data):
        try: 
            with con:
                cur = con.curser()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                    )
                return True
        except Exception:
            return False

    #TODO: delete data
    def fetch_data(self):
        try: 
            with con:
                cur = con.curser()
                cur.execute("SELECT * FROM courses")
                return cur.fetchall()
                    
        except Exception:
            return False


    def delete_data(self, id):
        
        try: 
            with con:
                cur = con.curser()
                sql = "DELETE FROM course WHERE Id = ?"
                cur.execute(sql, [id])
                return True
                    
        except Exception:
            return False       



# todo : provide interface to user

def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n ")
    print("*"*40)

    db = DatabaseManage()

    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)

    print('\n press 1. Insert a new Course\n')
    print('\n press 2. Show all Courses\n')
    print('\n press 3. Delete a course (NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")


    choice = input("\n Enter a choise: ")

    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Inter course price: ")
        private = input("\n Is this course private (0/1)")

        if db.insert_data([name, description, price, private ]):
            print("***Course was inseted successully***")
        else: 
            print("*** Something went wrong***")
    elif choice == "2":
        print("\n:: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Sl no : " + str(index +1))
            print("\n Course ID : " + str(item[0]))
            print("\n Course Name : " + str(item[1]))
            print("\n Course Description : " + str(item[2]))
            print("\n Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("\n Course Private : " + private)
            print("\n")
    elif choice == "3":
        record_id = input("Enter the course ID")

        if db.delete_data(record_id):
            print("Course deleted sucessfully")        
        else:
            print("Somethings went wrong")
    else:
        print("\n BAD CHOISE")


if __name__== '__main__':
    main()