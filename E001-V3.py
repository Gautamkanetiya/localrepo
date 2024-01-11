class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []

    def __str__(self):
        return f"{self.name} {self.code} {len(self.products)}"


class Product:
    def __init__(self, name, code, category, price, stock_at_locations):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        self.stock_at_locations = stock_at_locations

    def __str__(self):
        locations_str = ', '.join([f"{location.name} ({location.code}): {quantity}" for location, quantity in self.stock_at_locations.items()])
        return f"Product name: {self.name}  Code: {self.code}  Category: {self.category.name}  Price: {self.price}  Stock at Locations: {locations_str}"

    def move(self, from_location, to_location, quantity):
        try:
            if self.stock_at_locations[from_location] >= quantity:
                # Check if there is sufficient stock at the 'from_location'

                # Create a new movement instance
                new_movement = Movement(from_location, to_location, self, quantity)
                # Append the new movement to the 'movements_list' class variable in the Movement class
                Movement.movements_list.append(new_movement)

                # Update product stock at locations
                self.stock_at_locations[from_location] -= quantity
                # Check if 'to_location' is present in 'stock_at_locations'
                if to_location in self.stock_at_locations:
                    # If present, update the stock quantity by adding the new quantity
                    self.stock_at_locations[to_location] += quantity
                else:
                    # If not present, initialize 'to_location' with the new quantity
                    self.stock_at_locations[to_location] = quantity

                # Print a success message
                print(f"Moved {quantity} units of {self.name} from {from_location.name} to {to_location.name}")
            else:
                # Raise an exception if there is insufficient stock at 'from_location'
                raise ValueError(f"stock is not avilable")
        except KeyError:
            # Raise an exception if the product is not available at 'from_location'
            raise ValueError(f"stock is not avilable")

    def display_details(self):
        print(self)
        print()


    @classmethod
    def print_stock_information(self,location_list, product_list):
        for location in location_list:
            print(f"{location.name}:")
            location_products = [product for product in product_list if location in product.stock_at_locations]
            for product in location_products:
                print(f"  {product.name} ({product.code}): {product.stock_at_locations[location]}")
            print()


class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.name} {self.code}"


class Movement:
    movements_list = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        Movement.movements_list.append(self)

    def __str__(self):
        return f"{self.from_location}  {self.to_location}  {self.product}  {self.quantity}"

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements_list if movement.product == product]

    @classmethod
    def print_product_movements(self,product):
        for product in product_list:
            movements = set(Movement.movements_by_product(product))
            print(f"Product: {product.name} ({product.code})")
            for movement in movements:
                print(f" {movement}")
            print()


# Creating categories
vehicle = Category("Duster", 1014)
car = Category("Bugatti", 1015, parent=vehicle)
petrol = Category("Caren", 1016, parent=car)
metro = Category("Hoster", 1017, parent=petrol)
railway = Category("Gloster", 1018, parent=metro)

# Creating locations
loc1 = Location("Ahmedabad", 2001)
loc2 = Location("Surat", 2002)
loc3 = Location("Junagadh", 2003)
loc4 = Location("Amreli", 2004)

# Creating products
product20 = Product("Product20", 1038, petrol, 500, {loc1: 50})
product21 = Product("Product21", 1039, petrol, 600, {loc2: 70})
product22 = Product("Product22", 1040, petrol, 300, {loc3: 45})
product23 = Product("Product23", 1041, petrol, 100, {loc4: 35})
product24 = Product("Product24", 1042, petrol, 900, {loc1: 40})
product_list= [product20, product21, product22, product23, product24]

location_list=[loc1,loc2,loc3,loc4]
# Displaying product details
print("--------------------------------------------display details------------------------------------------------------")
for product in product_list:
    product.display_details()

print("------------------------------------------------------------------------------------------------------------------")


# Moving products from one location to another
product20.move(loc1, loc2,10)
product21.move(loc2, loc3, 5)
product22.move(loc3, loc4, 15)
product23.move(loc4, loc1, 9)
product24.move(loc1, loc3, 8)

# Displaying movements of each product
print("-----------------------------------------updated stocks at locations -----------------------------------------------")
Product.print_stock_information(location_list,product_list)
print("--------------------------------------------movement all details----------------------------------------------------")
Movement.print_product_movements(product)
