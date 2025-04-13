from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states import BookingStates

router = Router()


@router.callback_query(F.data.startswith("service:"))
async def choose_date(callback: CallbackQuery, state: FSMContext):
    service = callback.data.split(":", 1)[1]
    await callback.message.edit_text(f"✅ Вы выбрали услугу: {service}")
    await state.update_data(service=service)
    await callback.message.answer("📅 Введите дату записи в формате ДД.ММ.ГГГГ")
    await state.set_state(BookingStates.choosing_date)
