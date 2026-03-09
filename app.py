# import streamlit as st
# import pandas as pd
# import joblib

# model = joblib.load("crime_future_model.pkl")
# state_enc = joblib.load("state_encoder_A0.pkl")
# target_enc = joblib.load("target_encoder_A0.pkl")

# df = pd.read_csv("C:/Users/hp/Desktop/ML03/indian_crime_with_categories_ordered.csv")

# st.title("Future Crime Risk Prediction")

# state = st.selectbox("Select State", sorted(df["State"].unique()))
# year = st.number_input("Enter Future Year", min_value=2023, max_value=2035)

# if st.button("Predict"):
#     hist = df[df["State"]==state].sort_values("Year").tail(3)

#     lag1 = hist.iloc[-1]["Crime_Rate_Per_100k"]
#     lag2 = hist.iloc[-2]["Crime_Rate_Per_100k"]
#     lag3 = hist.iloc[-3]["Crime_Rate_Per_100k"]

#     input_data = [[
#         state_enc.transform([state])[0],
#         year,
#         lag1, lag2, lag3
#     ]]

#     pred = model.predict(input_data)
#     result = target_enc.inverse_transform(pred)[0]

#     st.success(f"Predicted Crime Risk for {state} in {year}: **{result}**")


# import streamlit as st
# import pandas as pd
# import joblib

# # Load models
# model = joblib.load("crime_future_model.pkl")
# state_enc = joblib.load("state_encoder_A0.pkl")
# target_enc = joblib.load("target_encoder_A0.pkl")

# df = pd.read_csv("C:/Users/hp/Desktop/ML03/indian_crime_with_categories_ordered.csv ")

# # Page config
# st.set_page_config(page_title="Indian Crime Risk Prediction", page_icon="🚔", layout="centered")

# # Custom CSS
# st.markdown("""
# <style>
# body {
#     background-color: #f4f6f9;
# }
# .title {
#     text-align:center;
#     font-size:42px;
#     font-weight:bold;
# }
# .subtitle {
#     text-align:center;
#     font-size:18px;
#     color:gray;
# }
# .card {
#     background-color:white;
#     padding:30px;
#     border-radius:15px;
#     box-shadow:0px 0px 15px rgba(0,0,0,0.1);
# }
# .result {
#     text-align:center;
#     font-size:30px;
#     font-weight:bold;
#     padding:20px;
#     border-radius:12px;
# }
# </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown("<div class='title'>🚔 Indian Crime Risk Level Prediction</div>", unsafe_allow_html=True)
# st.markdown("<div class='subtitle'>Predict future crime risk for Indian states</div><br>", unsafe_allow_html=True)

# # Card UI
# st.markdown("<div class='card'>", unsafe_allow_html=True)

# state = st.selectbox("🏙 Select State", sorted(df["State"].unique()))
# year = st.number_input("📅 Enter Future Year", min_value=2023, max_value=2035)

# if st.button("🔮 Predict Crime Risk"):
#     hist = df[df["State"]==state].sort_values("Year").tail(3)

#     lag1 = hist.iloc[-1]["Crime_Rate_Per_100k"]
#     lag2 = hist.iloc[-2]["Crime_Rate_Per_100k"]
#     lag3 = hist.iloc[-3]["Crime_Rate_Per_100k"]

#     input_data = [[
#         state_enc.transform([state])[0],
#         year,
#         lag1, lag2, lag3
#     ]]

#     pred = model.predict(input_data)
#     result = target_enc.inverse_transform(pred)[0]

#     if result=="Low":
#         color = "#2ecc71"
#         emoji = "🟢"
#     elif result=="Medium":
#         color = "#f39c12"
#         emoji = "🟠"
#     else:
#         color = "#e74c3c"
#         emoji = "🔴"

#     st.markdown(
#         f"<div class='result' style='background-color:{color}; color:white;'>"
#         f"{emoji} {state} Crime Risk in {year}: {result}</div>",
#         unsafe_allow_html=True
#     )

# st.markdown("</div>", unsafe_allow_html=True)







# import streamlit as st
# import pandas as pd
# import joblib

# # Load models
# model = joblib.load("crime_future_model.pkl")
# state_enc = joblib.load("state_encoder_A0.pkl")
# target_enc = joblib.load("target_encoder_A0.pkl")

# df = pd.read_csv("C:/Users/hp/Desktop/ML03/indian_crime_with_categories_ordered.csv")

# # Page config
# st.set_page_config(
#     page_title="Indian Crime Risk Prediction",
#     page_icon="🚔",
#     layout="centered"
# )

# # ------------------ CSS ------------------
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Poppins', sans-serif;
# }

