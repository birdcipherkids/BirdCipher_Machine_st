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
        'hashing.py',
        title = 'Hashing',
        icon = ':material/encrypted:'),
    st.Page(
        'cipher.py',
        title = 'Cryptography',
        icon = ':material/key:'),
    st.Page(
        'encrypted_messaging.py',
        title = 'Messaging',
        icon = ':material/chat_apps_script:'),
    st.Page(
        'digital_signature.py',
        title = 'Digital Signature',
        icon = ':material/checkbook:')

]

page = st.navigation(pages)
page.run()



with st.sidebar.container(height=310):

    if page.title == 'Home':

        st.page_link("home.py", label = 'Home')

    elif page.title == 'Login':

        st.page_link("login.py", label = 'Login')

    elif page.title == 'Social Engineering':

        st.page_link('social_eng.py', label = 'Social engineering')

    elif page.title == 'Hashing':

        st.page_link('hashing.py', label = 'Hashing')

    elif page.title == 'Cryptography':

        st.page_link('cipher.py', label = 'Caesar cipher')

    elif page.title == 'Messaging':

        st.page_link('encrypted_messaging.py', label = 'Encrypted Messaging')

    elif page.title == 'Digital Signature':

        st.page_link('digital_signature.py', label = 'Digital Signature')



    
    




    






