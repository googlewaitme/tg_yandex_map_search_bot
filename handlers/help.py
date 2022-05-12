#!/usr/bin/env python
# encoding: utf-8

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text('/help'))
async def send_help(message: types.Message):
    await message.answer("Просто запросы без номеров")

