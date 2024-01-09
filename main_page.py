import streamlit as st
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.markdown('# Main page')
st.write("Hello, world!")

st.sidebar.markdown('# Main page 🎈')

left_column, right_column = st.columns(2)

left_column.button("Press Me!")

with right_column:
    chosen = st.radio(
            'Sorting Hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write("You are in {}".format(chosen))
