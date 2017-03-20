#!/usrbin/env python

my_list = ['thing 1', 'thing 2', 'thing 3', 'thing 4', 'thing 5']

new_list = my_list[:]

my_list.append('thing 6')


print my_list.pop(0)

my_list.sort()

print my_list

