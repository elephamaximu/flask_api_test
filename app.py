# Flask 클래스 임포트
from flask import Flask

# 임포트한 Flask 클래스를 객체화 시켜서 app이라는 변수에 저장
# 이 app 변수가 바로 API 애플리케이션(정확히는 Flask 웹 애플리케이션)
# app 변수에 API 설정과 엔드포인트들을 추가하면서 API가 완성되는 것
app = Flask(__name__)

# flask의 route 데코레이터를 사용하여 엔드포인트를 등록한다.
# ping 함수를 엔드포인트 함수로 등록하였으며, 고유 주소는 "ping"이며
# 메소드는 GET으로 설정함
@app.route("/ping", methods=['GET'])

# ping 함수를 정의, route 데코레이터를 사용하여 엔드포인트를 등록한다.
# 
def ping():
    return "pong"

