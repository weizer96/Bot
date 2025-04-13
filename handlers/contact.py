from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import BookingStates
from config import load_config

router = Router()
config = load_config()


@router.message(BookingStates.entering_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(BookingStates.entering_phone)


@router.message(BookingStates.entering_phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data()

    text = (
        f"Услуга: {data['service']}\n"
        f"Дата: {data['date']} в {data['time']}:00\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}"
    )

    await message.answer(text)
    await message.answer("Заявка отправлена! Спасибо, мы скоро свяжемся с вами, чтобы подтвердить запись. 📲")
    await message.bot.send_message(chat_id=config.admin_chat_id, text=f"Новая запись:\n\n {text}")
    await state.clear()
