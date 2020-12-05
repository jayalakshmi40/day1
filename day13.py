choice = input("what would you like to have?\n1.Espresso\n2.latte\n3.cappuccino") 
report=input("If you want to print the report?\n1.Yes\n2.No")
resource_water = 3000
resource_milk = 2000 
resource_coffee = 500 
if choice== '1':
    def Espresso (resource_water,resource_coffee):
        resource_water -= 50
        resource_coffee -= 15
        print("The available amount of water",resource_water)
        print("The available amount of coffee",resource_coffee)
        if report=='1':
                        print("water: 50ml\ncoffee: 15g\namount: $2")
        else:
            passchoice = input("what would you like to have?\n1.Espresso\n2.latte\n3.cappuccino") 
            report=input("If you want to print the report?\n1.Yes\n2.No")
            resource_water = 3000
            resource_milk = 2000 
            resource_coffee = 500
    x=Espresso(resource_water,resource_coffee)
elif choice == '2':
    def latte (resource_coffee, resource_water, resource_milk):
        resource_water -= 25    
        resource_milk -= 30 
        resource_coffee -= 20   
        print("The available amount of water",resource_water)
        print("The available amount of milk",resource_milk) 
        print("The available amount of coffee",resource_coffee) 
        if report=='1':
            print("water:25ml\nmilk:30ml\ncoffee:20g,amount:$3")
    y = latte (resource_coffee, resource_milk, resource_water)
elif choice=='3':
    def cappuccino(resource_water,resource_milk,resource_coffee):
        resource_coffee-=10
        resource_milk-=30
        resource_water-=25
        if report=='1':
            print("water:25ml\nmilk:30ml\ncoffee:10g,amount:$3.5")
            print("The available amount of water",resource_water)
            print("The available amount of milk",resource_milk)
            print("The available amount of coffee",resource_coffee)
    z= cappuccino (resource_water,resource_milk,resource_coffee)
else:
    print("Resource is unavailable")
class payment:
    def process_coins():
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        x=round(total,5)
        print(x)
        return x
    y=process_coins()
    def transaction(choice,y):
        if choice=='2':
            if y=='2':
                print("Transaction successful")
            else:
                print("enter the correct amount")
        if choice=='2':
            if y=='3':
                print("Transaction successful")
            else:
                print("enter the correct amount")
        if choice=='3':
            if y=='3.5':
                print("Transaction successful")
            else:
                print("enter the correct amount")
    z=transaction(choice,y)
status=input("enter the status of the machine1.continue\n2.stop")