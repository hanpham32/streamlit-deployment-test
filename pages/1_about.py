import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="About", page_icon="🦦")

st.markdown("# About ")
st.sidebar.markdown("# About ")

st.write("CS Undergrad @UWB")
st.write("See more at: [hanspham.com](https://hanspham.com)")

button(username="hanspham", floating=False, width=221)

rain(emoji="🌈", font_size=30, falling_speed=10, animation_length=5)
