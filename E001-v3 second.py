class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []


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
                new_movement = Movement(from_location, to_location, self, quantity)
                Movement.movements_list.append(new_movement)

                self.stock_at_locations[from_location] -= quantity

                if to_location in self.stock_at_locations:
                    self.stock_at_locations[to_location] += quantity
                else:
                    self.stock_at_locations[to_location] = quantity

                print(f"Moved {quantity}  of {self.name} from {from_location.name} to {to_location.name}")
            else:
                raise ValueError(f"Stock is not available")
        except KeyError:
            raise ValueError(f"Product is not available at the source location")

    def display_details(self):
        print(f"Product Name: {self.name} ({self.code})")
        print(f"Category: {self.category.name}")
        print(f"Price: {self.price}")
        print(f"Stock at Locations: {self}")
        print()

    @staticmethod
    def print_stock_information(location_list, product_list):
        for location in location_list:
            print(f"{location.name} ({location.code}):")
            for product in product_list:
                if location in product.stock_at_locations:
                    print(f"  {product.name} ({product.code}): {product.stock_at_locations[location]}")
            print()

    @classmethod
    def input_user(ssss, product_list, location_list):
        for product in product_list:
            from_location_code = input(f"Enter source location code for {product.name}: ")
            to_location_code = input(f"Enter destination location code for {product.name}: ")
            quantity_to_move = int(input(f"Enter quantity to move for {product.name}: "))
            # Find source location
            from_location = next(loc for loc in location_list if loc.code == int(from_location_code))
            # Find destination location
            to_location = next(loc for loc in location_list if loc.code == int(to_location_code))
            # Move stocks
            product.move(from_location, to_location, quantity_to_move)

        # Display updated stocks in each location
        print("--------------------------------------Updated stocks by location --------------------------------------")
        for location in location_list:
            print(f"{location.name} ({location.code}):")
            for product in product_list:
                if location in product.stock_at_locations:
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
        return f" From_location :{self.from_location} to_location: {self.to_location}  product_details: {self.product}  Quantity add: {self.quantity}"

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements_list if movement.product == product]


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
product24 = Product("Product24", 1042, petrol, 900, {loc2: 40})

product_list = [product20, product21, product22, product23, product24]
location_list = [loc1, loc2, loc3, loc4]


# Displaying product details
print("---------------------display details stock at various location---------------------------------------")
for product in product_list:
    product.display_details()

print()
# Display stocks in each location
Product.print_stock_information(location_list, product_list)
# Call the input_user method
Product.input_user(product_list, location_list)


