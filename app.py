import streamlit as st
import os
from main import convert_markdown_file

def save_uploaded_file(uploaded_file):
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)

def main():
    st.set_page_config(page_title="Markdown to HTML")

    st.title(":green[Markdown] to :blue[HTML]")
    st.markdown("This is a simple tool to convert your markdown file to a basic HTML webpage.")
    st.markdown("Just upload your markdown file and click on the convert button to get your HTML file.")

    uploaded_file = st.file_uploader(label="Upload .md file", type="md")

    # if md_file and st.button("Convert"):
    #     convert_markdown_file(md_file, "index.html")

    if uploaded_file is not None:
        save_path = save_uploaded_file(uploaded_file)
        st.write(f"File {uploaded_file.name} uploaded successfully.")

        if st.button("Convert"):
            output_file = os.path.splitext(uploaded_file.name)[0] + ".html"
            convert_markdown_file(save_path, output_file)

            with open(output_file, 'r') as f:
                st.download_button(
                    label="Download HTML file",
                    data=f,
                    file_name=output_file,
                    mime="text/html"
                )

if __name__ == "__main__":
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    main()