from aiogram.fsm.state import State, StatesGroup


class Food707(StatesGroup):
    state_menyu = State()
    state_taomlar = State()
    state_ichimliklar = State()
    state_soni = State()
