import telebot

bot = telebot.TeleBot('6106226400:AAGHpTAogJF0zfclmDM10rcHqHayIGnK1kE')


@bot.message_handler(commands=['help'])
def help(message):

    bot.send_message(message.chat.id, f'Hello, enter /start')


@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Hello {user_name},тебе нравится футбол? да/нет')
    bot.register_next_step_handler(message,foot)


def foot(message):
    text = message.text
    if text == 'да':
        bot.send_message(message.chat.id, f'за какой футбольный клуб ты болеешь?')
        bot.register_next_step_handler(message, foot1)
    if text == 'нет':
        bot.send_message(message.chat.id, f'А что тебе нравиться? любишь компьютерные игры? да/ нет')
        bot.register_next_step_handler(message, game)




def foot1(message):
    text = message.text

    bot.send_message(message.chat.id, f'А твой любимый футболист')



def game(message):
    text = message.text
    if text == 'да':
            bot.send_message(message.chat.id, f'А во что ты любишь играть?')
            bot.register_next_step_handler(message, game1)

    if text == 'нет':
        bot.send_message(message.chat.id, f'Все ок, ок')


def game1(message):
    text = message.text

    bot.send_message(message.chat.id, f'А твой любимый футболист')



@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, f'Enter /help')






if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)