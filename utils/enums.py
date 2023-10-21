from enum import Enum

class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

class SystemState(Enum):
    RUNNING = 2
    SUCCESS = 0
    FAILURE = 1


class AccountType(Enum):
    CHECKING = 1
    SAVING = 2

class TransactionType(Enum):
    WITHDRAW = 1
    DEPOSIT = 2