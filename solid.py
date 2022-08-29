from abc import ABC, abstractmethod


class Order:
    '''
    a class for orders
    '''
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_items(self, name, quantity, price):
        self.items.append((name))
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] + self.prices[i]
        return total


class Authorizer(ABC):
    '''an abstract class for authorizer'''

    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    '''A class for sms authorizing'''

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f'Verifying SMS code {code}')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):
    '''a class for checking if you are a robot or not'''

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        print('Are you a robot? Nope')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    '''
    1. Single Responsibility Principle
       Order class should not have payment function defined in it.
    2. Open/Closed Principle
       should be open, so that when you need to add a new form of payment,
       we don't need to change the whole paymentprocessor every single time.
    3. Liskov Subsitution Principle
       should not valid this as it is best for case by case. So, you don't
       have to change parameters for different use cases.
    4. Intergration Segregation
       don't want a general interface, split it up, use compositions better too
    5. Dependency Inversion
    '''

    @abstractmethod
    def pay(self, orders):
        pass


class DebitpaymentProcessor(PaymentProcessor):
    '''a sub paymentprocess class for debit'''

    def __init__(self, security_code, authorizr: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizr

    def pay(self, orders):
        if not self.authorizer.is_authorized():
            raise Exception('Not Authorized')
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        orders.status = 'Paid'
        print(f'Order Status: {orders.status}')


class CreditPaymentProcessor(PaymentProcessor):
    '''a sub paymentprocess class for credit'''

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, orders):
        print('Processing debit payment type')
        print(f'Verifying security code: {self.security_code}')
        orders.status = 'Paid'
        print(f'Order Status: {orders.status}')


class PaypalPaymentProcessor(PaymentProcessor):
    '''a sub paymentprocess class for Paypal'''

    def __init__(self, email_address, authorizr: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizr

    def pay(self, orders):
        if not self.authorizer.is_authorized():
            raise Exception('Not Authorized')
        print('Processing debit payment type')
        print(f'Verifying email address: {self.email_address}')
        orders.status = 'Paid'
        print(f'Order Status: {orders.status}')


order = Order()
order.add_items('Keyboard', 1, 50)
order.add_items('SSD', 1, 150)
order.add_items('USB cable', 2, 5)

print(order.total_price())
authorizer = NotARobot()
authorizer.not_a_robot()
processor = PaypalPaymentProcessor('wesley.shih@sjsu.edu', authorizer)
processor.pay(order)
