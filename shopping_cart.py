class Shopping:
    def __init__(self) -> None:
        self.items={}
        self.sum=0
        
    def add_items(self,item,price):
        self.items[item]=price
        self.sum+=price
        return self.sum
    def remove_items(self,item):
        sum-=self.items[item]
        self.items.pop(item)
    def total(self):
        return self.sum
    
s= Shopping()
s.add_items("Fruits",202)
s.add_items("Vegeatbles",332)
print(s.total())

        