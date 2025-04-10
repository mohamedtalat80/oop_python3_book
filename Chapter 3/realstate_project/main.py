def get_valid_input(prompt, valid_inputs):
    input_string = f" {prompt} ({'/'.join(valid_inputs)}): "
    response = input(input_string)
    while response not in valid_inputs:
        print("Invalid input.")
        response = input(input_string)
    return response

class Property:
    _id_counter = 0  # Class variable to track IDs
    avialable = None  # Class variable to track availability
    def __init__(self, square_feet="", bedrooms="", bathrooms="", **kwargs):
        super().__init__(**kwargs)
        Property._id_counter += 1
        self.property_id = Property._id_counter
        Property.avialable = True
        self.avialable = Property.avialable
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        
    def display(self):
        print("\nPROPERTY DETAILS")
        print("-----------------------")
        print(f"avaiable: {self.avialable}")
        print(f"Square Feet: {self.square_feet}")
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")
        
    @staticmethod
    def prompt_init():
        return {
            'square_feet': input("Enter the square feet: "),
            'bedrooms': input("Enter number of bedrooms: "),
            'bathrooms': input("Enter number of bathrooms: ")
        }

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")
    
    def __init__(self, balcony="", laundry="", **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print(f"Balcony: {self.balcony}")
        print(f"Laundry: {self.laundry}")
        
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        parent_init.update({
            'balcony': get_valid_input("Balcony?", Apartment.valid_balconies),
            'laundry': get_valid_input("Laundry facilities?", Apartment.valid_laundries)
        })
        return parent_init

class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    
    def __init__(self, num_stories="", garage="", fenced="", **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced
        
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print(f"Stories: {self.num_stories}")
        print(f"Garage: {self.garage}")
        print(f"Fenced: {self.fenced}")
        
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        parent_init.update({
            'num_stories': input("Enter number of stories: "),
            'garage': get_valid_input("Garage type?", House.valid_garage),
            'fenced': get_valid_input("Fenced yard?", House.valid_fenced)
        })
        return parent_init

class Purchase:
    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
        
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print(f"Price: ${self.price}")
        print(f"Taxes: ${self.taxes}")

    @staticmethod
    def prompt_init():
        return {
            'price': input("Purchase price: "),
            'taxes': input("Estimated taxes: ")
        }

class Rental:
    def __init__(self, rent="", utilities="", furnished="", **kwargs):
        super().__init__(**kwargs)
        self.rent = rent
        self.utilities = utilities
        self.furnished = furnished
        
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print(f"Rent: ${self.rent}/month")
        print(f"Utilities: {self.utilities}")
        print(f"Furnished: {self.furnished}")

    @staticmethod
    def prompt_init():
        return {
            'rent': input("Monthly rent: "),
            'utilities': input("Utilities included: "),
            'furnished': get_valid_input("Furnished?", ("yes", "no"))
        }

# Combined classes
class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

