
import matplotlib.pyplot as plt

def predict_next(history):
    if not history:
        return "尚無資料"
    if history[-1] == 'B':
        return '預測：P（閒）可能出現'
    elif history[-1] == 'P':
        return '預測：B（莊）可能出現'
    return "無法預測"

def count_results(history):
    count_B = history.count('B')
    count_P = history.count('P')
    total = len(history)
    ratio_B = (count_B / total) * 100 if total else 0
    ratio_P = (count_P / total) * 100 if total else 0
    return count_B, count_P, ratio_B, ratio_P

def make_trend_chart(history):
    B_count, P_count = 0, 0
    B_trend, P_trend = [], []
    for h in history:
        if h == 'B':
            B_count += 1
        elif h == 'P':
            P_count += 1
        B_trend.append(B_count)
        P_trend.append(P_count)

    fig, ax = plt.subplots()
    ax.plot(B_trend, label='莊', marker='o')
    ax.plot(P_trend, label='閒', marker='o')
    ax.set_title("莊/閒累積趨勢圖")
    ax.set_xlabel("局數")
    ax.set_ylabel("次數")
    ax.legend()
    return fig
