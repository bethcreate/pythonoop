class Dog:
    ears="two"
    tail="one"
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age
    def bark(self):
        return f"my {self.age} year old {self.breed} barks gu!gu!gu"
    def run(self):
        return f"my {self.age} years old {self.breed} can run 5 kilometres"