# .hero {
#     background: linear-gradient(135deg, #1f4037, #99f2c8);
#     padding: 40px;
#     border-radius: 20px;
#     color: white;
#     text-align: center;
#     margin-bottom: 30px;
# }

# .hero h1 {
#     font-size: 42px;
#     font-weight: 700;
# }

# .hero p {
#     font-size: 18px;
#     opacity: 0.9;
# }

# .card {
#     background: rgba(255,255,255,0.9);
#     padding: 35px;
#     border-radius: 20px;
#     box-shadow: 0 10px 30px rgba(0,0,0,0.12);
# }

# .stButton>button {
#     width: 100%;
#     background: linear-gradient(135deg, #667eea, #764ba2);
#     color: white;
#     font-size: 18px;
#     padding: 14px;
#     border-radius: 12px;
#     border: none;
#     font-weight: 600;
# }

# .stButton>button:hover {
#     transform: scale(1.02);
#     transition: 0.3s;
# }

# .result-box {
#     margin-top: 30px;
#     padding: 25px;
#     border-radius: 18px;
#     text-align: center;
#     font-size: 30px;
#     font-weight: 700;
#     animation: fadeIn 1s ease-in-out;
# }

# @keyframes fadeIn {
#     from {opacity: 0; transform: translateY(15px);}
#     to {opacity: 1; transform: translateY(0);}
# }
# </style>
# """, unsafe_allow_html=True)

# # ------------------ HERO ------------------
# st.markdown("""
# <div class="hero">
#     <h1>🚔 Indian Crime Risk Prediction</h1>
#     <p>AI-powered prediction of future crime risk levels across Indian states</p>
# </div>
# """, unsafe_allow_html=True)

# # ------------------ CARD ------------------
# st.markdown("<div class='card'>", unsafe_allow_html=True)

# state = st.selectbox("🏙 Select Indian State", sorted(df["State"].unique()))
# year = st.number_input("📅 Select Future Year", min_value=2024, max_value=2035, step=1)

# if st.button("🔮 Predict Crime Risk"):
#     hist = df[df["State"] == state].sort_values("Year").tail(3)

#     lag1 = hist.iloc[-1]["Crime_Rate_Per_100k"]
#     lag2 = hist.iloc[-2]["Crime_Rate_Per_100k"]
#     lag3 = hist.iloc[-3]["Crime_Rate_Per_100k"]

#     input_data = [[
#         state_enc.transform([state])[0],
#         year,
#         lag1, lag2, lag3
#     ]]

#     pred = model.predict(input_data)
#     result = target_enc.inverse_transform(pred)[0]

#     if result == "Low":
#         bg = "#2ecc71"
#         emoji = "🟢"
#     elif result == "Medium":
#         bg = "#f39c12"
#         emoji = "🟠"
#     else:
#         bg = "#e74c3c"
#         emoji = "🔴"

#     st.markdown(
#         f"""
#         <div class="result-box" style="background:{bg}; color:white;">
#             {emoji} {state} Crime Risk in {year}: {result}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown("</div>", unsafe_allow_html=True)














# import streamlit as st
# import pandas as pd
# import joblib

# # ------------------ PAGE CONFIG ------------------
# st.set_page_config(
#     page_title="Indian Crime Risk Prediction",
#     page_icon="🚔",
#     layout="centered"
# )

# # ------------------ LOAD MODELS ------------------
# model = joblib.load("crime_future_model.pkl")
# state_enc = joblib.load("state_encoder_A0.pkl")
# target_enc = joblib.load("target_encoder_A0.pkl")

# # ------------------ LOAD DATA ------------------
# df = pd.read_csv(
#     "C:/Users/hp/Desktop/ML03/indian_crime_with_categories_ordered.csv"
# )

# # ------------------ CSS ------------------
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Inter', sans-serif;
#     background-color: #f5f7fa;
# }

# /* HEADER */
# .header {
#     background-color: #1f3c88;
#     padding: 32px;
#     border-radius: 16px;
#     color: white;
#     text-align: center;
#     margin-bottom: 22px;
# }

# .header h1 {
#     font-size: 36px;
#     font-weight: 700;
#     margin-bottom: 6px;
# }

# .header p {
#     font-size: 16px;
#     opacity: 0.9;
# }

# /* CARD */
# .card {
#     background: white;
#     padding: 28px;
#     border-radius: 16px;
#     box-shadow: 0 6px 18px rgba(0,0,0,0.08);
# }

# /* BUTTON */
# .stButton > button {
#     width: 100%;
#     background-color: #1f3c88;
#     color: white;
#     font-size: 16px;
#     padding: 12px;
#     border-radius: 10px;
#     font-weight: 600;
#     border: none;
# }

