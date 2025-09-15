import streamlit as st
from functions_birdcipher import *
import time

bambu_sound = 'Audios/bambu_click.mp3'
audio_login_created = 'Audios/Usuario_Creado.mp3'
audio_login_correct = 'Audios/Sesion_Iniciada.mp3'
audio_login_incorrect = 'Audios/Contrasena_Incorrecta.mp3'
audio_file_path = ''


st.header('Welcome to BirdCipher Machine')
login, face_recog, passcreator, passphrase, vault = st.tabs([
	'Log in', 'Face recognition', 'Password Generator', 'Passphrase Generator', 'Password Vault'])
dynamic_value = ['', '']
resulting_password = ['', '']
password_final = ''

with login:

	with st.form(key = 'login_button_form', enter_to_submit = False):

		col1, col2 = st.columns([2, 1])

		with col1:

			st.subheader('Sign in or create a new user on BirdCipher')
			user = st.text_input('Username', key = 'username', width = 500)
			passw = st.text_input('Password', key = 'main_password', type = 'password', width = 500)
			role_login = st.text_input('Role', key = 'role', width = 500)
			submit_button = st.form_submit_button('Send data', type="primary")

			if submit_button:

				dynamic_value = ['', '']
				evaluation_audios_es = ['Audios/caracter_especial.mp3', 'Audios/letra_mayuscula.mp3', 'Audios/letra_minuscula.mp3', 
				'Audios/numero_contrasena.mp3', 'Audios/Longitud_contrasena.mp3', 'Audios/Inicio_sesion_no_exitoso.mp3']
				data_breaches = ['Audios/Num_filtraciones_hibp_0.mp3', 'Audios/Num_filtraciones_hibp_1.mp3']
				print(user)
				dynamic_value = login_user(user, passw, role_login)
				audio_file_path = ''
				#st.audio(bambu_sound, format = 'audio/mp3', autoplay = True)

				placeholder = st.empty()

				with placeholder.container():

					if dynamic_value[1] == 'Weak':

						vid = check_master_password(passw)

						if vid[5] == False:

							audio_file_path = evaluation_audios_es[5]
							st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
							time.sleep(5)

						for i in range(len(vid) - 1):

							if vid[i] == False:

								audio_file_path = evaluation_audios_es[i]
								st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
								time.sleep(5)

					elif dynamic_value[1] == 'New':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_created
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						time.sleep(20)

					
					elif dynamic_value[1] == 'Old':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_correct
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						time.sleep(20)

					elif dynamic_value[1] == 'Incorrect':

						audio_file_path = bambu_sound
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						audio_file_path = audio_login_incorrect
						st.audio(audio_file_path, format = 'audio/mp3', autoplay = True)
						time.sleep(5)


				placeholder.empty()

				
		with col2:

			st.write('')
			st.write('')
			#col2.image('Images/BirdCipher-logo.png')
			col2.image('Images/HIBP.png')

			if submit_button:

				pass_hibp_breaches = hibp_breach(passw)
				placehold_hibp = st.empty()

				if pass_hibp_breaches:

					audio_hibp = data_breaches[1]
					st.audio(audio_hibp, format = 'audio/mp3', autoplay = True)

				else:

					audio_hibp = data_breaches[0]
					st.audio(audio_hibp, format = 'audio/mp3', autoplay = True)

				placehold_hibp.empty()

				hibp_rec = st.text_input('Password breaches: ', value = pass_hibp_breaches)


	#with st.form(key = 'second_authentication_form', enter_to_submit = False):

	enable_2fa = st.checkbox('Habilita segundo factor de autenticación')

	foto_facial = st.camera_input('Toma una foto', disabled = not enable_2fa)

	if foto_facial is not None:

		bytes_data = foto_facial.get_value()

		#send_face_recog = st.form_submit_button('Send data', type="primary")






	if dynamic_value[1] == 'New' or dynamic_value[1] == 'Old':

		hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = dynamic_value[0])


