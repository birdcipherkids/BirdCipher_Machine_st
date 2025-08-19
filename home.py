import streamlit as st
from cards import (login_card, social_engineering)

columns_init = st.columns(2)

with columns_init[0]:
	st.header('BirdCipher Tool Explorer')

with columns_init[1]:
	st.image('Images/BirdCipher-logo.png', width = 120)

cols = st.columns(2)

with cols[0].container(height = 310):

	login_card()

with cols[1].container(height = 310):

	social_engineering()