def new (user):
    return user.count(19) == 2 and user.count(5) >=3
user = [19, 19, 15, 5, 3, 5, 5, 2]
print(new(user))