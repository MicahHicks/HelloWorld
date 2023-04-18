ai_name = 'bob'
print('Hello my name is ' + ai_name + '. I will be your assistant today.')
name = input('What is your name? ')
laptop = input('Hello ' + name + ', what are you looking for today? ')
print('We have many different types of ' + laptop + 's for sale.')
gaming = 'gaming'
work = 'work'
user_response = input('What type of ' + laptop + ' are you looking for? ')
if user_response == "gaming":
    print('Ok, we have many different types of ' + gaming + ' ' + laptop + 's.')
elif user_response == "work":
    print('Ok, we have many different types of ' + work + ' ' + laptop + 's.')
else:
    print('Sorry we do not sell that.')

user_response1 = input('Which brand do you wish to look at? ')
if user_response1 == "msi":
    choice = input('Ok, we have three in stock, would you like to see them? ')
    if choice == "yes":
        print('There is one intel i5 laptop, and two intel i7 laptops.')
    else:
        print('Thank you for visiting our store.')
elif user_response1 == "lenovo":
    choice = input('Ok, we have two in stock. Would you like to see them? ')
    if choice == "yes":
        print('Here they are.')
    else:
        print('Thank you for visiting our store.')
elif user_response1 == "hp":
    choice = input('Ok, we have three in stock, would you like to see them? ')
    if choice == "yes":
        print('There is one HP Spectre laptop, one HP Pavilion laptop and one HP ProBook laptop.')
    else:
        print('Thank you for visiting our store.')
else:
    print('Sorry, we do not have that brand in stock.')

user_response2 = input('Which one do you want to buy? ')
if user_response2 == "intel i5 laptop" or user_response2 == "intel i5" or user_response2 == "i5":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "intel i7 laptop" or user_response2 == "intel i7" or user_response2 == "i7":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "HP Spectre laptop" or user_response2 == "HP Spectre" or user_response2 == "Spectre":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "HP Pavilion laptop" or user_response2 == "HP Pavilion" or user_response2 == "Pavilion":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "HP ProBook laptop" or user_response2 == "HP ProBook" or user_response2 == "ProBook":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
else:
    print('Sorry, we do not have that laptop in stock.')