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
	st.image('Images/Social engineering-logo.png', width = 290, use_container_width = True)


def hashing():

	st.page_link('hashing.py', label = 'Hashing', icon = ':material/encrypted:')
	st.image('Images/Hashing-logo.png', use_container_width = True)

def cryptography():

	st.page_link('cipher.py', label = 'Classic Cryptography', icon = ':material/encrypted_add_circle:')
	st.image('Images/Cryptography-logo.png', use_container_width = True)

def messaging():

	st.page_link('encrypted_messaging.py', label = 'Encrypted Messaging', icon = ':material/chat_apps_script:')
	st.image('Images/Crypto Messaging-logo.png', use_container_width = True)

def digital_signature():

	st.page_link('digital_signature.py', label = 'Digital Signature', icon = ':material/checkbook:')
	st.image('Images/Digital Signature-logo.png', use_container_width = True)
