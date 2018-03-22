# Selenium Example
- chrome을 이용한 selenium 모듈 조작 예제
- 주기적인 브라우저 조작 테스크를 crontab으로 예약

## Usage
### script.conf
run.py에서 사용되는 configuration 기본값 파일
- dest: target이 될 사이트 주소
- id: 컨트롤 할 html tag id
- chromedriver_path: chromedriver의 위치
    - ![https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) 에서 다운로드
    - 반드시 Supports Chrome을 확인하고 다운로드
- profile_path: chrome://version에서 profile path에서 확인가능 (optional)
    - 일반 chrome이 아닌 chromium의 경우엔 마지막 Default 이전까지 디렉토리 위치까지만 적어주면 됨
- browser_bin_path: 브라우저 실행파일 위치 (optional)
    - ubuntu의 경우, /usr/bin/google-chrome

### run.py
- 사이트에서 버튼 조작 example

### crontab
- `crontab -e` 으로 crontab 예약 가능
- `00 18 * * 1-5 env DISPLAY=:0 /usr/bin/python3 {dir}/run.py >> {dir}/log.txt 2>&1`
처럼 주중 간 6시에 자동 실행 예약 가능
