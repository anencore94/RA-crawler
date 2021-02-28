from enum import Enum

keywords_to_search = ['m/l', 'd/l', 'ml', 'dl', 'machine', 'deep', 'scientist',
                      '머신', '딥', '사이언티스트', '사이언스', '추천', '학습',
                      '전문연구']  # 추후 arg 로 받기


class CompanyUrl(str, Enum):
    LINE = "https://careers.linecorp.com"
    KAKAO = "https://careers.kakao.com"
    NAVER = "https://recruit.navercorp.com/naver/job"
    COUPANG = ''
    WOOWAH = ''
