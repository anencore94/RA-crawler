import line, kakao
import telegram

bot_access_token = '1638721240:AAGUo6cYy0VujwOJEcvZ9hRu_mee3aTFhpM'
my_telegram_id = '1010631797'
t_bot = telegram.Bot(token=bot_access_token)

msg = '' + \
      '[Line plus]' + '\n' + str("{}\n" * len(line.answer)).format(
    *line.answer) + '\n' + \
      '[Kakao]' + '\n' + str("{}\n" * len(kakao.answer)).format(
    *kakao.answer) + '\n'
t_bot.send_message(my_telegram_id, msg)
