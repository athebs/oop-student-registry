class Student:
    # adding attriubete to this class: name age and grade 
    # the init method 
    # passing arguments into the init method 

    def __init__(self, name, age =13 , grade = "12th") -> None:
        self.name = name 
        self.age = age 
        self.grade = grade 
    
    
    @property 
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self, new_name):
        if len(new_name)<= 3: 
            raise "Name must be longer than three Characters!"
        if new_name.isalpha() and " " not in new_name: 
            self.name = new_name
       

    @property 
    def get_age(self):
        return self.age
    
    @get_age.setter
    def set_age(self, new_age):
        return "hi" 
    
    @property 
    def get_grade(self):
        if self.get_grade == None: 
            return "No Grade"
        return self.grade
    # syntax would be @<GETTER-NAME>.setter 
    @get_grade.setter
    def set_grade(self, new_grade):
        self.grade = new_grade 

        #  Updates a students grade only if the grade
        #  falls within <br/> 9th - 12th grade
        # and the value is formatted with "th" <br/>next
        # the numbered grade | N/A |
        pass


    def __str__ (self):
        return f"Student 1:{self._name}"


bob = Student("Bob", 18, "12th")
alice =Student("alice", 11, "2nd")
#direct access the name 
print(alice.name)
# indrictest access the name 
print(alice.get_name)

#gets the get value with the get function 
print(alice.get_age) 

# when using a setter you must use the "=" because you can not call 
#  the setter cant use it like a function 
# like so 
alice.set_grade = 10 
# not like this alice.set_grade(10 )
print(alice.get_grade)

       
