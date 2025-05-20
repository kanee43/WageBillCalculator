from CSVManager import CSVManager
from Employee import employee
from Calculator import Calculator
##Imports classes and functions from three other files

def menu(): ##Function create a menu
    print("1: Add employee")
    print("2: Show employees")
    print("3: View total pay")
    print("4: View average pay")
    print("5: View lowest pay")
    print("6: View highest pay")
    print("7: Exit")

def main():
    csvmanager = CSVManager('employeewages.csv') ##Creates an instance of the csv manager class and creates a csv file called employee wages
    employees = csvmanager.read_employees() ##Calls the read function in csv manager to read employee array

    while True:
        menu() ##Calls the menu function
        choice = input("Enter your choice: ") #Reads user input and stores it as choice

        if choice == '1': #Takes user input and stores it in CSV file and employees array
            forename = input("Enter forename: ")
            surname = input("Enter surname: ")
            ninum = input("Enter National Insurance Number: ")
            grade = input("Enter Grade: ")
            pay = input("Enter pay: ")

            new_employee = employee(forename, surname, ninum, grade, pay)
            csvmanager.add_employee(new_employee)
            employees.append(new_employee)
            print ("Employee added successfully")

        elif choice == '2': #A for loop that displays each iteration of employee object in array
            if employees:
                for x in employees:
                    print(x)

        elif choice == '3': #Creates an instance of calculator, prints a formatted version of total pay
            calc = Calculator(employees)
            totalpay = calc.totalpay()
            print(f"Total pay: £{totalpay:.2f}")

        elif choice == '4': #Creates an instance of calculator, prints formatted verion of average pay
            calc = Calculator(employees)
            averagepay = calc.averagepay()
            print(f"Average pay: £{averagepay:.2f}")

        elif choice == '5': #Creates an instance of calculator, prints formatted version of lowest pay
            calc = Calculator(employees)
            lowestpay = calc.lowestpay()
            print(f"Lowest pay: {lowestpay.forename} {lowestpay.surname} with pay £{lowestpay.pay:.2f}")

        elif choice == '6':
            calc = Calculator(employees)
            highestpay = calc.highestpay()
            print(f"Highest pay: {highestpay.forename} {highestpay.surname} with pay £{highestpay.pay:.2f}")

        elif choice == '7': #Exits the program by breaking the loop
            break

if __name__ == "__main__":
    main()











