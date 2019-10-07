class Product:
    def __init__(self, name, price=-1):
        self.name = name
        self.price = price

    def __str__(self):
        return 'Product: {}, Price: ${}'.format(self.name,self.price)
    
    def get_csv_format(self):
        return '{}\t{}\n'.format(self.name, self.price)