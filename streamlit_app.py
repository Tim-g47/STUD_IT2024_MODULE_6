import streamlit as st
import requests


st.title("Prediction class site!")

file = st.file_uploader("Choose file CSV")

files = {'f': file}

if st.button("Prediction"):
    response = requests.post(url = " http://127.0.0.1:8090/predict", files = files)

    st.success(response.text[1:-1])

    # print(response.status_code == requests.codes.ok)ss
    # print(response.text)
    # with open("csv_file.csv", "w", encoding="utf-8") as file:
    #     file.write(response.text)
    # file_csv = open("csv_file.csv", "w", encoding="utf-8")
    # st.download_button('Download file', file_csv)
    # with open('myfile.zip', 'rb') as f:
    #     st.download_button('Download Zip', f, file_name='archive.zip')

# if st.button("Instruction"):
st.page_link("https://disk.yandex.ru/i/Y9aBVuhEOQUe_g", label="Instruction")