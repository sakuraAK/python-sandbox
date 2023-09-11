from utils.enums import DayOfWeek, SystemState
from datetime import datetime

day_of_week = datetime.now().isoweekday()

if day_of_week == DayOfWeek.WEDNESDAY.value:
    print(f"Today is {DayOfWeek.WEDNESDAY.name}")
print(DayOfWeek(day_of_week).name)

def get_state(code: int) -> SystemState:
    print(f"Process status: {SystemState(code).name}")

get_state(0)