with passcreator:

	with st.form(key = 'password_button_form', enter_to_submit = False):

		pass_created_rand = 'Audios/Contrasena_creada_guardada_rand.mp3'
		pass_no_created_rand = 'Audios/contrasena_no_creada_rand.mp3'

		st.subheader('Create your random password')

		pass_length = st.slider('Select your password length', min_value = 10, max_value = 40, value = 20, width = 600)

		colm1, colm2, colm3, colm4 = st.columns(4)

		with colm1:

			uppercase_chr = st.checkbox("Upper case")

		with colm2:

			lowercase_chr = st.checkbox('Lower case')

		with colm3:

			numerical_chr = st.checkbox('Numerical')

		with colm4:

			special_chr = st.checkbox('Punctuation')

	
		st.subheader('Store the password in your vault')

		col_pass1, col_pass2 = st.columns([2,1])

		with col_pass1:

			app_input = st.text_input('Enter the app name for your password: ', width = 700)
			user_app_input = st.text_input('Enter your username for the app: ', width = 700)
			submit_password = st.form_submit_button('Save your password in vault', type = 'primary')

			if submit_password:

				resulting_password = ['', '']
				resulting_password = password_generator(pass_length, uppercase_chr, lowercase_chr, numerical_chr, special_chr)
				password_crtd = st.text_input('Your password is: ', key = 'password_cr', width = 500, value = resulting_password[0])
				hash_login = st.text_input('Your password hash (SHA 256) is:', width = 700, value = resulting_password[1])
				send_rand_ok = send_random_password(user_db, passw, app_input, user_app_input, password_crtd)

				if send_rand_ok:

					audio_file_path_rand = pass_created_rand
					st.audio(audio_file_path_rand, format = 'audio/mp3', autoplay = True)

				else:

					audio_file_path_rand = pass_no_created_rand
					st.audio(audio_file_path_rand, format = 'audio/mp3', autoplay = True)

		with col_pass2:

			col_pass2.image('Images/BirdCipher-logo-white.png')


with passphrase:

	with st.form(key = 'passphrase_button_form', enter_to_submit = False):

		rock_you_no_approved = 'Audios/Rock_you_yes.mp3'
		rock_you_approved = 'Audios/Rock_you_no.mp3'

		st.write('')
		
		col_words_pss, col_words_button_pss = st.columns(2, vertical_alignment = 'bottom')

		with col_words_pss:

			entry_words_pass_pss = st.text_input('Enter your secret word for password creation: ', width = 400)

		with col_words_button_pss:

			entry_words_button_pss = st.form_submit_button('Add word to your vault', type = 'primary')

			if entry_words_button_pss:

				#print(entry_words_pass)
				hackingword_results = query_rockyou(entry_words_pass_pss)

				if hackingword_results == True:

					audio_file_path_rockyou = rock_you_no_approved
					st.audio(audio_file_path_rockyou, format = 'audio/mp3', autoplay = True)

				elif hackingword_results == False:

					if login_check:

						words_inclusion(entry_words_pass_pss, user_db)
						audio_file_path_rockyou = rock_you_approved
						st.audio(audio_file_path_rockyou, format = 'audio/mp3', autoplay = True)

						
	with st.form(key = 'passphrase_send_form', enter_to_submit = False):

		col_passphr1, col_passphr2 = st.columns([2,1])

		with col_passphr1:

			st.subheader('Add passphrase to your vault')
		
			separators = st.radio('Define the separator for your secrets words:', [' $ ', ' . ', ' _ ', ' ! ', ' ? '], width = 'stretch', horizontal=True)
			passphrase_length = st.slider('Define the number of secret words for your password', min_value = 3, max_value = 10, value = 4,
				width = 500)

			app_passphrase = st.text_input('Enter the app for your password: ', width = 300)
			username_passphr = st.text_input('Enter your username for the app: ', width = 300)
			send_my_passphrase = st.form_submit_button('Add passphrase to your vault', type = 'primary')

			if send_my_passphrase:

				passphrase_final = split_secretwords(user_db, passphrase_length, separators)
				send_random_password(user_db, passw, app_passphrase, username_passphr, passphrase_final)
				passphrase_app = st.text_input('Your password for the app is: ', width = 500, value = passphrase_final)

		with col_passphr2:

			col_passphr2.image('Images/BirdCipher-passphrase.png')

		



with vault:

	with st.form(key = 'vault_button_form', enter_to_submit = False):

		st.subheader('Password vault')

		col_vault1, col_vault2 = st.columns([2,1])
		results_vault_for_app = ['','']

		# if 'username_app' not in st.session_state:

		# 	st.session_state['username_app'] = ''

		# if 'password_app' not in st.session_state:

		# 	st.session_state['password_app'] = ''


		with col_vault1:

			user_app_enquiry = st.text_input('Enter the app name to which you wish to login: ', width = 400)
			submit_vault = st.form_submit_button('Bring your password', type = 'primary')

			if submit_vault:

				results_vault_for_app = ['','']
				results_vault_for_app = bring_password(user_db, passw, user_app_enquiry)
				username_app_enquiry = st.text_input('Your username for this app is: ', width = 400, value = results_vault_for_app[0])
				password_app_enquiry = st.text_input('Your password for this app is: ', width = 400, value = results_vault_for_app[1])


		with col_vault2:

			col_vault2.image('Images/Merkaba.png')



#with face_recog:



	

