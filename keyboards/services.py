from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

services = [
    "Диагностика автокондиционера",
    "Заправка автокондиционера",
    "Диагностика отопителя",
    "Ремонт отопителя",
    "Установка отопителя",
    "Дезинфекция салона",
    "Другое"
]

def get_services_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=s, callback_data=f"service:{s}")] for s in services
        ]
    )
