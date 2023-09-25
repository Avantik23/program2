class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a/b;
        return ("Cannot divide by zero.")
    
calc=Calculator()

result=(calc.add(2,3))
print("Addition =",result)
    


        