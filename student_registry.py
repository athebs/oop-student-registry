class Student:
    def __init__(self, name) -> None:
        self._name = name 
        self._age = 13 
        self._grade = "12th" 
    
    
    @property 
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        #  Updates the students name only if the student name
        #  <br/> is 3 characters or more, holds 
        # no spaces or special characters,<br/> 
        # and is in title format 
        pass

    @property 
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        # updates the students age only if the age value
        # is an int, is greater than 11 and lower 
        # than 18 

        return "hi" 
    
    @property 
    def get_grade(self):
        return self.grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        #  Updates a students grade only if the grade
        #  falls within <br/> 9th - 12th grade
        # and the value is formatted with "th" <br/>next
        # the numbered grade | N/A |
        pass


    def __str__ (self):
        return f"Student 1:{self._name}"


Bob = Student("Bob")
print(Bob)

       
