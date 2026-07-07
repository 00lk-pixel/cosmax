import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Hey, I miss you",
    page_icon="✈️",
    layout="wide",
)

# 원본 worldwidelovers 페이지(index.html)를 그대로 불러와서 임베드합니다.
# 캔버스 배경 애니메이션, 픽셀아트 옷차림/지구본, 실시간 항공편 목록 선택,
# localStorage 키 기억, 입력값 변경 시 자동 재계산 등 원본 동작을 전부 그대로 유지합니다.
html_path = Path(__file__).parent / "worldwidelovers.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=900, scrolling=True)

st.caption(
    "원본 페이지(https://00lk-pixel.github.io/worldwidelovers/)를 그대로 임베드한 화면입니다. "
    "날씨: Open-Meteo · 항공편 추적: AviationStack API"
)
