import streamlit as st
from functions_birdcipher import *

bambu_sound = 'Audios/bambu_click.mp3'
audio_login_created = 'Audios/NewUserCreated.mp3'
audio_login_correct = 'Audios/CorrectLogin.mp3'


st.header('Welcome to BirdCipher Machine')
login, passcreator = st.tabs(['Log in', 'Password creator'])

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		col1, col2 = st.columns([3, 1])

		dynamic_value = ['', '']

		with col1:

			st.subheader('Log in to BirdCipher')
			user = st.text_input('Username', key = 'username', width = 500)
			passw = st.text_input('Password', key = 'main_password', width = 500)
			role_login = st.text_input('Role', key = 'role', width = 500)
			submit_button = st.form_submit_button('Send data', type="primary")

			if submit_button:

				print(user)
				dynamic_value = login_user(user, passw, role_login)
				st.audio(bambu_sound, format = 'audio/mp3', autoplay = True)

				if dynamic_value[1] == 'New':

					st.audio(audio_login_created, format = 'audio/mp3', autoplay = True)
					#hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = dynamic_value[0])

				elif dynamic_value[1] == 'Old':

					st.audio(audio_login_correct, format = 'audio/mp3', autoplay = True)
					#hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = dynamic_value[0])

		with col2:

			col2.image('Images/BirdCipher-logo.png')


hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = dynamic_value[0])







	



