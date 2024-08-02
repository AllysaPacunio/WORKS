def createStack(): 
    stack = [] 
    return stack 
  
def isEmpty(stack): 
    return len(stack) == 0
  
def push(stack, x): 
    stack.append(x) 
  
def pop(stack): 
    if isEmpty(stack): 
        print("Error : stack underflow") 
    else: 
        return stack.pop(0) 

def myprogram(mylist): 
  list = createStack() 
  element = 0
  next = 0

  push(list, remove)
  
  while mylist:
    aa= mylist.pop(0)
    next= aa
  
    if isEmpty(list) == False: 
      element = pop(list) 
        
      while element < next : 
        print(str(element)+ " -> " + str(next)) 
                
        if isEmpty(list) == True : 
          break
        element = pop(list) 
  
      if  element > next: 
        push(list, element)
        
        if len(list) > 1:
          a=list.pop(0)
          list.append(a)
        
    push(list, next)
  
  while isEmpty(list) == False: 
    element = pop(list) 
    next = -1
    print(str(element) + " -> " + str(next)) 
  

mylist = [10,3,1,14,15,5]
remove= mylist.pop(0)
myprogram(mylist) 