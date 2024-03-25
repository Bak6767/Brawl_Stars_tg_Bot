from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Commands.user_cmd import send_profile_photo
from aiogram import types, Router, F, Bot
from dotenv import load_dotenv
from database import bd as db
import os


rp = Router()
load_dotenv()

bot = Bot(token = os.getenv("TOKEN_API"))

#Набор кнопок для команды /Brawl_Stars
async def communication() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = "Фото профиля", callback_data = "photo"))
    builder.row(InlineKeyboardButton(text = "Изменить Brawl Stars id", callback_data = "change"))
    return builder.as_markup()


async def photo(user_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):
        profile_id = str(await getattr(db, f'get_brawl_id_{i}')(user_id))
        if profile_id in ["False", "None"]:
            profile_id = "+"
            callback_data = f"add_brawl_id_{i}"
        else:
            callback_data = f"brawl_id_{i}"
        builder.row(InlineKeyboardButton(text=profile_id, callback_data=callback_data))
    return builder.as_markup()


async def brawl_stars_name(user_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(1, 4):
        profile_name = str(await getattr(db, f'get_brawl_name_{i}')(user_id))
        if profile_name in ["False", "None"]:
            profile_name = "+"
            callback_data = f"add_brawl_id_{i}"
        else:
            callback_data = f"brawl_id_{i}"
        builder.row(InlineKeyboardButton(text=profile_name, callback_data=callback_data))
    return builder.as_markup()