# .stButton > button:hover {
#     background-color: #162d66;
# }

# /* RESULT */
# .result {
#     margin-top: 24px;
#     padding: 18px;
#     border-radius: 12px;
#     text-align: center;
#     font-size: 26px;
#     font-weight: 700;
# }
# </style>
# """, unsafe_allow_html=True)

# # ------------------ HEADER ------------------
# st.markdown("""
# <div class="header">
#     <h1>🚔 Indian Crime Risk Prediction</h1>
#     <p>AI-based prediction of future crime risk levels across Indian states</p>
# </div>
# """, unsafe_allow_html=True)

# # ------------------ INPUT CARD ------------------
# st.markdown("<div class='card'>", unsafe_allow_html=True)

# state = st.selectbox(
#     "🏙 Select Indian State",
#     sorted(df["State"].unique())
# )

# year = st.number_input(
#     "📅 Select Future Year",
#     min_value=2024,
#     max_value=2035,
#     step=1
# )

# if st.button("🔮 Predict Crime Risk"):
#     # Last 3 years data for lag features
#     hist = (
#         df[df["State"] == state]
#         .sort_values("Year")
#         .tail(3)
#     )

#     lag1 = hist.iloc[-1]["Crime_Rate_Per_100k"]
#     lag2 = hist.iloc[-2]["Crime_Rate_Per_100k"]
#     lag3 = hist.iloc[-3]["Crime_Rate_Per_100k"]

#     input_data = [[
#         state_enc.transform([state])[0],
#         year,
#         lag1,
#         lag2,
#         lag3
#     ]]

#     prediction = model.predict(input_data)
#     result = target_enc.inverse_transform(prediction)[0]

#     if result == "Low":
#         bg_color = "#2ecc71"
#         emoji = "🟢"
#     elif result == "Medium":
#         bg_color = "#f39c12"
#         emoji = "🟠"
#     else:
#         bg_color = "#e74c3c"
#         emoji = "🔴"

#     st.markdown(
#         f"""
#         <div class="result" style="background-color:{bg_color}; color:white;">
#             {emoji} {state} Crime Risk in {year}: {result}
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown("</div>", unsafe_allow_html=True)

# # ------------------ FOOTER ------------------
# st.markdown(
#     "<p style='text-align:center; color:gray; margin-top:18px;'>"
#     "Final Year Machine Learning Project | Indian Crime Risk Level Prediction"
#     "</p>",
#     unsafe_allow_html=True
# )









import streamlit as st
import pandas as pd
import joblib

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Indian Crime Risk Prediction",
    page_icon="🚔",
    layout="centered"
)

# ------------------ LOAD MODELS ------------------
model = joblib.load("crime_future_model.pkl")
state_enc = joblib.load("state_encoder_A0.pkl")
target_enc = joblib.load("target_encoder_A0.pkl")

# ------------------ LOAD DATA ------------------
df = pd.read_csv(
    "C:/Users/hp/Desktop/ML03/indian_crime_with_categories_ordered.csv"
)

# ------------------ HEADER ------------------
st.markdown(
    """
    <h1 style="text-align:center;">🚔 Indian Crime Risk Prediction</h1>
    <p style="text-align:center;">
    AI-based prediction of future crime risk levels across Indian states
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# ------------------ INPUTS (NO WRAPPERS) ------------------
state = st.selectbox(
    "🏙 Select Indian State",
    sorted(df["State"].unique())
)

year = st.number_input(
    "📅 Select Future Year",
    min_value=2024,
    max_value=2035,
    step=1
)

# ------------------ BUTTON ------------------
if st.button("🔮 Predict Crime Risk"):
    hist = (
        df[df["State"] == state]
        .sort_values("Year")
        .tail(3)
    )

    lag1 = hist.iloc[-1]["Crime_Rate_Per_100k"]
    lag2 = hist.iloc[-2]["Crime_Rate_Per_100k"]
    lag3 = hist.iloc[-3]["Crime_Rate_Per_100k"]

    input_data = [[
        state_enc.transform([state])[0],
        year,
        lag1,
        lag2,
        lag3
    ]]

    prediction = model.predict(input_data)
    result = target_enc.inverse_transform(prediction)[0]

    if result == "Low":
        st.success(f"🟢 {state} Crime Risk in {year}: LOW")
    elif result == "Medium":
        st.warning(f"🟠 {state} Crime Risk in {year}: MEDIUM")
    else:
        st.error(f"🔴 {state} Crime Risk in {year}: HIGH")

# ------------------ FOOTER ------------------
st.markdown(
    "<hr><p style='text-align:center;'>Final Year Machine Learning Project | Indian Crime Risk Level Prediction</p>",
    unsafe_allow_html=True
)





