import random
import time

class Stonk:
    MAX_SYM_LEN = 4

    def __init__(self, shares):
        self.shares = shares
        self.symbol = self._generate_symbol()
        self.next = None

    def _generate_symbol(self):
        AI_symbol_len = random.randint(1, Stonk.MAX_SYM_LEN)
        return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=AI_symbol_len))

class Portfolio:
    def __init__(self):
        self.money = random.randint(1, 2018)
        self.head = None

    def view_portfolio(self):
        print("\nPortfolio as of", time.ctime())
        print("\n")
        head = self.head
        if not head:
            print("You don't own any stonks!")
        while head:
            print(f"{head.shares} shares of {head.symbol}")
            head = head.next

    def pick_symbol_with_AI(self, shares):
        if shares < 1:
            return None
        return Stonk(shares)

    def buy_stonks(self):
        print("Using patented AI algorithms to buy stonks")
        while self.money > 0:
            shares = random.randint(1, self.money)
            stonk = self.pick_symbol_with_AI(shares)
            stonk.next = self.head
            self.head = stonk
            self.money -= shares
        print("Stonks chosen")

        # Read the token from user input
        user_buf = input("What is your API token?\n")
        print(f"Buying stonks with token:\n{user_buf}")

        self.view_portfolio()

def main():
    random.seed(time.time())
    p = Portfolio()

    print("Welcome back to the trading app!\n\n")
    print("What would you like to do?")
    print("1) Buy some stonks!")
    print("2) View my portfolio")
    resp = int(input())

    if resp == 1:
        p.buy_stonks()
    elif resp == 2:
        p.view_portfolio()

    print("Goodbye!")

if __name__ == "__main__":
    main()
