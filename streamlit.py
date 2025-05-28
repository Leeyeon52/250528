import streamlit as st

# 제주 추천 장소 샘플 데이터 (지역별로 확장 가능)
recommendations = {
    "제주시": [
        {"place": "한라산국립공원 성판악탐방로", "score": 4.76},
        {"place": "코난해변", "score": 4.76},
        {"place": "숙성도 함덕점", "score": 4.74},
        {"place": "미영이네식당", "score": 4.74},
        {"place": "회춘 애월점", "score": 4.73},
        {"place": "호텔리젠트마린", "score": 4.73},
        {"place": "보룡제과", "score": 4.73},
        {"place": "부촌", "score": 4.71},
        {"place": "빽다방베이커리 제주사수점", "score": 4.71},
        {"place": "노을해안1014", "score": 4.70},
    ],
    "서울시": [],  # 추후 서울 추천 추가 가능
    "부산시": [],  # 추후 부산 추천 추가 가능
    "강릉시": [],  # 추후 강릉 추천 추가 가능
}

st.title("🌏 여행지 만족도 기반 장소 추천기")
st.write("여행 성향을 입력하면 해당 도시에서의 인기 장소 Top 10을 예측합니다.")

gender = st.selectbox("성별 (0=남, 1=여)", options=[0, 1], format_func=lambda x: "남자" if x == 0 else "여자")
travel_style = st.selectbox("여행 스타일", options=["휴양", "문화", "자연", "쇼핑"])
visit_area = st.selectbox("방문 지역", options=list(recommendations.keys()))

if st.button("Top10 추천 보기"):
    recs = recommendations.get(visit_area, [])
    if not recs:
        st.warning(f"{visit_area}에 대한 추천 장소 데이터가 없습니다.")
    else:
        st.markdown(f"### 📌 {visit_area} Top 10 추천 장소")
        for i, rec in enumerate(recs, start=1):
            st.write(f"{i}. {rec['place']} — 점수: {rec['score']:.2f}")
s