import streamlit as st
from functions_birdcipher import *
import time

bambu_sound = 'Audios/bambu_click.mp3'
audio_login_created = 'Audios/NewUserCreated.mp3'
audio_login_correct = 'Audios/CorrectLogin.mp3'
audio_login_incorrect = 'Audios/Incorrect_password.mp3'
audio_file_path = ''


st.header('Welcome to BirdCipher Machine')
login, passcreator = st.tabs(['Log in', 'Password creator'])
dynamic_value = ['', '']
resulting_password = ['', '']

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		col1, col2 = st.columns([3, 1])

		with col1:

			st.subheader('Log in to BirdCipher')
			user = st.text_input('Username', key = 'username', width = 500)
			passw = st.text_input('Password', key = 'main_password', width = 500)
			role_login = st.text_input('Role', key = 'role', width = 500)
			submit_button = st.form_submit_button('Send data', type="primary")

			if submit_button:

				dynamic_value = ['', '']
				print(user)
				dynamic_value = login_user(user, passw, role_login)
				audio_file_path = ''
				#st.audio(bambu_sound, format = 'audio/mp3', autoplay = True)

				placeholder = st.empty()

				with placeholder.container():

					if dynamic_value[1] == 'New':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_created
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)

					
					elif dynamic_value[1] == 'Old':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_correct
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)

					elif dynamic_value[1] == 'Incorrect':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_incorrect
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)


				time.sleep(13)
				placeholder.empty()

				
		with col2:

			col2.image('Images/BirdCipher-logo.png')


with passcreator:

	st.header('Password generator')

	pass_length = st.slider('Select your password length', min_value = 10, max_value = 40, value = 10)

	colm1, colm2, colm3, colm4 = st.columns(4)

	with colm1:

		uppercase_chr = st.checkbox("Upper case")

	with colm2:

		lowercase_chr = st.checkbox('Lower case')

	with colm3:

		numerical_chr = st.checkbox('Numerical')

	with colm4:

		special_chr = st.checkbox('Special characters')

	create_pass_button = st.button('Create password', type = 'primary')

	if create_pass_button:

		resulting_password = ['', '']
		resulting_password = password_generator(pass_length, uppercase_chr, lowercase_chr, numerical_chr, special_chr)
		password_crtd = st.text_input('Your password is: ', key = 'password_cr', width = 500, value = resulting_password[0])
		hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = resulting_password[1])





hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = dynamic_value[0])







	



