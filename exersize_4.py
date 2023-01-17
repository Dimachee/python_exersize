def new(user):
    if (user / 2) ==0:   
        print(user, next_pile)
    else:
        print(user, next_pile)   
user = int(input('Enter even or odd number: '))
next_pile = user + 2 
new(user)
