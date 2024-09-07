class ShoppingCart:
    def __init__(self):
        self.items=[] 
    def add_item(self,item_name,price,quantity):
        item={"name":item_name,"price":float(price),"quantity":int(quantity)}
        self.items.append(item)
    def calculate_total(self):
        total=0
        for item in self.items:
            total+=item["price"]
        return total
    def remove_item(self,item_name):
         for item in self.items:
            if(item["name"] == item_name):
                self.items.remove(item)
                break
         else:
             print("item not found")

    def displayCart(self):
        if not self.items:
            print("cart is empty")
        else: 
         for item in self.items:
               print(item["name"]+" for "+str(item["price"])+" ("+str(item["quantity"])+")")
         print("total cost = "+str(self.calculate_total()))
           
    

def main():
   mycart=ShoppingCart()
   mycart.add_item("pepsi",3.9,4)
   mycart.add_item("biscuit",4,2)
   mycart.add_item("candy",1.5,2)
   mycart.remove_item("biscuit")
   mycart.displayCart()



main()