class category:
    def __init__(self, name, code,parent=None):
        self.name = name
        self.code = code
        self.no_of_products=0
        self.parent=parent
        self.display_name=self.generate_display_name()
        self.products=[]
       
#this function use for print the object
    def __str__(self):
        return f"{self.name} {self.code} {self.no_of_products}"
    
 #update the no of product    
    def update(self, product_list):
        for product in product_list:
            if product.category == self:
                self.no_of_products += 1
                
#add new product               
    def add_product(self, product):
        self.products.append(product)
                
   
#generate display name                
    def generate_display_name(self):
        if self.parent:
            return f"{self.parent.display_name} > {self.name}"
        else:
            return self.name   
        
#display detais of name ,code, display name,no of products etc       
    def display_details(self):
        print(f"Category Code:{self.name} ({self.code})")
        print(f"Display Name: {self.display_name}")
        print(f"No. of products: {self.no_of_products}")
    
        for product in self.products:
            print(f"  name:  {product.name}    code:  {product.code}    price:  {product.price}")
        print()
    

class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        
#get the product price
    def get_price(self):
        return self.price
    
# get the category name    
    def get_name(self):
        return self.category.name
    
#sort the product list by category name
    def sort_products_by_name(product_list):
        n = len(product_list)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if product_list[j].get_name() > product_list[j + 1].get_name():
                    product_list[j], product_list[j + 1] = product_list[j + 1], product_list[j]
                    

    
#low to high price
    def Lsort(self, k):
        n = len(k)
        for i in range(n):
            for j in range(i + 1, n):
                if k[j].get_price() < k[i].get_price():
                    k[i], k[j] = k[j], k[i]
                    
#high to low price
    def Hsort(self, h):
        n = len(h)
        for i in range(n):
            for j in range(i + 1, n):
                if h[j].get_price() > h[i].get_price():
                    h[i], h[j] = h[j], h[i]
                    
#search product by code                    
    def search(self, product_list):
            se = int(input("Enter the code: "))
            for i in product_list:
                if i.code == se:
                    print(f"Name:  {i.name}     Code: {i.code}    Category: {i.category}    price: {i.price}")
                

#5 category object
vehicle =category("duster", 1014)
car =category("bugaty", 1015,parent=vehicle)
petrol =category("caren", 1016,parent=car)
metro=category("hoster",1017,parent=petrol)
railway=category("gloster",1018,parent=metro)

#3 object category
bullet= category("archer", 1011)
brezza= category("polo", 1012)
honda= category("verna", 1013)


cat_list=[vehicle,car,petrol,metro,railway,bullet,brezza,honda]

#10 product
product1 = product("aa", 1019, bullet, 10)
product2 = product("ff", 1020, brezza, 110)
product3 = product("cc", 1021, honda, 180)
product4 = product("dd", 1022, bullet, 190)
product5 = product("ee", 1023, brezza, 100)
product6 = product("yy", 1024, bullet, 19)
product7 = product("gg", 1025, honda, 21)
product8 = product("hh", 1026, bullet, 500)
product9 = product("ii", 1027, brezza, 300)
product10 = product("kk", 1028, honda, 900)

#create 3 product object for each category
product11 = product("ll",1029, vehicle, 450)
product12 = product("mm",1030, vehicle, 200)
product13 = product("nn",1031, vehicle, 350)

product14 = product("oo",1032, car, 600)
product15 = product("pp",1033, car, 800)
product16 = product("qq",1034, car, 500)

product17 = product("jj",1035, petrol, 500)
product18 = product("ss",1036, petrol, 400)
product19 = product("tt",1037, petrol, 900)

#add the new category in products
vehicle.add_product(product11)
vehicle.add_product(product12)
vehicle.add_product(product13)
car.add_product(product14)
car.add_product(product15)
car.add_product(product16)
petrol.add_product(product17)
petrol.add_product(product18)
petrol.add_product(product19)

product_list = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10,product11,product12,product13,product14,product15,product16,product17,product18,product19]

#update the product list
for category in cat_list:
    category.update(product_list)

# Print category info with its no_of_products
print("<........ Print category info with its no_of_products......>")
for category in cat_list:
    print(f" Neame:  {category.name}    Code:  {category.code}    NO_of_product:  {category.no_of_products}")
    
print()

#  low to high price
print(" <...............low to high price....,...........>")
product1.Lsort(product_list)
for pro in product_list:
    print(f"Name:  {pro.name}     Code:  {pro.code}    Category:  {pro.category}    price:  {pro.price}")

print()

#hitgh to low price
    
print(" <................high to low price...............>")
product1.Hsort(product_list)
for pro in product_list:
    print(f"Name:  {pro.name}     Code:  {pro.code}    Category:  {pro.category}    price:  {pro.price}")

print()

#display details
for category in cat_list:
    category.display_details()

print()
    
#product list by order by category name
print("<................product list by order by category name..........>")
product.sort_products_by_name(product_list)
for pro in product_list:
    print(f"Name:  {pro.name}     Code:  {pro.code}    Category:  {pro.category}    price:    {pro.price}")
    


print()

#Search product by code
print("<...............Search product by code............>")
product1.search(product_list)


