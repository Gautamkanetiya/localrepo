import re
from datetime import datetime, timedelta


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company=None, type=None):

        list = [name, city, country, state]
        if any(any(char.isdigit() for char in name) for name in list):
            raise ValueError("------------")

        if type not in ["company", "contact", "billing", "shipping"]:
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


class Product:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return f"{self.name}"

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
        return (f" Oreder NO:{self.number} \n Date: {self.date} \n Company: {self.company} \n billinig:{self.billing} \n Shipping: {self.shipping}   ")

    def add_order_line(self, order_line):
        self.order_lines.append(order_line)

    def calculate_total_amount(self):
        total = sum(order_line.subtotal for order_line in self.order_lines)
        return total


    def display_order(self):
        # for i in order_list:
        #     print(f"number: {i.number} ")
        #     print(f"date: {i.date}")
        #     print(f"company:  {i.company}")
        #     print(f"billing:  {i.billing}")
        #     print(f"shipping: {i.shipping} ")
        for order_line in self.order_lines:
            print(f"  {order_line}")
        print(f"total: {ord1.calculate_total_amount()} ")

    def order_by_date(self,order_list):
        n=len(order_list)
        for i in range(n):
            for j in range(i + 1, n):
                if order_list[j].date < order_list[i].date:
                    order_list[i], order_list[j] = order_list[j], order_list[i]

    def is_current_month(self):
        current_date = datetime.now()
        return self.date.month == current_date.month and self.date.year == current_date.year





    @classmethod
    def current_month_list(cls, order_list):
        current_month_orders = [order for order in order_list if order.is_current_month()]
        return current_month_orders

    def search_number(serlf,order_list):
        search=int(input("enter the number of order:"))
        for i in order_list:
            if i.number==search:
                print(f"  number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")



class OrderLine:
    def __init__(self, order,product, quantity, price):
        self.order=order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = quantity * price

    def __str__(self):
        return f"{self.order} \n product: {self.product} \n qauntity:{self.quantity}  \n price: {self.price} \n subtotal:{self.subtotal}\n"

    def calculate_amount(self):
        return self.subtotal


pro1=Product("product1")
pro2=Product("product2")
pro3=Product("product1")
pro4=Product("product2")
pro5=Product("product1")

product_list=[pro1,pro2,pro3,pro4,pro5]




cus1 = Customer("gk ent", "abc@mail.com", "1234567890", "123 main bajar", "bota", "gujarat", "ind", None, "company")
cus2 = Customer("sk ent", "bdc@mail.com", "7548467890", "123 main bajar", "ahme", "gujarat", "ind", None, "shipping")
cus3 = Customer("ff ent", "fbs@mail.com", "3422567890", "123 main bajar", "ranp", "gujarat", "ind", None, "billing")
cus4 = Customer("dd ent", "sds@mail.com", "1454567890", "123 main bajar", "rajk", "gujarat", "ind", None, "contact")
cus5 = Customer("jj ent", "jjs@mail.com", "1234567890", "123 main bajar", "jamn", "gujarat", "ind", None, "company")


ord1 = Order(12540, datetime(2024, 1, 25), cus1, cus1, cus2, [])
ord2 = Order(32450, datetime(2024, 5, 15), cus3, cus5, cus2, [])
ord3 = Order(82650, datetime(2024, 1, 21), cus4, cus2, cus5, [])
ord4 = Order(52550, datetime(2024, 6, 12), cus1, cus4, cus2, [])
ord5 = Order(62850, datetime(2024, 8, 16), cus3, cus4, cus2, [])



order_line1 = OrderLine(ord1,pro1, 30, 100)
order_line2 = OrderLine(ord2,pro2, 70, 150)
order_line3 = OrderLine(ord3,pro5, 34, 200)
order_line4 = OrderLine(ord4,pro3, 40, 450)
order_line5 = OrderLine(ord5,pro4, 90, 800)



#add orderlines one by one in orderlines list
ord1.add_order_line(order_line1)
ord1.add_order_line(order_line2)
ord1.add_order_line(order_line3)
ord1.add_order_line(order_line4)
ord1.add_order_line(order_line5)


order_list=[ord1,ord2,ord3,ord4,ord5]
customer_list=[cus1,cus2,cus3,cus4,cus5]



print("-------------------------------------------order details---------------------------------------------------")
ord1.display_order()




#
# print("----------------------------------------order_by_date---------------------------------------------------------")
# ord1.order_by_date(order_list)
# for i in order_list:
#     print(f"  number: {i.number}   date: {i.date}  company:  {i.company}   billing:  {i.billing}   shipping: {i.shipping} ")
#
# print("----------------------------------------current_month---------------------------------------------------------")
#
# current_month_orders = Order.current_month_list(order_list)
# for order in current_month_orders:
#     print(f"  number: {order.number}   date: {order.date}  company:  {order.company}   billing:  {order.billing}   shipping: {order.shipping} ")
#
#









# product_wise_orders =[]
# for order in order_list:
#     # Iterate through order_lines in each order
#     for order_line in order.order_lines:
#         product_name = order_line.product.name
#         product_wise_orders[product_name].append(order)
# for product_name, orders in product_wise_orders.items():
#     print(f"Product: {product_name}")
#     for order in orders:
# #         print(f"  Order Number: {order.number}   Date: {order.date}   Company: {order.company}   Billing: {order.billing}   Shipping: {order.shipping}")
#
# print("----------------------------------------search order by numbers------------------------------------------------")
# ord1.search_number(order_list)