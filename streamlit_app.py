import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("서울 날씨 대시보드")   # ← 제목을 바꿔보세요

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["막대 그래프", "꺾은선 그래프", "면적 그래프"]   # ← 유형을 바꿔보세요
)

n = st.sidebar.slider(
    "데이터 개수",
    min_value=5,    # ← 최솟값을 바꿔보세요
    max_value=50,   # ← 최댓값을 바꿔보세요
    value=30
)

# ── 메인 화면 ─────────────────────────────────
st.write("계절 온도")   # ← 설명을 바꿔보세요

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['봄', '여름', '가을']   # ← 컬럼 이름을 바꿔보세요
)
st.header("지표(Metric)")
col1, = st.columns(1)
col1.metric("올해 평균 온도", "36.5°C", "+1.2°C")


if chart_type == "꺾은선 그래프":
    st.line_chart(data)
elif chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────
