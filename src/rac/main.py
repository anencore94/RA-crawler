import line, kakao
import telegram

bot_access_token = '1638721240:AAGUo6cYy0VujwOJEcvZ9hRu_mee3aTFhpM'
my_telegram_id = '1010631797'
t_bot = telegram.Bot(token=bot_access_token)

msg = '' + \
      '[Line plus]' + '\n' + str("{}\n" * len(line.job_posting_msg)).format(
    *line.job_posting_msg) + '\n' + \
      '[Kakao]' + '\n' + str("{}\n" * len(kakao.job_posting_msg)).format(
    *kakao.job_posting_msg) + '\n'
t_bot.send_message(my_telegram_id, msg)
