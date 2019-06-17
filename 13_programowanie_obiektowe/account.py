class Account:

    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      self.__account_number = '12 4530 0000 1001 2345 3213'
      self.__money = 100

    def show_number(self):
        print("Current account number: {}".format(self.__account_number))

    def set_new_number(self, number):
        self.__account_number = number

    def show_money(self):
        print('this is your money ' + str(self.__money))

    def add_money(self):
        money = input('how much money you want to add?:')
        self.__money = self.__money + int(money)
        print(self.__money)

    def pay(self):
        money = input('how much you need to pay?:')
        self.__money = self.__money - int(money)
        print(self.__money)


user = Account('Maria', 'Kowalczyk')
user.show_number()


user.set_new_number('35 0000 0000 0001 0000 7777')
user.show_number()

user.show_money()
user.add_money()
user.pay()