class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        ''' accepts an amount and an optional description '''
        self.ledger.append({
                   'amount':amount,
                   'description': description})
    
    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction["amount"]
        return total
    
    def withdraw(self, amount, description=''):
        if amount <= self.get_balance():
            self.ledger.append({
                "amount":-amount,
                "description":description})
            return True
        return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def __str__(self):
        output = self.name.center(30, "*") + "\n"

        for entry in self.ledger:
            description = entry["description"][:23]
            amount = entry["amount"]
            output += f"{description:<23}{amount:>7.2f}\n"

        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    output = "Percentage spent by category\n"

    # policzenie wydatków
    spends = []

    for category in categories:
        total_spend = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                total_spend += abs(transaction["amount"])

        spends.append(total_spend)

    # suma wszystkich wydatków
    total = sum(spends)

    # procenty zaokrąglone do dziesiątek
    percentages = []

    for spend in spends:
        percentages.append(int((spend / total) * 100) // 10 * 10)


    # wykres od 100 do 0
    for number in range(100, -1, -10):
        output += f"{number:>3}| "

        for percentage in percentages:
            if percentage >= number:
                output += "o  "
            else:
                output += "   "

        output += "\n"


    # linia pod wykresem
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"


    # nazwy kategorii pionowo
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += "     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i] + "  "
            else:
                output += "   "

        if i != max_length - 1:
            output += "\n"

    return output

# # --- TEST CODE 1 ---
# food = Category('Food')

# print("\n")

# food.deposit(1000, 'initial deposit')

# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50,clothing)

# print(food)

# animal = Category('Animal')
# animal.deposit(900, 'initial deposit')
# animal.withdraw(10.1, 'groceries')
# animal.withdraw(15.99, 'restaurant and more food for dessert')
# print(create_spend_chart([food,animal]))



