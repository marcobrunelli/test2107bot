from telegram.ext import Updater, CommandHandler


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def main():
    updater = Updater('1336769815:AAE0wpLwXM8MwitYbe0IWOgqEfYD6QE5RXw', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
