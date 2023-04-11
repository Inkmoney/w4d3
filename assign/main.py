
# Q1
def array(arr):
    return arr[::-1]
_array = ["tail", "body", "head"]
fixed_array = array(_array)
print(fixed_array)  


def array(arr):
    result = []
    i = len(arr) - 1
    while i >= 0:
        result.append(arr[i])
        i -= 1
    return result

_array = ["tail", "body", "head"]
fixed_array = array(_array)

print(fixed_array)

#2
class Person():
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

person = Person("John", "Doe", "30")
print(person.age) 


from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name: str
    age: int

person = Person("John", "Doe", 30)
print(person.age)

#Quesion 3
class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name()) 
print(person.age)



class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

person = Person('Yukihiro', 'Matsumoto', 47)
print(person.full_name()) 
print(person.age)

