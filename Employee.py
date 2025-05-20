class employee: ##Creates an employee class
    def __init__(self, forename, surname, ninum, grade, pay): ##Constructs the class, defines parameters
        self.forename = forename
        self.surname = surname
        self.ninum = ninum
        self.grade = grade
        self.pay = float(pay)

    def __str__(self): ##Formats the string of the object, else displaying the object will show its location in system memory
        return f"{self.forename} {self.surname}, NI: {self.ninum}, Grade: {self.grade}, Pay: £{self.pay:.2f}"




