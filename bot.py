from telegram.ext import Updater
from telegram.ext import CommandHandler
from film_pars import suggest_film as sf



def return_film(Update, CallbackContext):
    data = sf('User_info.json')
    photo = data[6]
    text = f'Название: {data[0]}\nРейтинг: {data[1]}\nГод выпуска: {data[2]}\nЖанры: {data[3]}\nСтраны выпуска: {data[4]}\nСсылка на фильм: {data[5]}\n'
    CallbackContext.bot.send_photo(chat_id=Update.message.chat_id, photo=photo, caption=text)


def main():
    TOKEN = "5055283494:AAE4IvF_pCnLIkSkafWr4mcI2mNe6Y0Wj1o"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = CommandHandler("get", return_film)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
