
from Employee import Employee

def main():
    emp1 = Employee("Osman","Mutlu","055555555555","osman_mutlu_2205@hotmail.com","Engineer","6000")
    emp2 = Employee("Beyza","Gur","05555555555","beyza.gur@gmail.com","Engineer","9000")
    emp1.display()
    print("-----------------------")
    emp2.display()
    
    
if __name__ == '__main__':
    main()