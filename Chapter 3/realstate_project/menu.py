from main import *  # Assuming all property classes are imported correctly

class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("apartment", "rental"): ApartmentRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "purchase"): ApartmentPurchase
    }
    
    def __init__(self):
        self.property_list = []
    
    def display_properties(self, show_all=True):
        """Display all properties in the list"""
        if not self.property_list:
            print("No properties available.")
            return
            
        print("\n=== PROPERTY LIST ===")
        for prop in self.property_list:
            prop.display()
            print("========================")
    
    def add_property(self):
        """Add a new property to the list"""
        try:
            prop_type = get_valid_input("Property type?", ("house", "apartment"))
            trans_type = get_valid_input("Transaction type?", ("rental", "purchase"))
            
            PropertyClass = self.type_map[(prop_type, trans_type)]
            init_args = PropertyClass.prompt_init()
            new_property = PropertyClass(**init_args)
            self.property_list.append(new_property)
            print(f"\nProperty {new_property.property_id} added successfully!")
        except Exception as e:
            print(f"\nError adding property: {str(e)}")
    
    def remove_property(self, property_id):
        """Remove a property by ID"""
        try:
            property_id = int(property_id)
            for i, prop in enumerate(self.property_list):
                if prop.property_id == property_id:
                    del self.property_list[i]
                    print(f"\nProperty {property_id} removed successfully.")
                    return
            print(f"\nProperty {property_id} not found.")
        except ValueError:
            print("\nInvalid property ID. Please enter a number.")
    
    def find_property(self, property_id):
        """Find and return a property by ID"""
        try:
            property_id = int(property_id)
            for prop in self.property_list:
                if prop.property_id == property_id:
                    return prop
            return None
        except ValueError:
            print("\nInvalid property ID. Please enter a number.")
            return None
    
    def mark_unavailable(self, property_id):
        """Mark a property as unavailable"""
        try:
            property_id = int(property_id)
            prop = self.find_property(property_id)
            if prop:
                if hasattr(prop, 'available'):
                    prop.available = False
                    print(f"\nProperty {property_id} marked as unavailable.")
                else:
                    print("\nThis property type doesn't support availability status.")
            else:
                print(f"\nProperty {property_id} not found.")
        except ValueError:
            print("\nInvalid property ID. Please enter a number.")


class Menu(Agent):
    def __init__(self):
        super().__init__()
        self.menu_options = {
            '1': ('Add Property', self.add_property),
            '2': ('Remove Property', self._remove_property_handler),
            '3': ('Display Properties', self.display_properties),
            '4': ('Find Property', self._find_property_handler),
            '5': ('Mark Property Unavailable', self._mark_unavailable_handler),
            '6': ('Exit', self._exit_program)
        }
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n=== REAL ESTATE AGENT MENU ===")
        for key, (description, _) in self.menu_options.items():
            print(f"{key}. {description}")
    
    def _remove_property_handler(self):
        """Handle property removal input"""
        property_id = input("Enter property ID to remove: ")
        self.remove_property(property_id)
    
    def _find_property_handler(self):
        """Handle property search input"""
        property_id = input("Enter property ID to find: ")
        prop = self.find_property(property_id)
        if prop:
            print("\n=== PROPERTY FOUND ===")
            prop.display()
        else:
            print(f"\nProperty {property_id} not found.")
    
    def _mark_unavailable_handler(self):
        """Handle marking property as unavailable"""
        property_id = input("Enter property ID to mark as unavailable: ")
        self.mark_unavailable(property_id)
    
    def _exit_program(self):
        """Exit the program"""
        print("\nThank you for using the Real Estate Agent System. Goodbye!")
        exit()
    
    def run(self):
        """Run the main menu loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice in self.menu_options:
                _, action = self.menu_options[choice]
                action()
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    try:
        menu = Menu()
        menu.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting...")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")