import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from config import BOT_TOKEN as token
from buttons import phone, menyu, taomlar, ichimliklar, buyurtma_sonlar
from data_base import Food_Sql, UsersAdd
from states import Food707
import time


TOKEN = token
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=phone)

@dp.message(F.contact)
async def Telefon_Nomr(message: Message, state: FSMContext):
    telefon = message.contact.phone_number
    telegram_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    UsersAdd(title=f"{full_name}", phone_number=f"{telefon}", telegram_id=f"{telegram_id}", username=f"@{username}")
    await state.update_data({
        'telefon':telefon,
        'telegram_id':telegram_id
    })
    await message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption=f"Bizning Restrandagi menyu", reply_markup=menyu.as_markup())
    await state.set_state(Food707.state_menyu)



@dp.callback_query(F.data, Food707.state_menyu)
async def Taomlar(call: CallbackQuery, state: FSMContext):
    mijoz_taom = call.data
    await state.update_data({
        "taom":mijoz_taom
    })
    if mijoz_taom == "Ichimliklar 🥂":
        for taom in Food_Sql():
            if taom[0] == 1:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=taomlar.as_markup())
                await state.set_state(Food707.state_ichimliklar)
    elif mijoz_taom == "Taomlar  🍔":
        for taom in Food_Sql():
            if taom[0] == 2:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=ichimliklar.as_markup())
                await state.set_state(Food707.state_taomlar)


@dp.callback_query(F.data, Food707.state_taomlar)
async def Taomlar(call: CallbackQuery, state: FSMContext):
    taomlar_royhat = call.data
    await state.update_data({
        'taomlar_royhat':taomlar_royhat
    })
    for taom in Food_Sql():
           if taom[1] == taomlar_royhat:
                rasm = FSInputFile(f"../media/{taom[3]}")
                await call.message.answer_photo(photo=rasm, caption=f"Nomi: {taom[1]}\nNechta olmoqchisiz\nNarxi: {taom[2]} so'm", reply_markup=buyurtma_sonlar.as_markup())
                await state.set_state(Food707.state_soni)    

@dp.callback_query(F.data, Food707.state_ichimliklar)
async def Ichimliklar(call: CallbackQuery, state: FSMContext):
    taomlar_royhat = call.data
    await state.update_data({
        'taomlar_royhat':taomlar_royhat
    })
    for taom in Food_Sql():
            if taom[1] == taomlar_royhat:
                rasm = FSInputFile(f"../media/{taom[3]}")
                # rasm = FSInputFile(f"media/{taom[3]}")
                await call.message.answer_photo(photo=rasm, caption=f"Nomi: {taom[1]}\nNechta olmoqchisiz\nNarxi: {taom[2]} so'm", reply_markup=buyurtma_sonlar.as_markup())
                await state.set_state(Food707.state_soni)    


@dp.callback_query(F.data, Food707.state_soni)
async def Taomlar_Zakaz(call: CallbackQuery, state: FSMContext):
    sonlar = call.data
    await state.update_data({
        'sonlar':sonlar
    })
    await call.answer("Sizning buyurtmangiz savatga qo'shildi Yena buyurtma qo'shishingiz mumkin")
    time.sleep(3)
    await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption=f"Bizning Restrandagi menyu", reply_markup=menyu.as_markup())
    await state.set_state(Food707.state_menyu)



@dp.callback_query(F.data == "zakaz")
async def Karzinka(call: CallbackQuery):
    pass
    





async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())