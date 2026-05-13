import streamlit as st
import pandas as pd
import numpy as np

# 여기서부터 자유롭게 작성하세요

# ── 예시 구조 (지우고 새로 써도 됩니다) ────────────────
# 1. [텍스트] 제목과 설명
st.title("🌡️ 우리 동네 날씨 대시보드")
st.header("월별 기온과 강수량 확인하기")
st.write("슬라이더를 움직여서 보고 싶은 달의 데이터를 확인하세요.")

# 2. [데이터] 아주 간단한 데이터 만들기
# 월 이름을 숫자로만 쓰면 차트 글자가 똑바로 보입니다.
data = {
    "월": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "기온": [-2.4, 0.4, 6.3, 12.8, 18.2, 22.4, 25.5, 26.3, 21.0, 14.5, 7.3, 0.5],
    "강수량": [20, 28, 45, 78, 102, 150, 380, 320, 160, 55, 45, 25]
}
df = pd.DataFrame(data)

# 3. [위젯] 사이드바에 월 선택 슬라이더 만들기
st.sidebar.header("설정")
month_range = st.sidebar.slider("월 범위를 선택하세요", 1, 12, (1, 12))

# 4. [위젯-화면 연동] 선택한 범위만 데이터 잘라내기
start_m, end_m = month_range
filtered_df = df[(df["월"] >= start_m) & (df["월"] <= end_m)]

# 5. [데이터] 메트릭으로 최고 기온 보여주기
high_temp = filtered_df["기온"].max()
st.metric(label="선택 범위 최고 기온", value=f"{high_temp} °C")

# 6. [데이터] 표 보여주기
st.dataframe(filtered_df)

# 7. [차트] 기온은 선 그래프, 강수량은 막대 그래프
st.subheader("🌡️ 기온 변화 추이")
st.line_chart(filtered_df.set_index("월")["기온"])

st.subheader("💧 월별 강수량")
st.bar_chart(filtered_df.set_index("월")["강수량"])
