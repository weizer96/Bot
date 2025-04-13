from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

def get_time_keyboard(date: datetime):
    weekday = date.weekday()
    times = []

    if weekday == 6:
        return None  # Sunday — no buttons
    elif weekday == 5:
        times = [f"{h}:00" for h in range(9, 14)]
    else:
        times = [f"{h}:00" for h in range(9, 17)]

    keyboard = [
        [InlineKeyboardButton(text=t, callback_data=f"time:{t}")] for t in times
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
