class property(property):
    def __init__(self,prop_id,address,price,sqm):
        self.prop_id = prop_id
        self.address = address
        self.price = price
        self.sqm = sqm

class apartment(property):
    def __init__(self,prop_id,address,price,sqm,floor_level):
     super().__init__(prop_id,address,price,sqm)
     self.floor_level=floor_level
    def get_actual_area(self):
        return self.sqm*1.05
    def display_listing(self):
        print(f"[APT] ID: {self.prop_id} | "
              f"Floor {self.floor_level} | "
              f"{self.address} | "
              f"{self.price}B VND | "
              f"Area: {self.get_actual_area()} sqm")

class villa(property):
    def __init__(self,prop_id,address,price,sqm,floor_level,has_pool):
        super().__init__(prop_id, address, price, sqm)
        self.floor_level = floor_level
        self.has_pool = has_pool
    def caculate_maintainance(self):
        return self.price*0.0005

    def add_pool(self):
        self.has_pool = True

    def display_listing(self):
        print(f"[VILLA] ID: {self.prop_id} | "
              f"Floor {self.floor_level} | "
              f"{self.address} | "
              f"{self.price} billion vnd | "
              f"pool: {self.has_pool} "
              f"monthly maintainenace fee : {self.caculate_maintainance()}billion vnd")

class penthouse(property):
    def __init__(self,prop_id,address,price,sqm,has_private_elevator):
        super().__init__(prop_id, address, price, sqm)
        self.has_private_elevator = has_private_elevator
    def  get_taxed_price(self):
        return self.price*1.1

    def display_listing(self):
        print(f"[PENTHOUSE] ID: {self.prop_id} | "
              f"Private Elevator: "
              f"{self.has_private_elevator} | "
              f"Total Price: "
              f"{self.get_taxed_price()} billion vnd")

market_dashboard = [

    apartment(
        201,"Ocean Park, Gia Lam",3.1,55,15
    ),
    apartment(
        202,"Masteri Thao Dien",4.5,70,20
    ),
    villa(
        301,"Vinhomes Riverside",35.0,300,2,True
    ),
    villa(
        302,"Phu My Hung Villa",28.0,250,3,False
    ),
    penthouse(
        401,"Keangnam Landmark 72",15.5,250,True
    ),
    penthouse(
        402,"Bitexco Residence",18.0,280,False
    )
]
def generate_market_report(listings):

    total_market_value = 0

    print("====== MARKET REPORT ======\n")

    for property_item in listings:

        property_item.display_listing()

        total_market_value += property_item.price

        print()
    print("====== SUMMARY ======")
    print(f"Total Market Value: "
          f"{total_market_value} billion VND")
generate_market_report(market_dashboard)

def villa_inspection(listings):
    for property_item in listings:
        if isinstance(property_item, villa):
            print(f"--- Inspection Required for "
                  f"Pool at Property "
                  f"{property_item.prop_id} ---")
        else:
            print(f"--- Property "
                  f"{property_item.prop_id} "
                  f"does not require "
                  f"pool inspection ---")

for property_item in market_dashboard:

    if isinstance(property_item, villa):

        if property_item.has_pool == False:

            print("=== BEFORE ADDING POOL ===")
            property_item.display_listing()

            # add pool
            property_item.add_pool()

            print("\n=== AFTER ADDING POOL ===")
            property_item.display_listing()
villa_inspection(market_dashboard)
penthouse1=penthouse( 401, "Keangnam Landmark 72", 15.5, 250, True)
villa1=villa( 301, "Vinhomes Riverside", 35.0, 300,2, True)
apt= apartment (201, "Ocean Park, Gia Lam", 3.1, 55, 15)
apt.display_listing()
villa1.display_listing()
penthouse1.display_listing()
