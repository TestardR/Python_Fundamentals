# r read, w write, a append, r+ read/write
employee_file = open('employees.txt', 'r')

# make sure it is readable
# print(employee_file.readable())

# print(employee_file.read())
# print(employee_file.readline())

# put each line in an array
# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
