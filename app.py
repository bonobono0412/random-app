import random
import streamlit as st

# 웹앱 제목 및 안내 문구 설정
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 눌러 오늘 먹을 점심 메뉴를 랜덤으로 뽑아보세요!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정할 수 있습니다)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈가스",
    "초밥",
    "짜장면",
    "짬뽕",
    "햄버거",
    "파스타",
    "순대국밥",
    "비빔밥",
    "떡볶이",
    "쌀국수",
    "카레라이스",
    "마라탕",
]

# 버튼을 클릭했을 때 실행되는 코드
if st.button("점심 메뉴 추천받기 🎲"):
    # 리스트에서 무작위로 하나 선택
    today_menu = random.choice(lunch_menus)

    # 결과 출력 및 축하 효과
    st.success(f"오늘의 추천 메뉴는 **{today_menu}**입니다! 맛있게 드세요 😋")
    st.balloons()
