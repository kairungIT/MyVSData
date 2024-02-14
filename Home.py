import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/377a24ee-4e19-48c9-8a2f-fcada962c70a/oax9riei3m.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การทำ Data Visualization ....")
st.header("by ผศ.ดร.ไก้รุ่ง เฮงพระพรหม")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()