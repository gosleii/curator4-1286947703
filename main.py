import telebot

bot = telebot.TeleBot("7042336154:AAFM7Y1oEzpTqEpZeLy9WbAMYgJ-puJ4x9g")

@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "_Привет_", parse_mode="Markdown")


@bot.message_handler(commands=["new"])
def new_handler(message):
    bot.send_message(message.chat.id, "_сейчас я тебе расскажу о музыкальных инструментах_", parse_mode="Markdown")

@bot.message_handler(commands=["musical"])
def musical_handler(message):
    bot.send_message(message.chat.id, ("**Все о самом популярном музыкальном инструменте**)[https://ru.m.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D1%82%D0%B5%D0%BF%D0%B8%D0%B0%D0%BD%D0%BE]"),parse_mode="Markdown")

@bot.message_handler(commands=["all"])
def all_handler(message):
    bot.send_message(message.chat.id, "[**Подробнее о других музыкальных инструментах**](https://jliza-ru.turbopages.org/turbo/jliza.ru/s/vidyi-muzyikalnyix-instrumentov.html)")
@bot.message_handler(commands=["end"])
def end_handler(message):
    bot.send_message(message.chat.id, "**Спасибо за внимание**", parse_mode="Markdown")
bot.infinity_polling()