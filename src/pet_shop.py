# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]  

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, sold):
    pets_sold["admin"]["pets_sold"] += sold
    


# def test_increase_pets_sold(self):
#         increase_pets_sold(self.cc_pet_shop,2)
#         sold = get_pets_sold(self.cc_pet_shop)
#         self.assertEqual(2, sold)
