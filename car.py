class Car:
    sidemirrors="two"
    tires="four"
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def hoot(self):
        return f"I will buy a {self.model} car and it hoots pi!pi!pi"
    def move(self):
        return f"my {self.model} is color{self.color} and it moves when ignited" 
    