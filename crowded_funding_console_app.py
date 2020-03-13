import json
import re
import os

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
count = 0

#function to check that the file is empty or not & exists or not
def is_empty (way):
    if  not os.path.exists(way) or os.stat(way).st_size==0:
        return True
    else:
        return False

#function to check that email in corect formate
def check(email):
    global count
    if not (re.search(regex, email)):
        print("Invalid Email")
    else:
        count += 1

#function to check that name in corect formate
def valid_name(name):
    global count
    if name.isdigit() or not name:
        print("this is invalid name")
    else:
        count += 1

#function to check that phone in egyption phone formate
def check_phone(phone):
    global count
    if not (re.match("^01[1520][0-9]{8}$", phone)):
        print("Invalid phone number")
    else:
        count += 1

#function to check that confirm_password exactly like password or not
def password_confirmation(password, confirm_password):
    global count
    if not (re.match(password, confirm_password)):
        print("password not matched")
    else:
        count += 1

#function to check that date in corect formate
def date_confirmation(date):
    if not (re.match("^\d{1,2}\/\d{1,2}\/\d{4}$", date)):
        print("Invalid date")

#function to create user
def create_user(f_name, l_name, email, password, phone):
    global count
    # global data
    if is_empty ("database.json") :
        data =[]
    else:
        with open("database.json", "r")as read_file:
            data = json.load(read_file)

    if count == 5 :
            user_data = {'first_name': f_name,
                         'last_name': l_name,
                         'Email': email,
                         'Password': password,
                         'Phone': phone}
            data.append(user_data)
            with open("database.json", "w")as write_file:
                json.dump(data, write_file)
            print("success registration")
            menue3()

    # print(count)
    # print(data)

# this is the first menue will appare for user
def menue1():
    print("welcome .. ")
    print("1)register")
    print("2)login ")
    print("3)Quit ")
    choise = input("plz enter your choise")
    if choise == "1":
        register()
    elif choise == "2":
        login()
    elif choise == "3":
        pass
    else:
        print("invald choice")

#this menue will appare  for user when he makes a correct login
def menue2(user_email):
    print("==============================================================")
    print("1)create project")
    print("2)delete project")
    print("3)show projects")
    print("4)edit project")
    print("5)search for project")
    print("6)Quit")
    men_choice = input("Enter your choice")
    if men_choice == "1":
        create_project(user_email)
    elif men_choice== "2":
        delete_project(user_email)
    elif men_choice== "3":
        show_projects(user_email)
    elif men_choice == "4":
        edit_project(user_email)
    elif men_choice == "5":
        search_project(user_email)
    elif men_choice == "6":
        pass
    else:
        print("invalid choice")

def menue3():
    print("==============================================================")
    print("1)login")
    print("2)quit")
    choice = input("enter your choice")
    if choice == "1":
        login()
    else:
        pass

def register():
    print("==============================================================")
    first_name = input("enter your first name")
    valid_name(first_name)
    last_name = input("enter your last name")
    valid_name(last_name)
    email = input("enter your email")
    check(email)
    password = input("enter your password")
    confirm_password = input("confirm your password")
    password_confirmation(password, confirm_password)
    mobile_phone = input("enter your phone")
    check_phone(mobile_phone)
    create_user(first_name, last_name, email, password, mobile_phone)



def login():
    with open("database.json", "r")as read_file:
        f1 = json.load(read_file)
        print(f1)
    print("==============================================================")
    user_name = input("enter your name")
    user_password = input("enter your password")
    for user in f1:
        if user["first_name"] == user_name and user["Password"] == user_password:
            print("success login")
            menue2(user["Email"])
            break
    else:
        print("error login")


def create_project(user_email):

    if is_empty(user_email+".json"):
        projects = []
    else:
        with open(user_email+".json", "r")as read_file:
            projects = json.load(read_file)
    print("=====================================================")
    title = input("enter the project's title")
    details = input("enter the details")
    total = input("enter the total target")
    start_date = input("enter the start_date")
    date_confirmation(start_date)
    end_date = input("enter the end_date")
    date_confirmation(end_date)
    project_data = {
        "title_project": title,
        "detaile_project": details,
        "total_target": total,
        "start_poject": start_date,
        "end_project": end_date
    }

    projects.append(project_data)
    with open(user_email+".json", "w") as write_file:
        json.dump(projects, write_file)
        print("project is created")

def show_projects(user_email):
    if is_empty(user_email + ".json"):
        print("there isn't projects")
    else:
        with open(user_email+".json", "r")as read_file:
            f1 = json.load(read_file)
            for project in f1:
                print(project)

def  delete_project(user_email):
    if is_empty(user_email + ".json"):
        print("there isn't projects")
    else:
        with open(user_email+".json", "r")as read_file:
            f1 = json.load(read_file)
            del_project = input("enter the project title ")
            for project in f1:
                if project["title_project"]==del_project:
                    f1.remove(project)
                    with open(user_email + ".json", "w") as write_file:
                        json.dump(f1, write_file)
                        print("success deletion")


def  search_project(user_email):
    if is_empty(user_email + ".json"):
        print("there isn't projects")
    else:
        with open(user_email + ".json", "r")as read_file:
            f1 = json.load(read_file)
            project_title=input("enter the project title")
            for project in f1:
                if project["title_project"]==project_title:
                    print(project)

def edit_project(user_email):
    if is_empty(user_email + ".json"):
        print("there isn't projects")
    else:
        with open(user_email + ".json", "r")as read_file:
            f1 = json.load(read_file)
            project_title = input("enter the project title")
            for project in f1:
                if project["title_project"] == project_title:
                    variables_changed = input("enter the variable you want to change it")
                    value_changed = input("enter the value you want to change it")
                    project[variables_changed]=value_changed
                    with open(user_email + ".json", "w") as write_file:
                        json.dump(f1, write_file)
                        print("success update")




menue1()
