# Selenium Example
- chrome을 이용한 selenium 모듈 조작 예제
- 주기적인 브라우저 조작 테스크를 crontab으로 예약

## usage
### script.conf
- user_data_dir: chrome://version에서 profile path에서 확인가능 (마지막 Default는 제외하고 dir만 적어주면 됨)
- dest: target이 될 사이트 주소
- id: 컨트롤 할 html tag id

### run.py
- 사이트에서 버튼 조작 example

### crontab
- `crontab -e` 으로 crontab 예약 가능
- `00 18 * * 1-5 env DISPLAY=:0 /usr/bin/python3 {dir}/run.py >> {dir}/log.txt 2>&1`
처럼 주중 간 6시에 자동 실행 예약 가능
