from aiogram.dispatcher.filters.state import State, StatesGroup

class kursgaYozilish(StatesGroup):
    yolovchi = State()
    odam = State()
    teleraqam = State()
    check = State()

class taxi(StatesGroup):
    fio = State()
    teleraqam = State()
    check = State()