class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
p = Stack()
print (p.isEmpty())
n=int(input('Ingresa la cantidad de numero : '))
for i in range (n):
    x= int(input('Ingrese los valores:  '))
    p.push(x)
for i in range(n):
    print (x)
    

