### 모듈 로딩
import cgi, sys, codecs, datetime

### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


### 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage()
# output이 web에 나온다 (터미널이 아님)


if 'img_file' in form and 'message' in form:
    fileitem = form['img_file']

    # 서버에 이미지 파일 저장 
    img_file = fileitem.filename

    suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f"./image/{suffix}_{img_file}"   # 별도의 image 폴더에 저장될 것이다. (서버에 저장된 이미지가 로컬 컴에 저장될것)
                                        # 브라우저 입장에서는 image가 같은 경로이다 (현재 서버가 day03_0411 이니까)
    with open(save_path, 'wb') as f :
        f.write(fileitem.file.read())


    img_path = f"../image/{suffix}_{img_file}"   # 로컬에 저장된 파일을 가져오는 경로 
                                        # 파이선에서 나가니까 image폴더가 상위 경로에 있다
    msg = form.getvalue('message')  
else : 
    img_path = 'None'
    msg = 'None'


### 요청에 대한 응답 HTML
print("Content-Type : text/html")    
print()                               
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello World")

print(f"<img src = {img_path}>")
print(f"<h3>{fileitem} = {msg}</h3>")