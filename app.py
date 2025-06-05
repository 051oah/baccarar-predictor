import streamlit as st
import matplotlib.pyplot as plt
from utils import predict_next, count_results, make_trend_chart

# 頁面設定
st.set_page_config(page_title="百家樂預測器", layout="centered")

# Session 儲存
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🔮 百家樂預測器（升級版）")
st.markdown("請輸入歷史結果（B = 莊，P = 閒），用逗號分隔。例如：`B,P,B,P,B`")

# 輸入欄位
input_text = st.text_input("歷史結果輸入", value="")

if input_text:
    history = [x.strip().upper() for x in input_text.split(',') if x.strip().upper() in ['B', 'P']]
    st.session_state.history = history

if st.session_state.history:
    history = st.session_state.history
    st.write("📘 歷史紀錄：", history)

    # 統計資訊
    count_B, count_P, ratio_B, ratio_P = count_results(history)
    st.markdown("🧮 莊：{} 次（{:.1f}%）｜閒：{} 次（{:.1f}%）".format(count_B, ratio_B, count_P, ratio_P))

    # 預測與建議
    prediction = predict_next(history)
    st.subheader(f"🔮 {prediction}")

    # 趨勢圖表
    st.markdown("📈 出現趨勢：")
    fig = make_trend_chart(history)
    st.pyplot(fig)

    # 下注建議
    if len(history) >= 2 and history[-1] == history[-2]:
        st.info("提示：出現連續結果，考慮使用『反跳』策略，小注相反方。")
    elif len(set(history[-3:])) == 1:
        st.info("提示：連出三次相同結果，可考慮追打。")
    else:
        st.info("提示：建議觀察再下注，避免進場時機錯誤。")
