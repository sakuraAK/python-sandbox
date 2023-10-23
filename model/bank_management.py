import abc
import uuid
from abc import  ABC
from datetime import datetime
import asyncio

from utils.enums import AccountType
from utils.enums import TransactionType

class Account:
    INIT_ACC_NUMBER = 1000000
    def __init__(self, balance):
        Account.INIT_ACC_NUMBER += 1
        self._acc_number = Account.INIT_ACC_NUMBER
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

class CheckingAccount(Account):
    pass

class SavingAccount(Account):
    pass



class Client:
    INIT_CLIENT_NUMBER = 1000000
    def __init__(self, name, pin: int):
        self.name = name
        self.client_number = Client.INIT_CLIENT_NUMBER
        Client.INIT_CLIENT_NUMBER += 1
        self.pin = pin
        self._accounts = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()

    @property
    def client_number(self):
        return self._client_number

    @client_number.setter
    def client_number(self, value):
        self._client_number = value

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        self._pin = Bank.super_secure_hash(str(value))

    def get_accounts(self) -> dict:
        return self._accounts


class WebUser:
    def __init__(self, user_id: str, pwd: str):
        self.user_id = user_id
        self.password = pwd



    @property
    def user_id(self):
        return self._user_id
    @user_id.setter
    def user_id(self, value: str):
        self._user_id = value

    @property
    def password(self):
        return self._pwd


    @password.setter
    def password(self, value):
        self._pwd = Bank.super_secure_hash(value)

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    def get_accounts(self) -> dict:
        if self.client:
            return self.client.get_accounts()
        return None

class Transaction(ABC):
    def __init__(self, type, amount):
        self._type = type
        self._amount = amount
        self._date = datetime.utcnow().now()

class WebTransaction(Transaction):
    pass

class ATMTransaction(Transaction):
    pass



'''
Interface every bank that provides services should implement
'''
class BankingService(ABC):
    @abc.abstractmethod
    def authenticate(self, user_id: str, pwd: str) -> str:
        pass

    @abc.abstractmethod
    def authenticate(self, client_number: int, pin: int) -> str:
        pass

    @abc.abstractmethod
    def withdraw(self, amount: float, token: str, acc_type=AccountType.CHECKING):
        pass

    @abc.abstractmethod
    def deposit(self, amount: float, token: str, acc_type=AccountType.CHECKING):
        pass

    @abc.abstractmethod
    def get_balance(self, token, acc_type=AccountType.CHECKING) -> float:
        pass
    @abc.abstractmethod
    def quit(self):
        pass

class Bank(BankingService):

    def __init__(self, name, code, address):
        self._name = name
        self._code = code
        self._address = address
        self._clients = {}
        self._web_clients = {}
        self._session = {}



    def authenticate(self, user_id: str, pwd: str) -> str:
        if user_id in self._web_clients.keys() \
                and Bank.super_secure_hash(pwd) == self._web_clients[user_id].password:
            token = uuid.uuid4().hex
            self._session[token] = self._web_clients[user_id]
            return token
        return None


    # def authenticate(self, client_number: int, pin: int) -> str:
    #     if client_number in self._clients \
    #         and self._clients[client_number].pin == Bank.super_secure_hash(pin):
    #         token = uuid.uuid4().hex
    #         self._session[token] = self._clients[client_number]
    #         return token

    def add_client(self, name: str, pin: int) -> Client:
        new_client = Client(name, pin)
        self._clients[new_client.client_number] = new_client
        return new_client

    def add_web_user(self, client_number: int, user_id: str, pwd: str) -> bool:
        if client_number in self._clients.keys():
            client = self._clients[client_number]
            new_web_user = WebUser(user_id, pwd)
            new_web_user.client = client
            self._web_clients[user_id] = new_web_user
            return True
        return False

    def add_account(self, client_number: int, account_type: AccountType) -> bool:
        if client_number not in self._clients:
            return  False
        cur_client_accounts = self._clients[client_number].get_accounts()
        if account_type in cur_client_accounts.keys():
            return False
        if account_type == AccountType.CHECKING:
            cur_client_accounts[account_type] = CheckingAccount(0)
        elif account_type == AccountType.SAVING:
            cur_client_accounts[account_type] = SavingAccount(0)
        else:
            raise Exception('Unsupported account type')

    def withdraw(self, amount: float, token: str, acc_type=AccountType.CHECKING):
        if amount <= 0:
            raise Exception("Wrong amount")
        if token not in self._session.keys():
            raise Exception("Unauthorized")
        client = self._session[token]
        if client.get_accounts() is None or acc_type not in client.get_accounts().keys():
            raise Exception(f"Client does not have {acc_type.name}")
        account = client.get_accounts()[acc_type]
        if amount > account.balance:
            raise Exception("Insufficient funds")
        account.balance -= amount
        self._create_transaction(account, TransactionType.WITHDRAW)

    def deposit(self, amount: float, token: str, acc_type=AccountType.CHECKING):
        if amount <= 0:
            raise Exception("Wrong amount")
        if token not in self._session.keys():
            raise Exception("Unauthorized")
        client = self._session[token]
        if client.get_accounts() is None or acc_type not in client.get_accounts().keys():
            raise Exception(f"Client does not have {acc_type.name}")
        account = client.get_accounts()[acc_type]
        account.balance += amount
        self._create_transaction(account, TransactionType.DEPOSIT)


    def get_balance(self, token, acc_type=AccountType.CHECKING) -> float:
        if token not in self._session.keys():
            raise Exception("Unauthorized")
        client = self._session[token]
        if acc_type not in client.get_accounts().keys():
            raise Exception(f"Client does not have {acc_type.name}")
        account = client.get_accounts()[acc_type]
        return account.balance

    def _create_transaction(self, account: Account, tr_type: TransactionType):
        pass




    def quit(self, token):
        if token in self._session.keys():
            del self._session[token]

    def get_all_clients(self):
        return self._clients.values()

    @staticmethod
    def super_secure_hash(plain_pwd: str) -> str:
        # todo: provide implementation for encrypted hash
        return plain_pwd


'''
Example of banking service usage within web application
First we setting up the client and the account. This part is out
of scope of our UML.
'''
if __name__ == '__main__':
    # First we set up client and the account to be used
    # This part of the code is out of the scope of our UML
    service = Bank('FNBU', '1000', 'Nowhere in particular')
    new_client = service.add_client('John Doe', 1234)
    user_id = "JohnDoe"
    pwd = "StrongPassword123"
    service.add_web_user(new_client.client_number, user_id, pwd)
    service.add_account(new_client.client_number, AccountType.CHECKING)

    #deposit example
    token = service.authenticate(user_id, pwd)
    if token != None:
        service.deposit(1000, token, AccountType.CHECKING)
        print(f"Hi {user_id} your new balance is {service.get_balance(token, AccountType.CHECKING)}")
        service.quit(token)

