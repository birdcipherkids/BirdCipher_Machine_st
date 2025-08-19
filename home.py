import streamlit as st
from cards import (login_card, social_engineering, hashing, cryptography, messaging,
	digital_signature)

col_init1, col_init2 = st.columns([2,1])

with col_init1:
	st.header('BirdCipher Tool Explorer')

with col_init2:
	st.image('Images/BirdCipher-logo.png', width = 120)

cols = st.columns(2)

with cols[0].container(height = 310):

	login_card()

with cols[1].container(height = 310):

	social_engineering()

with cols[0].container(height = 310):

	hashing()

with cols[1].container(height = 310):

	cryptography()

with cols[0].container(height = 310):

	messaging()

with cols[1].container(height = 310):

	digital_signature()





