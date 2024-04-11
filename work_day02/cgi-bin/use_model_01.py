import cgi, sys, codecs, os, joblib, cgitb
from pydoc import html
cgitb.enable()
import pandas as pd


### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())



# -----------------------------------------------------------------
# html 파일 읽어서 결과 보여주는 함수
# -----------------------------------------------------------------
def print_browser(result=""):
    # HTML 파일 읽기 -> body 문자열
    filename='./html/collect_model.html'
    with open(filename, mode="r", encoding="utf-8") as f:
        # HTML Header
        print("Content-Type: text/html; charset = utf-8")
        print()    # 한줄을 띄어주어야 head와 body 구분 가능

        # HTML Body
        # print(f.read().format(result))  # result라는 변수의 값을 파일에서 읽겠다.
        print(f.read().format(result)) 


# -----------------------------------------------------------------
# 모델 predict 함수
# -----------------------------------------------------------------
def model_predict(list):
    user_calorie = int(model.predict(list)[0])

    print(f"your hamburger has {user_calorie}kcal")

    hbg_brand = []
    hbg_name = []
    hbg_cal_list = []

    data = pd.read_csv('./Hamburger.csv')
    for i in range(data.shape[0]):
        if user_calorie - 5 <= data.iloc[i][2] <= user_calorie + 5:
            hbg_brand.append(data.iloc[i][0])
            hbg_name.append(data.iloc[i][1])
            hbg_cal_list.append(data.iloc[i][2])
    # print('we recommend these. (error range 5kcal)')
    return user_calorie, hbg_brand, hbg_name, hbg_cal_list



# -----------------------------------------------------------------
# (1) 모델 불러오기
# -----------------------------------------------------------------
filedir = '../my_model/gradient_boosting_reg.pkl'    # 햄버거 칼로리 계산
file = os.path.dirname(filedir)
model = joblib.load(filedir)


# -----------------------------------------------------------------
# (2) 브라우저에 작성된 내용을 불러오기
# -----------------------------------------------------------------
form = cgi.FieldStorage()  #클라이언트 요청으로 받은 from데이터 저장 목적의 클래스

natruim = form.getvalue('natruim')
sugar = form.getvalue('sugar')
fat = form.getvalue('fat')
protein = form.getvalue('protein')


# -----------------------------------------------------------------
# (3) 판정하기
# -----------------------------------------------------------------
# result=""


if 'natruim' in form and 'sugar' in form and 'fat' in form and 'protein' in form:
    print(f"you want sodium {natruim}mg, sugar {sugar}g, fat {fat}g, protein {protein}g")
    list = []
    list.append(natruim)
    list.append(sugar)
    list.append(fat)
    list.append(protein)
    # 불러온 모델에서 예측해서 결과값 내놓기
    calorie, brand, name, hbg_list  = model_predict(list)
    output = calorie
else:
    output = 'No Data'


# -----------------------------------------------------------------
# (4) browser에 출력하기
# -----------------------------------------------------------------
print_browser(result = output)

# python -m http.server 8080 --bind 127.0.0.1 --cgi
