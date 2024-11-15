# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# RRoot,1/1/2030,Created Script
# Luis, 11/13/2024, Edited script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
json_data: str = ''

import json # This imports the Python JSON Module to work with a file of this format

# Custom Exception for invalid menu choice
class InvalidMenuChoiceError(Exception):
    pass

# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
try:
       file = open(FILE_NAME, 'r')
       students = json.load(file)
       file.close()
       # This exception is a caveat of a missing file. It notifies the file
       # was not found and the following steps to correct the error.

except FileNotFoundError as e:
    print('The file',FILE_NAME,'you are trying to open does not exist or may be misplaced in a different directory')

# Write the contents to a file for each row in the table

for item in students:
    print(f"FirstName: {item['FirstName']}, LastName: {item['LastName']}, CourseName: {item['CourseName']}")

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    try:
        menu_choice = input("What would you like to do: ")
    # Input user data

        if menu_choice not in ['1', '2', '3', '4']:
          raise InvalidMenuChoiceError("Invalid choice. Please select a valid option (1, 2, 3, or 4).")
        #break  # Exit the loop if a valid choice is entered
    except InvalidMenuChoiceError as e:
       print(e)  # Print the exception message and prompt again
       continue


    if menu_choice == "1":  # This will not work if it is an integer!
        while (True):
          try:
              student_first_name = input("Enter the student's first name: ")
              if not student_first_name.isalpha():
                 raise ValueError("Invalid entry. Input must be a string.\nPlease try again")
              break

          except ValueError as ve:
             print(ve)  # Print the exception message and prompt again
             continue

        while(True):
          try:
               student_last_name = input("Enter the student's last name: ")
               if not student_last_name.isalpha():
                 raise ValueError("Invalid entry. Input must be a string.\nPlease try again")
               break

          except ValueError as ve: #"ve" is a variable reference for the exception "ValueError
             print(ve)  # Print the exception message and prompt again
             continue

        course_name = input("Please enter the name of the course: ")

        student_data = {
            "FirstName": student_first_name,
            "LastName": student_last_name,  # add input information into this dictionary row
            "CourseName": course_name
          }



        students.append(student_data) #this line appends the new student_data row to the students list
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.") #prompts message
        continue


    # Present the current data
    elif menu_choice == "2": # Identifies the second menu choice

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students: #using a for loop displays every element of the list of rows in a customized sentence.
            message = print(f"In the course '{student['CourseName']}', {student['FirstName']} {student['LastName']} is enrolled.")
        print("-"*50)
        continue


    # Save the data to a file
    elif menu_choice == "3":
         file = open(FILE_NAME, "w") #This overwrites the previous file with new appended row.
         json.dump(students, file)# JSON Module function "json.dump" saves the new row into the JSON File
         file.close()
         continue

    # Stop the loop
    elif menu_choice == "4":
        break  # breaks out of the loop and ends the program.
    #else:            #this step waa replaced by the exception
        #print("Please only choose option 1, 2, or 3")

print("Program Ended")