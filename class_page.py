#Create A Class That Stores The Table Class
class table:
    def __init__(self , table = None , customer = None , order=list() ,waiter=None, items_sold = 0, total_sales_made = 0.0):
        self.table = table
        self.customer = customer
        self.order = order
        self.waiter = waiter
        self.total_sale = total_sales_made;
        self.items_sold = items_sold
    #Define The Values once the class is defined

    def Add_customer(self , customer_name = None):
        self.customer = customer_name
    #Function To Change The Customer Names

    def reset_order(self,order=[]):
        self.order = order
    #Function To Reset The Orders To Nothing

    def change_table(self,table = None):
        self.table = table
    #Function To Change The Table

    def change_waiter(self,waiter = None):
        self.waiter = waiter
    #Function To Change The Waiter

    def append_order(self,data):
        array_list = self.order
        array_list.append(data)
        self.order = array_list;

    def reset_orders(self, new_list=[]):
        self.order = new_list

    def reset_customer(self, customer = None):
        self.customer = customer
