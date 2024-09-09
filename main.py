#Modules:-
import os
import sys

#MYSQL Connection:-
try:
    import mysql.connector as sql
except:
    print("Errors:\n1) MySql is not Installed on System\n2) pip is not Installed\n3) MySQL is not connected with Python\n")
    print("Please Refer to the Documentation for Fix this")

#Database Creation/Connection:-
pass_wd=str(input("Enter MySQL Password: "))
try:
    db=sql.connect(host="localhost",user="root",passwd=pass_wd)
    cursor=db.cursor()
    if db.is_connected():
        try:
            cursor.execute("USE pyplm")
            db.commit()
            print("Database connected")
        except:
            cursor.execute("create database pyplm")
            cursor.execute("USE pyplm")
            
            print("New Database Created")
            db.commit()
            print("Database connected")        
except:
    print("Password is Wrong, Try Again")
    pass_wd2=str(input("Re-Enter MySQL Password: "))
    try:
        db=sql.connect(host="localhost",user="root",passwd=pass_wd2)
        cursor=db.cursor()
        if db.is_connected():
            try:
                cursor.execute("USE pyplm")
                db.commit()
                print("Database connected")
            except:
                cursor.execute("create database pyplm")
                cursor.execute("USE pyplm")
                
                print("New Database Created")
                db.commit()
                print("Database connected")
    except:
        print("Password is Wrong, Try Again [Last Chance]")
        pass_wd3=str(input("Re-Enter MySQL Password: "))
        try:
            db=sql.connect(host="localhost",user="root",passwd=pass_wd3)
            cursor=db.cursor()
            if db.is_connected():
                try:
                    cursor.execute("USE pyplm")
                    db.commit()
                    print("Database connected")
                except:
                    cursor.execute("create database pyplm")
                    cursor.execute("USE pyplm")
                    
                    print("New Database Created")
                    db.commit()
                    print("Database connected")
        except:
            print(" ")
            print("We are Unable to authorize You")
            print(" ")
            print("Press '1' to fix Errors")
            fix_db=int(input("Enter: "))
            print("")
            if fix_db==1:
                x=input("Enter Name of host (Default: localhost): ")
                y=input("Enter Name of user (Default: root): ")
                z=input("Enter Password: ")
                try:
                    db=sql.connect(host=x,user=y,passwd=z)
                    cursor=db.cursor()
                    if db.is_connected():
                        try:
                            cursor.execute("USE pyplm")
                            db.commit()
                            print("Database connected")
                        except:
                            cursor.execute("create database pyplm")
                            cursor.execute("USE pyplm")
                            
                            print("New Database Created")
                            db.commit()
                            print("Database connected")
                except:
                    print("\n")
                    print("Unable to authorize")
                    print("Please Refer to the Documentation for Fix this")
                    print("Errors May Occurs:\n1) MySql is not Installed on System\n2) pip is not Installed\n3) MySQL is not connected with Python\n")
            else:
                print("Thank You for Use Our Service\nPlease give us your feedback to improve our service")
                exit

#Password Manager:-
Admin_Passwd = "admin"

#First Time Run Setup:-
def Create_Table():
    try:
        Table="CREATE TABLE DATA (Student_ID INT(3), Book_ID INT(5))"
        cursor.execute(Table)
        db.commit()
    except:
        print("TABLE ALREADY EXIST")
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

#Credit:-
def credit():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Credit:-")
    print("Python Librery Project")
    print("Version: 1.0 BETA")
    print("\nCode By: Yash Garg\nTeam Members: Dhruv Gupta, Apurva Bansal, Ritesh Kumar Sinha, Anshul Sirohi, Saurav Agrawal\n")
    print("An Opne Source Project - Build for College Project 3rd SEM (SRM University Delhi-NCR)")
    print("Contact US via E-Mail: help.yashgarg@gmail.com\n")
    if (continue_Query()==1):
        start_menu()

#Menu:-
def start_menu():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("WELCOME\n")
    print("1) Admin Login\n2) Student Login\nPress '-1' for Exit\n")
    temp = int(input("Choose: "))
    if temp==1:
        pass_admin = str(input("Enter Admin Password: "))
        if (pass_admin==Admin_Passwd):
            Admin_Panel()
        else:
            print("Wrong Password!")
    elif temp==2:
        Student_Panel()
    elif temp==0:
        credit()
    elif temp==-1:
        exit_prog()
    else:
        print("Wrong inpur")
        start_menu()

