# Кусок информации полученный нами от Телеграма
from telegram import Update

# ApplicationBuilder - способ создать приложение с указанием настроек
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from Parsing_Practice_2_1 import parse_hh

# token - секретный ключ к вашему боту (получить у @BotFather)
app = ApplicationBuilder().token('TOKEN').build()

# Функция вызывается при получении сообщения
# upd - новая информация от ТГ
# ctx - служебная информация
async def text_reply(upd: Update, _ctx):
    user_text = upd.message.text
    print(f'User: {user_text}')
    # Запустить парсинг
    name = upd.message.from_user.full_name
    reply = f'Уважаемый {name}, мы получили ваш запрос "{user_text}"'
    print(reply)
    await upd.message.reply_text(reply)
    jobs_count = parse_hh(user_text)
    await upd.message.reply_text(f'Найдено вакансий: {jobs_count}')

# Handler - обработчик сообщения
handler = MessageHandler(filters.TEXT, text_reply)
# MessageHandler - для сообщений (текстовые, аудио, анимации, стикеры)
# CommandHandler - для команд (/hello, /start)

# Прикрепляем обработчик к прилодению
app.add_handler(handler)

# Запускаем приложение
app.run_polling()
