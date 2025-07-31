import streamlit as st
from functions_birdcipher import *


audio_login_created = 'Audios/NewUserCreated.mp3'
st.header('Login procedures')
login, passcreator = st.tabs(['Log in', 'Password creator'])

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		col1, col2 = st.columns([3, 1])

		dynamic_value = ''

		with col1:

			st.subheader('Log in to BirdCipher Machine!')
			user = st.text_input('Username', key = 'username', width = 500)
			passw = st.text_input('Password', key = 'main_password', width = 500)
			role_login = st.text_input('Role', key = 'role', width = 500)
			submit_button = st.form_submit_button('Send data', type="primary")

			if submit_button:

				print(user)
				dynamic_value = login_user(user, passw, role_login)
				st.audio(audio_login_created, format="audio/mp3", autoplay = True)

		with col2:

			col2.image('Images/BirdCipher-logo.png')



	hash_login = st.text_input('Your password hash (SHA 256) is:', value = dynamic_value)
	#st.multiselect("Multiselect", options=["A", "B", "C"])


	



