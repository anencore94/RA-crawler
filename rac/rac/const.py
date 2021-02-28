from enum import Enum


class CompanyUrl(str, Enum):
    LINE = "https://careers.linecorp.com"
    KAKAO = "https://careers.kakao.com"
    NAVER = "https://recruit.navercorp.com/naver/job"
    COUPANG = ''
    WOOWAH = ''
