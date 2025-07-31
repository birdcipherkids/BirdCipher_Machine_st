import streamlit as st

st.header('Login procedures')
login, passcreator = st.tabs(['Log in', 'Password creator'])

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		col1, col2 = st.columns([3, 1])

		col1.subheader('Log in to BirdCipher Machine!')
		col1.text_input('Username', key = 'username', width = 500)
		col1.text_input('Password', key = 'main_password', width = 500)
		col1.text_input('Role', key = 'role', width = 500)
		col1.form_submit_button('Send data')

		col2.image('Images/BirdCipher-logo.png')

