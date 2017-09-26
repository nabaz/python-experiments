import time
import datetime

class YearToTurnHundred:
    """Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old.
    Extras:
    - Add on to the previous program by asking the user for another number and
     printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    - Print out that many copies of the previous message on separate lines.
    (Hint: the string "\n is the same as pressing the ENTER button)"""

    def __init__(self, name, age):
        super(YearToTurnHundred, self).__init__()
        self.name = name
        self.age = int(age)
        self.current_year = datetime.date.today().strftime("%Y")

    def is_integer(age):
        return isinstance(age, int)

    def age_to_hundred(self):
        return (100 - self.age) + int(self.current_year)

    def __str__(self):
        return "hey {} in {} you become 100 years old you still got {} for that".format(self.name, self.age_to_hundred(), 100- self.age)


name = input("Your name please: ")
age = int(input("Please enter your age: "))

years_to_hunred = YearToTurnHundred(name, age)

print(years_to_hunred)
