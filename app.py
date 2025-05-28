import streamlit as st

변수 = st.session_state
if '체력' not in 변수:
    변수.체력=100
st.image('https://i.namu.wiki/i/aSIKJEBn6XjMFF3BATPIgZEHUydVtd_dMVYDez64M7BVa2KX0Voya0k1IMRTXgPVbW2-OsgkgzrZAvgbndjwYQ.webp')
st.title(f"남은 체력: {변수.체력}")
if 변수.체력 < 0 :
    st.error("사망")

if st.button("죽여 버리기"):
    변수.체력 = 변수.체력 - 10000000000000000000
    st.rerun()

if st.button("회복"):
    변수.체력 = 변수.체력 + 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    st.rerun()
