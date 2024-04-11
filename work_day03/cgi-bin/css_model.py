### 모듈 로딩
import cgi, sys, codecs, datetime
from PIL import Image
import torchvision.transforms as transforms
import torch


### Web 인코딩 설정
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

### 모델 로딩
model_file = './model/dog_or_chicken.pth'
saved_model = torch.load(model_file)


### 웹 페이지의 form 태그 내의 input 태그 입력값 가져와서 저장하고 있는 인스턴스
form = cgi.FieldStorage()

if 'img_file' in form : 
    fileitem = form['img_file']   # 이미지 파일을 꺼낸다.
    img_file = fileitem.filename  # 이미지 파일 이름을 꺼낸다.

    date_hour = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

    save_path = f"./img/{date_hour}_{img_file}"

    with open(save_path, 'wb') as f:    # 2진수로 읽어서 쓰겠다.
        f.write(fileitem.file.read())

    img_path = f"../img/{date_hour}_{img_file}"
else : img_path = 'None'


### 요청에 대한 응답 HTML
print("Content-Type : text/html")    
print()
print("<TITLE>Let's check</TITLE>")
print(f"<img src = {img_path}>")       # 이미지 로딩함

### 예측해보기
new_path = img_path[1:]
img = Image.open(new_path)

# 모델이 학습된 형태의 이미지로 변환
preprocessing = transforms.Compose([
    transforms.Resize(size = (150, 150)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
p_img = preprocessing(img)


# 모델 시연 라쓰고
saved_model.eval()
with torch.no_grad():
    p_img = p_img.unsqueeze(dim = 0)
    output = saved_model(p_img)
    output = torch.sigmoid(output).item()

if output < 0.5: result = 'C H I C K E N'
else: result = 'P O O D L E'

print(f"<H1>{result}</H1>")      # 모델이 예측한 답