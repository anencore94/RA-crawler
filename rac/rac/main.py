import argparse

import telegram

import const
import kakao
import line
import naver


def run(param):
    t_bot = telegram.Bot(token=param['bot_access_token'])
    keywords = param['keywords_to_search']
    print(f'키워드 {keywords}에 속하는 채용 공고를 찾습니다.')

    msg_candidates = [line.get_msgs(keywords),
                      kakao.get_msgs(keywords),
                      naver.get_msgs(keywords)]

    msg = ''
    for company, msg_cand in zip([comp.name for comp in const.CompanyUrl],
                                 msg_candidates):
        msg += f'[{company}]\n' + \
               str("{}\n" * len(msg_cand)).format(*msg_cand) + '\n'

    t_bot.send_message(param['telegram_id'], msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot_access_token', '-b', type=str,
                        required=True)
    parser.add_argument('--telegram_id', '-t', type=str, required=True)
    parser.add_argument('--keywords_to_search', '-k', action='append',
                        required=True)

    args = parser.parse_args()
    dict_formatted_args = vars(args)

    run(dict_formatted_args)
