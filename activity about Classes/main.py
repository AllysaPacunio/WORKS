class Person:
  def __init__(self,name,age,place):
    self.name= name
    self.age= age
    self.place= place
    print(f"A new person was born, named {self.name}.")

  def age_gap(self,Al,Ay):
    if Al.age > Ay.age:
      gap=  Al.age - Ay.age
      print(f'The age gap between {Al.name} and {Ay.name} was {gap} years.')
      
    elif Al.age < Ay.age:
        gap=  Ay.age - Al.age
        print(f'The age gap between {Al.name} and {Ay.name} was {gap} years.')
      
    else: 
        gap= "same"
        print(f'{Al.name} and {Ay.name} are in the {gap} age.')

  def birthplace(self, Al, Ay):
    print(f'{Al.name} was born in {Al.place}, while {Ay.name} was born in {Ay.place}. ')

class Painting:
  def painter(self,Al):
    print(f'{Al.name} creates a new Painting.')

  def artwork(self,Ay):
    print(f'A Painting of {Ay.name} was created.')

if __name__ == '__main__':
  Al= Person("Alex",  18, "Bulacan")
  Ay= Person("Aysa", 14, "Manila")


  Al.age_gap(Al, Ay)
  Ay.birthplace(Al,Ay)
  
  r= Painting()
  r.painter(Al)
  
  p= Painting()
  r.artwork(Ay)




 
  

  

  

  
  
  

  
 
  