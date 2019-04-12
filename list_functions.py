lucky_numbers = [666, 4, 8, 15, 16, 23, 42]
friends = friends = ['Roger', 'Kevin', 'Lucie', 'Oscar']

# friends.extend(lucky_numbers)
friends.append('Creed')
friends.insert(1, 'Pamela')
friends.remove('Roger')
# friends.clear()
friends.pop()  # remove last
print(friends.index('Oscar'))
print(friends.count('Lucie'))
friends.sort()
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()

print(friends)
print(lucky_numbers)
print(friends2)
