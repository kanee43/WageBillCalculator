class Calculator:

    def __init__(self,employees): ##Creates an instance of calculator and passes the employee array list as a variable
        self.employees = employees

    def totalpay (self):
        return sum (x.pay for x in self.employees) ##Loops through each pay row in csv file and returns sum

    def averagepay (self):
        return self.totalpay () / len(self.employees) ##Divides the total by the amount of employees stored in array

    def highestpay (self):
        return max(self.employees, key=lambda x: x.pay)

    def lowestpay (self):
        return min(self.employees, key=lambda x: x.pay) ##Returns the lowest amount of pay