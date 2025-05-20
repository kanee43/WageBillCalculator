import csv
import os

from Employee import employee ##Imports employee class from separate file

class CSVManager: ##Creates the class to manager csv file
    def __init__(self,csvfile): ##Constructs an instance of the class called csvfile
        self.csvfile = csvfile

    def headers(self): ##A function which writes the headers of the csv file
        if os.path.exists(self.csvfile):
            with open(self.csvfile, 'w', newline='') as file: ##Opens and overwrites the csv file, tells python to ignore the line breaks
                writer = csv.writer(file) ##Writer class writes into the csv file
                writer.writerow(["forename", "surname", "ninum", "grade", "pay"]) ##Writes the information in a structured row system

    def add_employee(self, employee): ##Function to add employees to the csvfile
        if os.path.exists(self.csvfile):
            with open(self.csvfile, 'a', newline='') as file: ##Opens and adds to the file, does not overwrite it
                writer = csv.writer(file) ##Writes to the file
                writer.writerow([ ##Writes variable data in an array structured by rows
                employee.forename,
                employee.surname,
                employee.ninum,
                employee.grade,
                employee.pay
            ])

    def read_employees(self): ##Function to read the csv file
        employees = [] ##Creates an empty array list of employees to add to dynamically
        if os.path.exists(self.csvfile):
            with open(self.csvfile, 'r', newline='') as file: ##Opens and reads the csv file
                reader = csv.reader(file) ##Reads the opened file
            next(reader) ##Skips reading the headers row
            for row in reader: ##Reads each row written in the csv file
                forename = row[0]
                surname = row[1]
                ninum = row[2]
                grade = row[3]
                pay = row[4]
                employees.append(employee(forename, surname, ninum, grade, pay)) ##Reads added employee information
        return employees ##Returns employee information stored in csv file











