import streamlit as st
from cards import (login_card, social_engineering, hashing, cryptography, messaging,digital_signature)
import psycopg2


myConnection = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

myCursor = myConnection.cursor()
sql123 = 'select * from language where id = (%s)'
sql123_data = (1,)
myCursor.execute(sql123, sql123_data)
dltr = myCursor.fetchall()
lang = dltr[0][1]

myConnection.commit()
myConnection.close()

col_lang1, col_lang2 = st.columns(2)

with col_lang1:

	english_button = st.button('English', type = 'primary')

with col_lang2:

	spanish_button = st.button('Español', type = 'primary')


col_init1, col_init2 = st.columns([2,1])

with col_init1:

	if english_button:

		myConnection2 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
			user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

		myCursor2 = myConnection2.cursor()
		sql1231 = 'update language set languag = (%s) where id = (%s)'
		sql1231_data = ('English', 1)
		myCursor2.execute(sql1231, sql1231_data)
		myCursor2.execute(sql123, sql123_data)
		dltr1 = myCursor2.fetchall()
		lang = dltr1[0][1]

		myConnection2.commit()
		myConnection2.close()


	if spanish_button:

		myConnection3 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
			user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

		myCursor3 = myConnection3.cursor()
		sql1232 = 'update language set languag = (%s) where id = (%s)'
		sql1232_data = ('Español', 1)
		myCursor3.execute(sql1232, sql1232_data)
		myCursor3.execute(sql123, sql123_data)
		dltr2 = myCursor3.fetchall()
		lang = dltr2[0][1]

		myConnection3.commit()
		myConnection3.close()

	welcome = st.empty()

	if lang == 'English':

		welcome.header('BirdCipher Tool Explorer')

	elif lang == 'Español':

		welcome.header('Explorador de Birdcipher')
	

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







