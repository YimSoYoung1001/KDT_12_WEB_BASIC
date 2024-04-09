import cgi

form = cgi.FieldStorage()  #클라이언트 요청으로 받은 from데이터 저장 목적의 클래스

result=""
if 'data1' in form and 'data2' in form:
    result = form.getvalue('data1') + " - " + form.getvalue('data2')
    print(result)



def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열 
    filename='./html/test.html'
    with open(filename, 'r', encoding='utf-8') as f:
        # HTML Header
        print("Content-Type: text/html")
        print()    # 한줄을 띄어주어야 head와 body 구분 가능 

        # HTML Body
        print(f.read().format(result))  # result라는 변수의 값을 파일에서 읽겠다.


print_browser(result=result)

