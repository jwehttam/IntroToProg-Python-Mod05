# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   MatthewJohnson, 11/14/2023, Created Script
# ------------------------------------------------------------------------------------------ #

import json
import io

###########################################################################################
# Define the constant for the menu text and filename where enrollment data will be stored #
###########################################################################################
MENU: str = '''
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''
FILE_NAME: str = 'Enrollments.json'

###########################################
# Define the Data Variables and constants #
###########################################
student_first_name: str = ''  # No longer needed to be initialized here.
student_last_name: str = ''  # No longer needed to be initialized here.
course_name: str = ''  # No longer needed to be initialized here.
students: list = []  # A table of student data, will be a list of dictionaries.
file: io.TextIOWrapper = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

################################################
# Try to load existing data from the JSON file #
################################################
# This block attempts to open the JSON file and load its contents into the 'students' list.
try:
    file: io.TextIOWrapper = open(FILE_NAME, 'r')
    students = json.load(file)  # Assuming the file contains a list of dictionaries

except FileNotFoundError as e:
    # This exception handles the case where the JSON file doesn't exist.
    print('---Technical Information---')
    print('File not found. Starting with an empty list of students.')
    print(e, e.__doc__, type(e), sep='\n')

except json.JSONDecodeError:
    # This exception handles JSON decoding errors if the file content is not valid JSON.
    print('Error decoding JSON from file. Starting with an empty list of students.')

except IOError as e:
    # This handles general I/O errors, such as file read/write issues.
    print('An I/O error occurred:', e)

except Exception as e:
    # This is a catch-all for any other exceptions not previously caught.
    print('An unexpected error occurred while reading the file:', e)

finally:
    # This block will always execute regardless of whether an exception was thrown.
    if file is not None:
        file.close()

#####################
# Main program loop #
#####################
while True:
    try:
        print(MENU)
        menu_choice = input('What would you like to do: ')
        #################
        # Menu Choice 1 #
        #################
        if menu_choice == '1':
            student_first_name = input('Enter the student\'s first name: ')
            if not student_first_name.isalpha():
                raise ValueError('The first name should only contain letters.')

            student_last_name = input('Enter the student\'s last name: ')
            if not student_last_name.isalpha():
                raise ValueError('The last name should only contain letters.')

            course_name = input('Please enter the name of the course: ')
            if not course_name.strip():  # Check if course_name is empty or contains only whitespace
                raise ValueError('Course name cannot be empty.')

            # Create a new dictionary for the student and append to the students list
            student_data = {'FirstName': student_first_name, 'LastName': student_last_name, 'CourseName': course_name}
            students.append(student_data)
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')

        #################
        # Menu Choice 2 #
        #################
        elif menu_choice == '2':
            print('-' * 50)
            if students:
                for student in students:
                    # Adjusted to access dictionary keys
                    print(f"Student: {student['FirstName']} {student['LastName']}, Course: {student['CourseName']}")
            else:
                print('No current student data to display.')
            print('-' * 50)

        #################
        # Menu Choice 3 #
        #################
        elif menu_choice == '3':
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file, indent=4)

            with open(FILE_NAME, 'r') as file:
                print('Data Saved! Here are the contents of the "Enrollments.json" file:')
                print(file.read())

        #################
        # Menu Choice 4 #
        #################
        elif menu_choice == '4':
            print('Exiting the program...')
            break

        else:
            print('Please only choose option 1, 2, 3, or 4.')

    ##############
    # Exceptions #
    ##############
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")
        break

    except ValueError as e:
        print(f"Input error: {e}")

    except Exception as e:
        print('An unexpected error occurred while taking input:', e)

print('Program Ended')
