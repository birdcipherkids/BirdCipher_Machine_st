import streamlit as st

def login_card():

	audio_login_created = 'Audios/NewUserCreated.mp3'

	st.page_link('login.py', label = 'Login', icon = ':material/passkey:')
	st.markdown('* :material/passkey: Login page')
	st.markdown('* :material/Password_2:  Random Password Generator')
	st.markdown('* :material/Key: Passphrase Generator')
	st.markdown('* :material/cloud_lock: Password Vault')
	st.audio(audio_login_created, format = 'audio/mp3')


def social_engineering():

	st.page_link('social_eng.py', label = 'Social Engineering', icon = ':material/psychology:')
	st.image('Images/Social engineering-logo.png', width = 290)
