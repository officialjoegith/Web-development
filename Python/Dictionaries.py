#thisdict = {
#    "brand" : "Ford",
#    "model" : "Mustang",
#    "brand" : "Ford",
#    "year" : 1964,
#    "is new" : True,
#    "features" : ["blue", "vB", 170.21, 5],
#    "seller details" : {
#        "seller_name" : "Uswat",
#        "seller_phone" : "+1-3249823"
#        }
#}
#for i in thisdict:
#    print(thisdict[i])
#print(thisdict["brand"])
#print(thisdict)
#print(len(thisdict))

#login_details = {
#}

#print("Welcome to my App\nRegister Below\n")

#login_details["username"] = input("Username: ")
#login_details["password"] = input("Password: ")

#print(logindetails)

#print("\nThanks for registering\nLogin to Continue\n")
#user_name = input("Enter your username: ")
#pass_word = input("Enter your password: ")

#if user_name == login_details["username"] and pass_word == login_details["password"]:
#    print("Login successful")
#else:
#    print("Incorrect Username or Password")

students_details = {
}

print("Welcome!!!\nInput your Biodata Below\n")

students_details["fullname"] = input("Fullname: ").upper()
students_details["matricno"] = input("Matric Number: ").upper()
students_details["dob"] = input("Date of Birth: ").upper()
students_details["sex"] = input("Gender: ").upper()
students_details["dept"] = input("Department: ").upper()
students_details["level"] = input("Level: ").upper()
students_details["year"] = input("Year: ").upper()
students_details["age"] = input("Age: ").upper()
students_details["weight"] = input("Weight: ").upper()
students_details["isMuslim"] = input("Are u a Mulsim: ").upper()

#print(students_details)

print("Thanks for entering your Biodata :)")

full_name = input("Enter your Fullname: ").upper()
matric_no = input("Enter your Matric number: ").upper()
d_o_b = input("Enter your Date of Birth: ").upper()
sex = input("Enter your Gender: ").upper()
dept = input("Enter your Department: ").upper()
level = input("Enter your Level: ").upper()
year = input("Enter Year: ").upper()
age = input("Enter your Age: ").upper()
weight = input("Enter your Weight: ").upper()
isMuslim = input("Are you a Muslim: ").upper()

if full_name == students_details["fullname"] and matric_no == students_details["matricno"] and d_o_b == students_details["dob"] and sex == students_details["sex"] and dept == students_details["dept"] and level == students_details["level"] and year == students_details["year"] and age == students_details["age"] and weight == students_details["weight"] and isMuslim == students_details["isMuslim"]:
    print("Biodata input correct")
else:
    print("Incorrect Biodata")



