import streamlit as st
from azure.storage.blob import BlobServiceClient

# Azure接続情報
CONNECTION_STRING = 'YOUR_AZURE_STORAGE_CONNECTION_STRING'
CONTAINER_NAME = 'your-container-name'
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