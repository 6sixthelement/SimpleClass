class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

   def Add(self):
       emp_name=input('Enter Name\n')
       emp_sal=input('Enter Salary \n')
       self.name=emp_name
       self.salary=emp_sal
       print ("Name : ", emp_name,  ", Salary: ", emp_sal)
       print ("Total Employee %d" % Employee.empCount)



# "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

emp1.Add()
