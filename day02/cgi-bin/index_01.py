
### 모듈 로딩
import cgi, sys, codecs

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


# ----------------------------------------------------------------------------------------------
# html 파일 읽어서 결과 보여주는 함수
# ----------------------------------------------------------------------------------------------
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열 
    filename='./html/test.html'
    with open(filename, 'r', encoding='utf-8') as f:
        # HTML Header
        print("Content-Type: text/html; charset=utf-8")
        print()    # 한줄을 띄어주어야 head와 body 구분 가능 

        # HTML Body
        print(f.read().format(result))  # result라는 변수의 값을 파일에서 읽겠다.


### 클라이언트 요청으로 받은 from데이터 저장 목적의 클래스
form = cgi.FieldStorage()


### 데이터 추출
# result=""
if "data1" in form:
    result = form.getvalue("data1")
    # 딕셔너리처럼 form["data"]로 사용 가능 
    # print(result)
else :
    result = "no data"


### 브라우징
print_browser(result)

# python -m http.server 8080 --bind 127.0.0.1