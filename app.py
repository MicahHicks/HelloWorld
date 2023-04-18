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
    print('Ok, we have many different types of ' + work +  ' ' + laptop + 's.')
else:
    print('Sorry we do not sell that.')
user_response1 = input('Which brand do you wish to look at? ')
if user_response1 == "msi":
    input('Ok, we have three in stock, would you like to see them? ')
    print('There is one intel i5 laptop, and two intel i7 laptops.')
else:
    print('Sorry we do not sell that')
user_response2 = input('Which one do you want to buy? ')
if user_response2 == "intel i5 laptop":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "intel i5":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "i5":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "intel i7 laptop":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "intel i7":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
elif user_response2 == "i7":
    print('Ok, thanks for your purchase. It will arrive at your house shortly.')
    if user_response == "work":
        user_response3 = input('Which brand do you wish to look at? ')
        if user_response3 == "lenovo":
            print('Ok, we have two in stock. Would you like to see them?')
        elif user_response3 == "hp":
            print('Ok, we have three in stock, would you like to see them?')
            print('There is one HP Spectre laptop, one HP Pavilion laptop and one HP ProBook laptop.')
        else:
            print('Sorry, we do not have that brand in stock.')
        user_response4 = input('Which one do you want to buy? ')
        if user_response4 == "HP Spectre laptop":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "HP Spectre":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "Spectre":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "HP Pavilion laptop":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "HP Pavilion":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "Pavilion":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "HP ProBook laptop":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "HP ProBook":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        elif user_response4 == "ProBook":
            print('Ok, thanks for your purchase. It will arrive at your house shortly.')
        else:
            print('Sorry, we do not have that laptop in stock.')