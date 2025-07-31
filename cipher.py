import streamlit as st
from caesar_cipher import caesar_cipher


st.text_input("ENCRYPT YOUR MESSAGE WITH THE CAESAR CIPHER", key="name")

res = caesar_cipher(st.session_state.name)

archivo_audio = "Audios/ArchivosEncriptadosExitosamente.mp3"


checkbox_1 = st.checkbox("Caesar Cipher")
checkbox_2 = st.checkbox("Transposition cipher")
button_3 = st.button("Affine ciphers", type="primary")


if checkbox_1:

     st.write('Result for Caesar cipher: ')
     st.write(res[0])

    
if checkbox_2:

    st.write('Result for Transposition cipher: ', res[1])

if button_3:

    st.audio(archivo_audio, format="audio/mp3", autoplay = True)