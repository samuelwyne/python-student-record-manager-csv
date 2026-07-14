import csv

while True:
   try:
      num=int(input("How many students do want to save?\n"))
      if num>0:
         break
   except ValueError:
      print("Invalid number of students try again: ")


#Adding student to CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Course", "Marks"])
    for i in range(num):
        name=input("Enter name:")
        while True: 
            try:
             age=int(input("Enter age:"))
             if age>0:
                break
             elif age>150:
                print("Invalid age! try again")
            except ValueError:
               print("Invalid age! try again")
                
        course=input("Enter student course:")
        while True:
           try:
             marks=int(input("Enter student marks:"))
             if marks>=0 and marks<=100:
                break
           except ValueError:
              print("Invalid marks! try again: ")
        writer.writerow([name, age, course, marks])
        print()

#searching student by name  from CSV file
print()        
print("Do you want to search for a student by name: ")
status=input("Enter (Y/N):")

if status.upper()=="Y":
    search=input("Enter name u want to find:")
    with open("students.csv","r")as file:
     reader=csv.reader(file)
     for row in reader:
        if search==row[0]:
            print(f"{row[0]:15}{row[1]:5}{row[2]:22}{row[3]:8}")
        else:
           pass
        print("NOT FOUND!")
else:  
    pass
                

# Read data from csv file
print()
print("===== STUDENT RECORDS =====")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]:15}{row[1]:5}{row[2]:22}{row[3]:8}")