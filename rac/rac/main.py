import argparse

import telegram

import kakao
import line
import naver


def run(param):
    t_bot = telegram.Bot(token=param['bot_access_token'])
    key = param['keywords_to_search']
    print(f'키워드 {key}에 속하는 채용 공고를 찾습니다.')
    msg_candidates = [line.line(param['keywords_to_search']),
                      kakao.kakao(param['keywords_to_search']),
                      naver.naver(param['keywords_to_search'])]

    msg = ''
    for comp, msg_cand in zip(['Line', 'Kakao', 'Naver'], msg_candidates):
        msg += '[' + comp + ']' + '\n' \
               + str("{}\n" * len(msg_cand)).format(*msg_cand) + '\n'

    t_bot.send_message(param['telegram_id'], msg)


if __name__ == "__main__":
    bot_access_token = '1638721240:AAGUo6cYy0VujwOJEcvZ9hRu_mee3aTFhpM'
    my_telegram_id = '1010631797'

    parser = argparse.ArgumentParser()
    parser.add_argument('--bot_access_token', type=str,
                        default=bot_access_token)
    parser.add_argument('--telegram_id', type=str, default=my_telegram_id)
    parser.add_argument('--keywords_to_search', '-k', action='append')

    args = parser.parse_args()
    dict_formatted_args = vars(args)

    run(dict_formatted_args)
