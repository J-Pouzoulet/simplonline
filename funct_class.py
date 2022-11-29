import pandas as pd

'''def open_csv(self):
    self.data_dict = pd.read_csv(f'{name}_data.csv', index_col=[0])
    self.money = data_dict['money']
    self.cane = data_dict['cane']

def write_csv(self):
    new_row = {'cane' : self.cane, 'money' : self.money}
    self.data_dict = data_dict.append(new_row, ignore_index=True)
    self.data_dict.to_csv(f'{name}_data.csv')'''



def buy_cane(self):
    print(f'How many cane would you like to buy?')
    number_of_cane = input()
    number_of_cane = float(number_of_cane)
    number_of_cane = round(number_of_cane)
    number_of_cane = int(number_of_cane)
    print(f'Please insert at least {number_of_cane*self.cane_price} euros')
    print(f'Enter your cash in:')
    cash_in = input()
    cash_in = float(cash_in)
    while cash_in < (number_of_cane*self.cane_price):
        print(f'I said AT LEAST {number_of_cane*self.cane_price} euros')
        print(f'Enter cash in')
        cash_in = input()
        cash_in = float(cash_in)
    self.cane = self.cane - number_of_cane
    self.money += number_of_cane * 1.5
    change = cash_in - number_of_cane * self.cane_price
    print(f'!!!Thanks for your purpchase!!!\nYour change is {change} euros')
    return self.money, self.cane

def load_cane(self):
    counter = 0
    print(f'password:')
    password = input()
    while password != "0000":
        if counter == 3:
            print(f'Password attempt failed')
            break
        else:
            print(f'!!! ACCESS DENIED !!!')
            print(f'password:')
            password = input()
            counter += 1
    if password == "0000":
        print('Welcome!\nHow many canes will you put in the distributor today?')
        self.cane += int(input())
        print(f"Would you like to collect the distributor's receipts?")
        answer3 = input()
        if answer3 == 'yes':
            self.money = 11.5
    return self.money, self.cane

def user_tech(self):
    self.data_dict = pd.read_csv('data.csv', index_col=[0])
    data = self.data_dict.iloc[-1]
    self.money = float(data[1])
    self.cane = float(data[0])
    print(f'Would you like to buy a drink today?\n yes or no:')
    answer1 = input()
    if answer1 == 'yes':
        self.buy_cane()
    else:
        print("Are you a technician, isn't it?\n yes or no:")
        answer2 = input()
        if answer2 == 'yes':
            self.load_cane()
        else:
            print(f"Sorry, I can't much for you...")

    self.data_dict = self.data_dict.append({'cane': self.cane, 'money' : self.money}, ignore_index=True)
    self.data_dict.to_csv('data.csv')
    return None
