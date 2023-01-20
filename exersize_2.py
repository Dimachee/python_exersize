def new (user):
    return user.count(5) == 3 
user = [19, 19, 15, 5, 5, 5, 1, 2]
lenghth = len(user)
print(lenghth, new(user))