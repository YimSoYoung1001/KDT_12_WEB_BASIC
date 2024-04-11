### 모듈 로딩
import cgi, sys, codecs

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage()
# output이 web에 나온다 (터미널이 아님)


if 'img_file' in form and 'message' in form:
    filename = form['img_file']  # filename = form.getvalue(key = 'img_file')
    msg = form['message']  # msg = form.getvalue(key = 'message')
    

# 이거는 파이선 파일이 아니다.
# 이거는 클라이언트가 입력한 파일을 처리해주는 파일이 된다.

### 요청에 대한 응답 HTML
print("Content-Type : text/html")      # 브라우저가 html을 읽어주도록 해준다 (HTML is following)
print()                                # end of headers 
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello World : {form}")

print(f"<h3>{fileitem} = {msg}</h3>")