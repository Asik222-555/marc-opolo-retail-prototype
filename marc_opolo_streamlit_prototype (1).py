
import streamlit as st

st.set_page_config(page_title="Marc O'Polo Prototype", layout="wide")

st.title("🛍️ Marc O'Polo Kazakhstan – Hybrid Retail Experience")

tab1, tab2, tab3 = st.tabs(["🧠 AI Tutor", "🧵 Product Filter", "🏪 Try in Store Reservation"])

with tab1:
    st.header("🧠 AI Tutor for Product Understanding")
    st.write("This tool helps users understand materials, styles, and matchups.")
    user_question = st.text_input("Enter your question (e.g., 'What is smart casual?')")
    if user_question:
        st.markdown(f"**AI Tutor Response:** Smart casual is a dress code that blends well-fitted, polished business wear with elements of casual attire...")

with tab2:
    st.header("🧵 Filter Marc O'Polo Products")
    style = st.selectbox("Choose Style", ["Smart Casual", "Business", "Casual", "Sport"])
    category = st.selectbox("Choose Category", ["Sweaters", "Pants", "Coats", "Shirts"])
    if st.button("Apply Filters"):
        st.success(f"Showing results for **{style}** style in **{category}** category")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Marc_O%27Polo_Logo.svg/2560px-Marc_O%27Polo_Logo.svg.png", width=200)
        st.caption("Example Item: Smart Casual Wool Sweater")

with tab3:
    st.header("🏪 Try In Store")
    st.write("Reserve a product for fitting in a nearby store")
    city = st.selectbox("City", ["Almaty", "Astana", "Shymkent"])
    store = st.selectbox("Select Store", ["Mega Center", "Dostyk Plaza", "Esentai Mall"])
    date = st.date_input("Choose fitting date")
    time = st.time_input("Choose time")
    phone = st.text_input("Enter phone number for confirmation")
    if st.button("Reserve Item"):
        st.success(f"Item reserved at {store} in {city} on {date} at {time}. Confirmation will be sent to {phone}.")
