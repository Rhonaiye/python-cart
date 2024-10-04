foods = []
prices = []

        
             
def cart():
    total = 0
    try:
       while True:
           food = input('input a food to buy (q to quit): ')
        
           if food.isdigit() :
              print('put a valid food name')
        
           if(food.lower() == 'q'):
              break
        
           price = float(input(f'input the price of a {food}: $ '))
        
           foods.append(food)
           prices.append(price)
        
    except ValueError as e:
        print(e)
    
    
    print('-----Your cart-----')
    print(' Items')
    
    for food in foods:
        print(food)
        
    for price in prices:
        total += price
    print(' ')
    print(f'Your total is ${total}')
    
    print('-----End of Cart-----')
    
cart()
