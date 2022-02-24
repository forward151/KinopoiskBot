from telegram.ext import Updater, MessageHandler, Filters


def echo(update, context):
    update.message.reply_text(f'Я получил сообщение {update.message.text}')


def main():
    TOKEN = "5055283494:AAE4IvF_pCnLIkSkafWr4mcI2mNe6Y0Wj1o"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
