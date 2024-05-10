class Customer:
    def __init__(self,cust_id,name,shipping_city,shipping_country,billing_city,billing_country):
        self.cust_id = cust_id
        self.name = name
        self.shipping_address = self.Address(shipping_city,shipping_country)
        self.billing_address = self.Address(billing_city,billing_country)
        
        
    class Address:
        def __init__(self,city,country):
            self.city = city
            self.country = country
        
        def display(self):
            print(self.city)
            print(self.country)
        
        
customer_c1 = Customer(1,'Rishabh','Allahabad','India','Bangalore','India')
customer_c1.shipping_address.display()
customer_c1.billing_address.display()
