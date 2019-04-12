monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

# print(monthConversions)
print(monthConversions['Nov'])  # November
print(monthConversions.get('Dec'))
print(monthConversions.get('Luv', 'Not a valid key'))  # Default value
