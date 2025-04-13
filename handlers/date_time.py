from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from states import BookingStates
from datetime import datetime
from keyboards.time import get_time_keyboard

router = Router()


@router.message(BookingStates.choosing_date)
async def choose_date(message: Message, state: FSMContext):
    try:
        date = datetime.strptime(message.text, "%d.%m.%Y")
        keyboard = get_time_keyboard(date)
        if not keyboard:
            await message.answer("🗓️ Воскресенье — выходной. Выберите пожалуйста другую дату.")
            return
        await state.update_data(date=message.text)
        await message.answer(f"✅ Вы выбрали дату: {message.text}")
        await message.answer("🕒 Выберите время:", reply_markup=keyboard)
        await state.set_state(BookingStates.choosing_time)
    except ValueError:
        await message.answer("📅 Введите дату корректно, в формате ДД.ММ.ГГГГ")


@router.callback_query(F.data.startswith("time:"))
async def choose_time(callback: CallbackQuery, state: FSMContext):
    time = callback.data.split(":")[1]
    await state.update_data(time=time)
    await callback.message.edit_text(f"✅ Вы выбрали время: {time}:00")
    await callback.message.answer("Введите ваше ФИО:")
    await state.set_state(BookingStates.entering_name)
