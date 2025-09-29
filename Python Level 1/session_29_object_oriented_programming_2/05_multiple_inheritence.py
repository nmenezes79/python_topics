# Parent class 1
class Father:
    def skills(self):
        return "Gardening, Programming"

# Parent class 2
class Mother:
    def skills(self):
        return "Cooking, Art"

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        # Get skills from both parents
        father_skills = Father.skills(self)
        mother_skills = Mother.skills(self)
        return father_skills + ", " + mother_skills

# Create an object of Child
c = Child()
print("Child's skills:", c.skills())
