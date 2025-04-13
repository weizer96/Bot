from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.main import get_start_keyboard
from states import BookingStates

router = Router()


@router.message(F.text, F.text.lower() == "/start")
async def start_handler(message: Message, state: FSMContext):
    await message.answer("🚗 Привет! Добро пожаловать в Автоклимат44 — твой помощник по обслуживанию авто! ❄️🛠️\n\n")
    await message.answer("Выбери услугу и время с помощью кнопки ниже! 👇",
        reply_markup=get_start_keyboard()
    )


@router.callback_query(F.data == "book")
async def book_handler(callback: CallbackQuery, state: FSMContext):
    from keyboards.services import get_services_keyboard
    await callback.message.edit_text(
        "🔧 Выбери подходящую услугу:",
        reply_markup=get_services_keyboard()
    )
    await state.set_state(BookingStates.choosing_service)

