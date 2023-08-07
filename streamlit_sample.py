
import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_title='LoL Ban/Pick Dashboard',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Define your custom CSS
blue_custom_css = """
<style>
.blue-column {
    background-color: blue;
    padding: 30px;
    border-radius: 0px;
    text-align: left; 
    font-size: 30px;
    left: 5px;
    margin: 5px
}
"""
red_custom_css = """
.red-column {
    background-color: red;
    padding: 30px;
    border-radius: 0px;    
    text-align: left; 
    font-size: 30px ;
    left: 5px;
    margin: 5px
}
</style>
"""

def main():
    st.title('LoL Ban/Pick Dashboard 2023')
    team_body()
#     cs_body()

    return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def team_body(): 
    col1,col2 = st.columns(2)
    team_select_box = st.selectbox('select a team', ["Option 1", "Option 2", "Option 3"])
    with col1:
        
        col1_1, col1_2 = st.columns([1,3])
        with col1_1:
#             st.markdown(blue_custom_css, unsafe_allow_html=True)
            st.markdown(blue_custom_css,'Blue', unsafe_allow_html=True)
        with col1_2:
#             st.markdown(blue_custom_css, unsafe_allow_html=True)
            st.markdown(f"{team_select_box}")
#     with col1: 
#         st.markdown('<div class="blue-column">Blue</div>', unsafe_allow_html=True)
#         st.selectbox('select a team', ["Option 1", "Option 2", "Option 3"])
    
#     with col2:    
#         st.markdown('<div class="red-column">Red</div>', unsafe_allow_html=True)


if __name__ == '__main__':
     main()
