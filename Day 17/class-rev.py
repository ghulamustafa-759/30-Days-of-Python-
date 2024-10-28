class User:
    def __init__(self, name, reg_no) -> None: #defines self, plus can use many parameters for objs
        print("New user being created...")
        self.name = name
        self.reg_no = reg_no
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Gm",203002) #attributes to objs
user2 = User("Mg", 203003)
print("Calling objs now")

print(user1.name, user1.reg_no) #calling objs
print(user2.reg_no, user2.name)

print(user2.followers)
user1.follow(user2)
print("You are now following user 2!")
print(user2.followers)