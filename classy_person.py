'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def increase_age(self):
        self.age = self.age + 1
    
    def say_greeting(self):
        print(f'Hello world! My name is {self.name}!')
    
    def count_to_age(self):
        lst = []
        count = 1
        while count <= self.age:
            lst.append(count)
            count += 1
        for x in lst:
            print(x)

#taylor = Person(26, 'Taylor')
#print(taylor.age)
#taylor.say_greeting()
#taylor.increase_age()
#print(taylor.age)
#taylor.count_to_age()





# You won't need to call anything here.