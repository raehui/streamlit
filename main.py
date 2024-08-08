import streamlit as st

#스트림릿에서 제목을 사용할 때
st.title("내 스트림릿 페이지임^^")

#스트림릿에서 헤더를 사용할 떄
st.header("이것은 헤더이다")

#스트림릿에서 서브헤더를 사용할 떄
st.subheader("이것은 서브헤더이다")

#스트림릿에서 텍스트를 사용할 떄===================================
#1. text -> 비교적 제한된 글쓰기. 단순한 문자, 포맷팅 없음, 일반 텍스트 형식 출력
#2. write -> 다양한 데이터 유형 표현 가능, 마크다운, html, LaTex,Json, 입력 데이터 유형에 따라서 자동으로 형식을 지정
            #포맷팅 f{} 사용가능

st.text("이것은 text이다")

date='2024-08-07'
st.write(f"today is {date}")

#마크다운 쓰기==============================================================
st.markdown("# 마크다운 쓰기")

#마크다운으로 하이퍼링크 걸기
st.markdown("[NAVER](http://www.naver.com)")

#마크다운으로 html 코드 쓰기
html_page = """
<div style="background-color:blue;padding:50px">
	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
</div>
"""

st.markdown(html_page, unsafe_allow_html=True)

#------------------------------------------------------------------------------------------
#팝업! -------> 시스템 메시지 띄우기
#성공, 정보전달, 경고, 에러
st.success("성공")

st.info("추가 정보는 여기 있습니다")

st.warning("뭔가 잘못되었음")

st.error("에러 발생하여 동작 불가")

#------------------------------------------------------------------------------------------
# 이미지, 비디오, 오디오 삽입

# 이미지 삽입
from PIL import Image

#Image.open('이미지 파일 경로')
#./ =현재 디렉토리
#외부 파일 가져오기: Image.open("C:/Users/jeong/Desktop/다운로드.jpg")
image=Image.open("./image_1.png")
st.image(image=image,width=300,caption='VGG19')

#비디오 삽입
#1. 가지고있는 비디오 재생하기
# video_file=open("비디오파일의 경로","rb").read()
# st.video(video_file)

#2. 스트리밍 비디오 재생하기
# st.video("https://www.youtube.com/watch?v=OmtlFkDOoNc")

# 오디오 삽입
# audio_file=open("","rb").read()
# st.audio(audio_file)

#------------------------------------------------------------------------------------------
#상호작용
if st.button("생일 축하해 아잉"):
    st.balloons()

#체크박스
if st.checkbox("check"):
    st.write("체크되었습니다.")

# 라디오버튼
radio_buttons = st.radio("선호하는 색상은?", ["빨강", "노랑", "파랑"])
if radio_buttons == "빨강":
    st.write("빨강색 장미꽃 추천!")
elif radio_buttons == "노랑":
    st.write("노랑색 해바라기 추천!")
else:
    st.write("파랑색 수국 추천!")  

# 셀렉트박스
city = st.selectbox("당신이 사는 도시는?", ["서울", "부산", "대구", "대전", "광주", "인천", "울산", "세종", "천안"])

# 당신이 원하는 직업은?
job = st.multiselect("당신이 원하는 직업은?", ["개발자", "디자이너", "데이터분석가", "연구원", "기획자", "마케터", "기타"])

#텍스트 인풋
# name=st.text_input("당신의 이름은?","이름을 입력하세요")
# if st.button("제출"):
#     result=name.title()
#     st.success(result) 

#텍스트 에어리어 
#여러 줄의 텍스트 입력 받기 가능
#플레이스 홀더 설정, 줄 수 지정 등이 가능
messages=st.text_area("메시지를 입력하세요","메시지를 입력하세요")
if st.button("제출"):
    result=messages.title()
    st.success(result) 

#슬라이더
st.slider("당신의 나이는?",1,80,1)

#날짜, 시간을 입력바을 수 있는 컴포넌트
import datetime
import time

st.header("날짜 & 시간")

today = st.date_input("오늘은 언제인가요?", datetime.datetime.now())
hours = st.time_input("지금 몇 시인가요?", datetime.time())

#------------------------------------------------------------------------------------------
#판다스 파일 업로드
import pandas as pd

st.header("판다스 데이터프레임")
df=pd.read_csv("./auto.csv")

st.dataframe(df)

#플롯 그리기
st.area_chart(df['mpg'])
st.bar_chart(df["mpg"])
st.line_chart(df["mpg"])

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.heatmap(df[["mpg","cylinders"]].corr(), annot=True, ax=ax)
st.pyplot(fig)

#------------------------------------------------------------------------------------------
import time
my_bar=st.progress(0)
for v in range(100):
    my_bar.progress(v+1)
    time.sleep(0.1)

with st.spinner("잠시만 기다려 주세요..."):
    time.sleep(5)
st.success("완료되었습니다.")

