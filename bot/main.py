import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from config import BOT_TOKEN as token
from buttons import phone, menyu, taomlar, ichimliklar
from data_base import Food_Sql


TOKEN = token
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=phone)

@dp.message(F.contact)
async def Telefon_Nomr(message: Message):
    telefon = message.contact.phone_number
    await message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption=f"Bizning Restrandagi menyu", reply_markup=menyu.as_markup())
    

@dp.callback_query(F.data)
async def Taomlar(call: CallbackQuery):
    mijoz_taom = call.data
    if mijoz_taom == "Taomlar  🍔":
        for taom in Food_Sql():
            if taom[0] == 1:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=taomlar.as_markup())
    elif mijoz_taom == "Ichimliklar 🥂":
        for taom in Food_Sql():
            if taom[0] == 2:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=ichimliklar.as_markup())




@dp.callback_query(F.data)
# async def 










async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())