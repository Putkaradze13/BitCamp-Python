# Hello program with various kinds of greetings

name = input('What is your name? ').title()

first_letter = name[0].lower()

letters_list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g',]
letters_list2 = ['h', 'i', 'j', 'k', 'l', 'm', 'q',]
letters_list3 = ['r', 's', 't', 'n', 'o', 'p',]

if first_letter in letters_list1: 
    print(f'Hello, {name},' ' Nice to meet you!')
elif first_letter in letters_list2:
    print(f'Hey there, {name},' ' It is nice meeting you!')
elif first_letter in letters_list3:
    print(f'Greetings, {name},' ' Have a nice day!')
else:
    print(f'Hi, {name},' ' How do you do!')