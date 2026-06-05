class Soldier:
    def __init__(self, name, rank, kills):
        self.name = name
        self.rank = rank
        self.kills = kills

    # Defines how the object is displayed when printed
    def __str__(self):
        return f"{self.rank} {self.name}"

    # Two soldiers are equal if they have the same name and rank
    def __eq__(self, other):
        return self.name == other.name and self.rank == other.rank

    # Compare soldiers by kill count
    def __gt__(self, other):
        return self.kills > other.kills

    # Add the kills of two soldiers
    def __add__(self, other):
        return self.kills + other.kills


s1 = Soldier("John", "Major", 12)
s2 = Soldier("David", "Captain", 15)
s3 = Soldier("Joey", "Major", 12)

print(s1)              # __str__
print(s1 == s3)        # __eq__
print(s2 > s1)         # __gt__
print(s1 + s2)         # __add__
