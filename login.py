import streamlit as st

st.header('Login procedures')
login, passcreator = st.tabs(['Log in', 'Password creator'])

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		st.subheader('Log in to BirdCipher Machine!')
		st.text_input('Username', key = 'username', width = 400)
		st.text_input('Password', key = 'main_password', width = 400)
		st.text_input('Role', key = 'role', width = 400)
		st.form_submit_button('Send data')