def Admin_Panel():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("Admin Portal\n")
    print("1) View All Books Issued\n2) Edit Issued Books Data\n3) Delete Record\n4) Student Portal")

    temp = int(input("Choose: "))
    if temp==1:
        View_Table_Data()
    elif temp==2:
        Edit_Table_Data()
    elif temp==3:
        Delete_Row()
    elif temp==4:
        Student_Panel()
    elif temp==0:
        start_menu()
    else:
        print("Wrong Input")
        if continue_Query()==1:
            Admin_Panel()
        else:
            start_menu()
    
    if (continue_Query()==1):
        Admin_Panel()
    else:
        exit_prog()

def Student_Panel():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    print("WELCOME TO LIBRERY\n")
    print("1) Issue a New Book\n2) Return a Book\n3) View all Issued Book")
    temp = int(input("Choose: "))
    if temp==1:
        Issue_Book()
    elif temp==2:
        Return_Book()
    elif temp==3:
        View_Student_Issue_Book()
    elif temp==0:
        start_menu()
    else:
        Student_Panel()

    if (continue_Query()==1):
        Student_Panel()
    else:
        exit_prog()

#Commands:-
def continue_Query():
    print("Press '1' To Return")
    try:
        cont_que = int(input("Enter: "))
        if cont_que==1:
            return 1
        else:
            return 0
    except:
        start_menu()

def exit_prog():
    cursor.close()
    db.close()
    sys.exit()

#Admin Panel Commands:-
def View_Table_Data():
    view = "SELECT * FROM DATA"
    cursor.execute(view)
    results = cursor.fetchall()
    print("+------------+---------------+\n| Student ID |    Book ID    |\n+------------+---------------+")
    for i in results:
        j=str(i).split()
        for k in j:
            print(k,end="        | ")
        print()
        print("+------------+---------------+")

def Edit_Table_Data():
    print("\n1) Edit Book ID\n2) Return Back\n")
    temp = int(input("Choose: "))
    if temp==1:
        StudentID = int(input("Enter Student ID: "))
        BookID = int(input("Enter Correct Book ID: "))
        query = "UPDATE DATA SET Book_ID = '%d' WHERE Student_ID = '%d'" % (BookID, StudentID)
        cursor.execute(query)
        db.commit()
    elif temp==2:
        Admin_Panel()
    else:
        print("Wrong Input!")
        if continue_Query()==1:
            Admin_Panel()
        else:
            start_menu()

def Delete_Row():
    StudentID = int(input("Enter Student ID: "))
    query = "DELETE FROM DATA WHERE Student_ID = '%d'" % (StudentID)
    cursor.execute(query)
    db.commit()
    if continue_Query()==1:
        Admin_Panel()
    else:
        start_menu

#Student Panel Commands:-
def Issue_Book():
    try:
        x = int(input("Enter Student ID: "))
        y = int(input("Enter Book UPC Code: "))
        query = "INSERT INTO DATA (Student_ID, Book_ID) VALUES ('%d','%d')" % (x,y)
        cursor.execute(query)
        db.commit()
        print("Student ID: '%d'\nBook ID: '%d' \nhas been Issue Successfully\n" % (x,y))
        if continue_Query()==1:
            Student_Panel()
        else:
            Issue_Book()
    except:
        print("WRONG INPUT! ENTER Numbers Only\n")
        if continue_Query == 1:
            Issue_Book()
        else:
            Student_Panel()

def Return_Book():
    try:
        x = int(input("Enter Student ID: "))
        y = int(input("Enter Book ID which has to be Return: "))
        query = "DELETE FROM DATA WHERE Student_ID = '%d' AND Book_ID = '%d'" % (x,y)
        cursor.execute(query)
        db.commit()
        print("\n")
        if continue_Query() == 1:
            Student_Panel()
        else:
            Return_Book()
    except:
        print("WRONG INPUT!\n")
        if continue_Query() == 1:
            Student_Panel()
        else:
            Return_Book()

def View_Student_Issue_Book():
    try:
        x = int(input("Enter Student ID: "))
        query = "SELECT * FROM DATA WHERE Student_ID = '%d'" % (x)
        cursor.execute(query)
        results = cursor.fetchall()
        print("+------------+---------------+\n| Student ID |    Book ID    |\n+------------+---------------+")
        for i in results:
            j=str(i).split()
            for k in j:
                print(k,end="        | ")
            print()
            print("+------------+---------------+")
    except:
        print("Wrong Student ID!\n")
        if continue_Query() == 1:
            Student_Panel()
        else:
            View_Student_Issue_Book()

#Main Run:-
Create_Table()
start_menu()
