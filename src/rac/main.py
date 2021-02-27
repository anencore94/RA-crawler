import line, kakao, naver
import telegram

bot_access_token = '1638721240:AAGUo6cYy0VujwOJEcvZ9hRu_mee3aTFhpM'
my_telegram_id = '1010631797'
t_bot = telegram.Bot(token=bot_access_token)

msg_candidates = []
msg_candidates.append(line.job_posting_msg)
msg_candidates.append(kakao.job_posting_msg)
msg_candidates.append(naver.job_posting_msg)

msg = ''

for comp, msg_cand in zip(['Line', 'Kakao', 'Naver'], msg_candidates):
    msg += '[' + comp + ']' + '\n' + str("{}\n" * len(msg_cand)).format(
        *msg_cand) + '\n'

t_bot.send_message(my_telegram_id, msg)
