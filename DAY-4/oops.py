class Greeting:
    name="Khushi"
    def __init__(self):
        print("Consructor is invoked")
    print("Class obj is invoked")
    def say_hello_world(self):
        print("Hello world")
    def __str__(self):
        return "This is a Greet class"
    def say_hello_name(self):
        print(f"hello,{self.name}")

obj=Greeting()
obj.say_hello_name()
obj.say_hello_world()
obj.say_hello_world()
obj.say_hello_world()

# print(obj)