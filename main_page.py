import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠"
)

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
