import streamlit as st
from azure.storage.blob import BlobServiceClient

# Azure接続情報
CONNECTION_STRING = 'DefaultEndpointsProtocol=https;AccountName=adachitakehiro;AccountKey=adSQfl85W6VyYuuZgxJa6lV+v13GEmbPsXZ9ImS5oJ8nyOe0woYlaHEYEOtSoZtUqc9hDa0NlNlI+ASt8k+AAg==;EndpointSuffix=core.windows.net'
CONTAINER_NAME = 'democontainer1'
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

def save_to_blob(file):
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file.name)
    blob_client.upload_blob(file.getvalue())

st.title('Azure Blob Storage Uploader')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    save_to_blob(uploaded_file)
    st.success('File uploaded to Azure Blob Storage!')
