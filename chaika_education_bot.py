import telebot
from telebot import types
 
bot = telebot.TeleBot('5671778001:AAHV_f8iqC4CrXC7UkgHkDORESQaFiaj7LA')

@bot.message_handler(commands=['start'])
def start(message):
    
   
    photo = open('logo.png', 'rb')
    bot.send_photo(message.chat.id, photo )
 




    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    more = types.KeyboardButton('ДІЗНАТИСЯ БІЛЬШЕ')
    check = types.KeyboardButton('ПЕРЕВIРИТИ ЗНАННЯ')
    regLesson = types.KeyboardButton('ЗАРЕЄСТРУВАТИСЯ НА БЕЗКОШТОВНИЙ УРОК')
    regWeb = types.KeyboardButton('ЗАРЕЄСТРУВАТИСЯ НА БЕЗКОШТОВНИЙ ВЕБІНАР')
    contact = types.KeyboardButton('ЗВ’ЯЗАТИСЯ З АДМІНІСТРАТОРОМ')
    
    markup.add(more, check, regLesson, regWeb, contact)
    bot.send_message(message.chat.id, 'Привіт, це чат-бот команди школи “Chaika Education”!\n \nДавай знайомитися ближче😉\n💫 Ми крутезна мовна школа, яка випустила більше 300 задоволених клієнтів \n💫 Ми унікальні курси для підготовки до ЗНО та ДПА, які допомогли вступити до омріяного ВНЗ багатьом українським абітурієнтам.\n💫Наші викладачі стають справжніми друзями для учнів і 24/7 готові прийти на допомогу.\n\nУсю цікаву інформацію ти зможешь знайти в меню 👇',
          parse_mode='html', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == "ДІЗНАТИСЯ БІЛЬШЕ":
        markup1 = types.InlineKeyboardMarkup()
        markup1.add(types.InlineKeyboardButton("НАШ САЙТ 🌍", url="http://chaikaeducation.com.ua/"))
        markup1.add(types.InlineKeyboardButton("ІНСТАГРАМ 📷", url="https://www.instagram.com/chaika_education/"))
        markup1.add(types.InlineKeyboardButton("ТІК ТОК 🕺", url="https://www.tiktok.com/@chaika.education?_t=8XAQTftDb5J&_r=1"))
        bot.send_message(message.chat.id, 'Познайомитись з нами можна тут', reply_markup=markup1)
    elif message.text == "ПЕРЕВIРИТИ ЗНАННЯ":
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton('ТЕСТ З АНГЛІЙСЬКОЇ 🇬🇧', url="http://chaikaeducation.com.ua/"))
        markup2.add(types.InlineKeyboardButton('ТЕСТ З ПОЛЬСЬКОЇ 🇵🇱', url="http://chaikaeducation.com.ua/"))
        markup2.add(types.InlineKeyboardButton('ТЕСТ З НІМЕЦЬКОЇ 🇩🇪', url="http://chaikaeducation.com.ua/"))
        bot.send_message(message.chat.id, 'Обери тест з якої мови ти хочеш пройти', reply_markup=markup2)
    elif message.text == "ЗАРЕЄСТРУВАТИСЯ НА БЕЗКОШТОВНИЙ УРОК":
        markup3 = types.InlineKeyboardMarkup()
        markup3.add(types.InlineKeyboardButton('РЕЄСТРАЦІЯ НА БЕЗКОШТОВНИЙ УРОК', url="http://chaikaeducation.com.ua/"))
        bot.send_message(message.chat.id, 'Зареєструватись можна натиснувши на цю кнопку', reply_markup=markup3)
    elif message.text == "ЗАРЕЄСТРУВАТИСЯ НА БЕЗКОШТОВНИЙ ВЕБІНАР":
        markup4 = types.InlineKeyboardMarkup()
        markup4.add(types.InlineKeyboardButton('РЕЄСТРАЦІЯ НА БЕЗКОШТОВНИЙ ВЕБІНАР', url="http://chaikaeducation.com.ua/"))
        bot.send_message(message.chat.id, 'Зареєструватись можна натиснувши на цю кнопку', reply_markup=markup4)
    elif message.text == "ЗВ’ЯЗАТИСЯ З АДМІНІСТРАТОРОМ":
        markup4 = types.InlineKeyboardMarkup()
        markup4.add(types.InlineKeyboardButton('АДМІНІСТРАТОР АЛІНА 👧', url="https://t.me/nu_mqu_am"))
        bot.send_message(message.chat.id, 'Аліна чекає на твоє повідомлення', reply_markup=markup4)
    
bot.polling(none_stop=True)

