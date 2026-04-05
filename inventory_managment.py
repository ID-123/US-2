products = []

def getInt():
    try:
        return int(input('> '))
    except ValueError:
        print('Invalid value, try again.')
        return getInt()
    
def getFloat():
    try:
        return float(input('> '))
    except ValueError:
        print('Invalid value, try again.')
        return getFloat()
    
def addProduct():
    
    name = input('Product name \n> ')
    print('Product price')
    price = getFloat()
    print('Product quantity')
    quantity = getInt()

    new_product = {'name': name,'price': price,'quantity': quantity}
    products.append(new_product)
    print('Added successfully.')

def listProducts():
    if len(products) == 0:
        print('Inventory currently empty.')
        return
    
    for product in products:
        print(f'Name: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}')

def stadistics():
    if len(products) == 0:
        print('Inventory currently empty.')
        return
    
    choice = input('What do you want to do? \n1. Check total inventory \n2. Calculate total inventory value \n> ') 
    if choice == '1':
        total_quantity = 0
        for product in products:
            print(f'Product: {product['name']} | Quantity: {product['quantity']}')
            total_quantity += product['quantity']
        print(f'Total inventory quantity: {total_quantity}')

    elif choice == '2':
        total_value = 0
        for product in products:
            print(f'Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}, Value: {product['price'] * product['quantity']}')
            total_value += product['price'] * product['quantity']
    
        print(f'Total inventory value: {total_value}')

    else:
        print('Invalid choice, try again.')
        stadistics()

def main_menu():
    print('''
        --< Inventory Management >--
        1. Add product
        2. List products
        3. Inventory statistics
        4. Exit
          ''')
    choice = input('> ')
    if choice == '1':
        addProduct()
    elif choice == '2':
        listProducts()
    elif choice == '3': 
        stadistics()
    elif choice == '4':
        print('Goodbye.')
        return
    else:
        print('Invalid choice, try again.')
    if choice != '4':
        main_menu()

main_menu()