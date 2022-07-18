#!/usr/bin/env python
# encoding: utf-8

from loader import dp, searcher

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile



@dp.message_handler()
async def send_answer(message: types.Message):
    request = message.text

    searcher.search_by_text_in_file(request, 'output.csv')

    await message.reply_document(InputFile('output.csv'), 'output.csv') 


"""
    result = searcher.search_by_text(request, skip=0)

    inline_button = InlineKeyboardButton('Следующая выдача', callback_data='1:' + request)
    markup = InlineKeyboardMarkup().add(inline_button)

    await message.answer(title + result, reply_markup=markup)

"""

@dp.callback_query_handler()
async def send_answer_from_callback(query: types.CallbackQuery):
    skip, request = query.data.split(':', 1)
    skip = int(skip)

    callback_data = f"{skip+1}:{request}"
    inline_button = InlineKeyboardButton('Следующая выдача', callback_data=callback_data)
    markup = InlineKeyboardMarkup().add(inline_button)

    title = f"Результаты по запросу '{request}', выдача №{skip + 1}\n\n"
    result = searcher.search_by_text(request, skip=skip)
    await query.answer()
    await query.message.answer(title + result, reply_markup=markup)

