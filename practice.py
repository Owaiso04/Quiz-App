class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.follwers += 1
        self.following += 1


user1 = User("001", "Jack")
user2 = User("002", "Tom")
