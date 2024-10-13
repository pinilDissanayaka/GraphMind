import streamlit as st

#app side bar
with st.sidebar:
    st.subheader("Upload the manifesto of the candidate.")
    
    uploaded_files = st.file_uploader(
    "Choose a PDF, TXT files", accept_multiple_files=True, type=["pdf", "txt"])
    
    
    for uploaded_file in uploaded_files:
        st.write("filename:", uploaded_file.name)
        
    if uploaded_files:
        with st.spinner("Processing..."):
            st.button("Upload to vector store.")
