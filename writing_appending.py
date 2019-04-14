# r read, w write (overwrite), a append, r+ read/write
employee_file = open('employees1.txt', 'w')

employee_file.write('\nKelly - Singer')

employee_file.close()
