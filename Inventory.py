import pandas as pd #This will convert list to dataframes
names= ["Phones", "Laptops"]
prices= [899, 1299 ]
quantities= [39, 34]
stock_list= pd.DataFrame(list(zip(names, prices, quantities))   #This converts the above lists to a dataframe
                             , columns =['Product', 'Price', 'Quantity'])

holiday_discount = ["15% off on Christmas", "10% off on Easter"]

def main(): #This is the main method
    #this displays a list of options/commands a user can choose
    print("Type ---Add--- to add new products")
    print("Type ---Search--- to search for products")
    print("Type ---Edit--- to search for products")
    print("Type ---Exit--- to exit")

#This method returns user to main
def home():
    return main()


class Tech:
    #A list of the class methods
    _popular_colors = ["Black", "White", "Silver", "Rose"] 
    _popular_brands = ["Apple", "Samsung", "Huawei", "Microsoft"]
    _chargers = ["wireless", "wired"]
    _holiday_discount = ["15% off on Christmas", "10% off on Easter"]
    
    #This will assign values to objects
    def __init__(self, names, prices, quantities):
        self.names= [] 
        self.prices= []
        self.quantities= []
    
    #Class methods    
    @classmethod 
    def holiday_discount(cls, *args): 
        return cls._holiday_discount
    @classmethod
    def popular_colors(cls):
        return cls._popular_colors
    
    @classmethod
    def popular_brands(cls):
        return cls._popular_brands
    
    @classmethod
    def chargers(cls):
        return cls._chargers

running = True #This will allow the while loop to run

#This loop will take commands and execute them based on the user's options
if __name__ == "__main__":
    main()

while running: 
    print("Type")
    next_option = input("Pick an option:  ")                  #Allows the user to choose Add, Search, Delete, or Edit
    if next_option == "Exit" or next_option == "exit":
        running= False     #exits the loop if user types exit
    #Allows user to add products
    elif next_option == "Add" or next_option == "add":
        name= input("Enter the name of the product you would like to add: ")
        if name in names:
            print("Product in stock")
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option")   
        else:
            price= input("Enter product's price: ")
            quantity= input("Enter the product quantity: ")
            discount= input("Enter Christmas or Easter or None: ")
            if (discount == "Christmas"):
                holiday_discount= holiday_discount[0]
                print(holiday_discount)
            elif (discount == "Easter"):
                holiday_discount= holiday_discount[1]
                print (holiday_discount)
            else:
                print("No discount")  
            new_product= Tech(name, price, quantity)   #Adds the new object to the class
            #inserts details to the respective lists
            names.insert(0, name)      
            prices.insert(0, price)
            quantities.insert(0, quantity)
            new_product_series= pd.Series([name, price, quantity], index=stock_list.columns)  #converts inputs to a series
            #adds the above series to a row in the dataframe
            stock_list= stock_list.append(new_product_series, ignore_index=True)
            print("Product has been added")
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option")
    #Searchs for products
    elif next_option == "Search" or next_option == "search":
        name= input("Enter product name to view its details: ")
        if name in names:
            print(stock_list[stock_list['Product'] == name]) #This gets product details from the stock list
            print("Popular brands \n", Tech("","","").popular_brands())
            print("Popular colors \n", Tech("","","").popular_colors())
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option")
        else:
            print("Product not in stock")
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option") 
    #Allows editing of product details
    elif next_option == "Edit" or next_option == "edit":
        name= input("Enter the name of the product you would like to edit: ")
        if name in names:
            new_name= input("Enter the new name of the product: ")
            new_price= input("Enter product's new price: ")
            new_quantity= input("Enter the product's new quantity: ")
            #Creates new row in stock list
            new_row = pd.DataFrame({"Product":new_name, "Price":new_price, 'Quantity':new_quantity,},index =[0])
            # adds row to dataframe
            stock_list = pd.concat([new_row, stock_list]).reset_index(drop = True)
            deleted = stock_list["Product"] != name  #Deletes replaced product
            stock_list= stock_list[deleted] #updates stock_list
            print("Product edited successfully \n", stock_list)  
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option")   
        else:
            print("Product not in stock")   
            next_option= input("Type ----Home---- to go back to main menu: ")
            if next_option == "Home" or next_option == "home":
                home()
            else:
                print("invalid option")
if len(names) == 100:   #Limits the number of products in stock
    print('Congratulations! Your stock is full', Tech("","","").popular_brands(), 
          Tech("","","").popular_colors(), Tech("","","").holiday_discount())
    running= False

