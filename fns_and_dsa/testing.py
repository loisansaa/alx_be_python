class student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def student_info(self):
    print(f"{self.name} is {self.age} years old")


student1 = student("Samuel", 18)
student1.student_info()



class product:
  def __init__(self,name,price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def total_value(self):
    total = self.price * self.quantity 
    return total
  
product1 = product("shoe", 50, 7)
print(product1.total_value())