# RA-crawler

Recruit Announcement Crawler Sample

## How to Use

- telegram bot 을 만들어 $BOT_TOKEN 을 준비합니다.
- telegram bot 으로부터 message 를 받을 본인 계정의 $TELEGRAM_PRIVATE_ID 를 준비합니다.
- 원하는 모든 keyword 를 -k argument 로 입력합니다.

- 예)

```shell
python rac/rac/main.py -b $BOT_TOKEN -t $TELEGRAM_PRIVATE_ID -k ml -k dl -k m/l -k d/l -k machine -k deep -k scientist -k 머신 -k 딥 -k 사이언티스트 -k 사이언스 -k 학습 -k 전문연구
```

- 실행이 완료되면 $TELEGRAM_PRIVATE_ID 계정으로 다음과 같은 메시지가 도착합니다.

```markdown
[LINE]
('Machine Learning Engineer (LINE TIMELINE)', 'https://careers.linecorp.com/ko/jobs/308')
(' ML/AI ML Ops Engineer', 'https://careers.linecorp.com/ko/jobs/300')
('ML Platform Server-side Engineer', 'https://careers.linecorp.com/ko/jobs/299')
('Machine Learning Platform Engineer', 'https://careers.linecorp.com/ko/jobs/245')
('Machine Learning Platform Engineer', 'https://careers.linecorp.com/ko/jobs/240')
('AD Performance ML Engineer', 'https://careers.linecorp.com/ko/jobs/25')
('Data Scientist', 'https://careers.linecorp.com/ko/jobs/93')
('M/L Data Scientist', 'https://careers.linecorp.com/ko/jobs/67')

[KAKAO]
('카카오 전문연구요원(전직 및 보충역) 모집', 'https://careers.kakao.com/jobs/P-9349?page=1')
('데이터 사이언티스트를 지향하는 데이터 엔지니어 모집', 'https://careers.kakao.com/jobs/P-10993?page=2')
('데이터 가치를 함께 발굴하실 머신러닝, 통계 모델링 전문가 모집', 'https://careers.kakao.com/jobs/P-11479?page=2')
('추천 통계분석/데이터사이언티스트', 'https://careers.kakao.com/jobs/P-10913?page=2')
('머신러닝 엔지니어 모집', 'https://careers.kakao.com/jobs/P-11842?page=3')
('데이터 사이언스 전문가 및 머신러닝 전문가 모집', 'https://careers.kakao.com/jobs/P-10142?page=4')
('데이터 엔지니어 및 사이언티스트 (경력)', 'https://careers.kakao.com/jobs/P-11888?page=4')
('카카오톡 안티어뷰징을 위한 데이터/백엔드 엔지니어 및 머신러닝 전문가 모집', 'https://careers.kakao.com/jobs/P-11083?page=5')
('데이터 사이언티스트 모집 (경력)', 'https://careers.kakao.com/jobs/P-11816?page=5')

[NAVER]
('[Search] Applied Scientist for Web Search Relevance 신입/경력
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005251&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
('[Search] 파파고 머신러닝(자연어처리, 컴퓨터비전) 엔지니어 신입/경력
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005144&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
('[Biz] 광고 AI 조직 AI/ML/Backend/Data Engineer 경력사원
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005426&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
('[Clova CIC] 기계학습 모델링 및 데이터 분석 경력사원
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005175&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
('[지식베이스] 지식베이스 ML Engineer 경력사원
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005187&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
('[Apollo CIC] 데이터 사이언스 경력
모집', 'https://recruit.navercorp.com/naver/job/detail/developer?annoId=20005299&classId=&jobId=&entTypeCd=002&searchTxt=&searchSysComCd=')
```

- 일정 주기로 반복적인 실행을 원할 경우, `.github/workflows/python-app.yml` 을 참고하여 cronjob 으로 메시지를 받을 수 있습니다.
    - 원하는 keywords가 있는 경우 본 프로젝트를 fork 하여 `.github/workflows/python-app.yml` 를 수정 후 사용하시면 됩니다.
        - `$TELEGRAM_PRIVATE_ID` 를 본인 계정 id 로 변경
        - `-k`의 value 를 본인이 원하는 keywords 로 변경
            - 여러 keyword 가 있을 경우 `-k val_1`, `-k val_2`, ... 계속 추가하시면 됩니다.
        - 해당 val 을 **포함하는** 모든 채용공고가 선택됩니다.
- 현재 제 github action workflow 는 저에게만 매일 아침 09:00 경 ('ml', 'dl', 'm/l', 'd/l', 'machine', 'deep', 'scientist', '머신', '
  딥', '사이언티스트', '사이언스', '학습', '전문연구') 중 하나를 포함하는 채용공고와 링크를 담은 메시지를 보냅니다.

## TODO

- 마감날짜 표시
- 다른 회사 추가
- 오타 -> 비슷한 단어로 보정해서 검색 (needs DB so maybe implemeted later..)