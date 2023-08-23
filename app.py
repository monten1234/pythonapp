import streamlit as st
from azure.storage.blob import BlobServiceClient

# Azure接続情報
CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=adachitakehiro;AccountKey=B3Px4aJ9dBCJJQAkCW6ZRDJFqYk7E6EYNgosHvbloU3+6QTNV2cmq/w3vFtpj0C4eMvA2VzscIv7+ASt61DFww==;EndpointSuffix=core.windows.net'
CONTAINER_NAME = 'democontainer1'
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

def save_to_blob(file):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.name)
    blob_client.upload_blob(file.getvalue())

    # ファイルのURLを取得
    blob_url = blob_client.url
    return blob_url

st.title('Azure Blob Storage Uploader')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    url = save_to_blob(uploaded_file)
    st.success(f'File uploaded to Azure Blob Storage! URL: {url}')