import streamlit as st
from caesar_cipher import caesar_cipher

pages = [
    st.Page(
        "home.py",
        title="Home",
        icon=":material/home:"
    ),
    st.Page(
        'login.py',
        title = 'Login',
        icon = ':material/passkey:'),
    st.Page(
        'social_eng.py',
        title = 'Social Engineering',
        icon = ':material/psychology:'),
    st.Page(
        "cipher.py",
        title="Caesar cipher",
        icon=":material/key:"
    ),

]

page = st.navigation(pages)
page.run()



with st.sidebar.container(height=310):

    if page.title == 'Home':

        st.page_link("home.py", label="Home")

    elif page.title == 'Login':

        st.page_link("login.py", label="Login")

    elif page.title == 'Social Engineering':

        st.page_link('social_eng.py', label = 'Social engineering')

    elif page.title == 'Caesar cipher':

        st.page_link("cipher.py", label="Caesar cipher")



    
    




    






