class category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_product=0
       

    def __str__(self):
        return f"{self.name} {self.code} {self.no_of_product}"

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    
    def Lsort(self, k):
        n = len(k)
        for i in range(n):
            for j in range(i + 1, n):
                if k[j].price < k[i].price:
                    k[i], k[j] = k[j], k[i]

    def Hsort(self, h):
        n = len(h)
        for i in range(n):
            for j in range(i + 1, n):
                if h[j].price > h[i].price:
                    h[i], h[j] = h[j], h[i]

    def search(self, product_list):
        se = int(input("Enter the code: "))
        for i in product_list:
            if i.code == se:
                print(i.name, i.code, i.category, i.price)
                


cat1 = category("aa", 1011)
cat2 = category("bb", 1012)
cat3 = category("cc", 1013)


product1 = Product("aa", 1011, cat1, 10)
product2 = Product("ff", 1012, cat2, 110)
product3 = Product("cc", 1013, cat3, 180)
product4 = Product("dd", 1014, cat1, 190)
product5 = Product("ee", 1010, cat2, 100)
product6 = Product("yy", 1012, cat1, 19)
product7 = Product("gg", 1017, cat3, 20)
product8 = Product("hh", 1050, cat1, 500)
product9 = Product("ii", 1019, cat2, 300)
product10 = Product("kk", 1020, cat3, 900)

product_list = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

for product in product_list:
    product.category.no_of_products += 1

    # Print category info with its no_of_products
for category in [cat1, cat2, cat3]:
    print(f" {category.name} {category.code} {category.no_of_product}")


#  low to high
product1.Lsort(product_list)
for pro in product_list:
    print(pro.name, pro.code, pro.category, pro.price)

print()

#  high to low
product1.Hsort(product_list)
for pro in product_list:
    print(pro.name, pro.code, pro.category, pro.price)

# Search
product1.search(product_list)


