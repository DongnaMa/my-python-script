class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisibe_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisibe_type.title())
    def open_restaurant(self):
        print(self.restaurant_name+" is opening")

my_restaurant = Restaurant('KFC', 'Burger')
print("My favorite restaurant is "+my_restaurant.restaurant_name+".")
print("Type of cooking in this restaurant is "+my_restaurant.cuisibe_type+".")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()