###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('First name: ')
last_name = keyboard.input_string('Last name: ')
age = keyboard.input_integer('Age: ')
salary = keyboard.input_real('Salary:')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}')
print(f'Last name: {last_name}')
print(f'Age: {age}')
if is_salary_hidden == False:
    print(f'Salary {salary}')
elif is_salary_hidden == True:
    print('Hidden salary')