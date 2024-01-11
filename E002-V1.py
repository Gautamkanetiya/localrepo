import re
from datetime import datetime, timedelta

class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company=None, type=None):

        list = [name, city, country, state]
        if any(any(char.isdigit() for char in name) for name in list):
            raise ValueError("------------")

        if type not in ["company", "contact", "billing", " shipping"]:
            raise ValueError("Invalid customer type")

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number")

        if not self.validate_email(email):
            raise ValueError("Invalid email address")

        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.company = company
        self.type = type

    def validate_email(self, email):
        return bool(re.match(r'^\S+@\S+\.\S+$', email))

    def __str__(self):
        return (
            f"{self.name}    {self.email}     {self.phone}   {self.street}    {self.city}   {self.state}    {self.country}  {self.company}   {self.type}")


    def display(self):
        print(self)


class Order:
    def __init__(self, number, date, company, billing, shipping, order_lines=None):

        if date < datetime.now():
            raise ValueError("Order date must be today or in the future")

        self.number = number
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = []

    def __str__(self):
        return (
            f"{self.number}    {self.date}     {self.company}   {self.billing}    {self.shipping}   ")

    def add_order_line(self, order_line):
        self.order_lines.append(order_line)



    def calculate_amount(self):
        total = sum(order_line.subtotal for order_line in self.order_lines)
        return total

    def display_order(self):
        print(self)

class OrderLine:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = quantity * price

    def calculate_total_amount(self):
        return self.subtotal



order_line1 = OrderLine("Product1", 30, 100)
order_line2 = OrderLine("Product2", 30, 150)

cus1 = Customer("gk ent", "abc@mail.com", "1234567890", "123 main bajar", "City ", "State", "Country", None, "company")
cus2 = Customer("sk ent", "abc@mail.com", "1234567890", "123 main bajar", "City", "State","Country", cus1, "company")

ord1 = Order("12540", datetime(2024, 1, 15), cus1, cus1, cus2, [order_line1, order_line2])
ord2 = Order("22150", datetime(2024, 4, 25), cus2, cus1, cus2, [order_line1, order_line2])

ord1.add_order_line(order_line1)
ord1.add_order_line(order_line2)


order_list=[ord1,ord2]
customer_list=[cus1,cus2]


print("---------------------------------------------customer list -----------------------------------------------")
for i in customer_list:
    i.display()
print("-------------------------------------------order details---------------------------------------------------")

for i in order_list:
    i.display_order()

print(f"total: {ord1.calculate_amount()} ")
print(f"sub_total:{order_line1.calculate_total_amount()}")

