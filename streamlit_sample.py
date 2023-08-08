
import streamlit as st
from streamlit_sortables import sort_items
from pathlib import Path
import base64
import plotly.graph_objects as go
import numpy as np

# Initial page config

st.set_page_config(
     page_title='LoL Ban/Pick Dashboard',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Define your custom CSS
custom_css = """
<style>
    .blue-column {
    background-color: blue;
    padding: 0px;
    border-radius: 0px;
    border: 0px;
    text-align: left; 
    font-size: 30px;
    left: 10px;
    margin: 0px;
    font-family: Roboto;
}
    .stHorizontalBlock > div {
    margin-right: 0 !important;
    margin-left: 0 !important;
}
</style>
"""

def main():
    st.title('LoL Ban/Pick Dashboard 2023')
#     team_body()
#     cham_body()
    cal_body()
#     prob_body()
#     cs_body()

    return None

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# @st.cache_data
# def get_sorted_champ():
#     sorted_champ = cham_body()
#     value=sorted_champ[2]['items']
#     return value

def team_body():
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    """, unsafe_allow_html=True)

#     st.markdown(custom_css_string, unsafe_allow_html=True)
    
    team_items = [
        {'header': 'Blue', 'items': []},
        {'header': 'Red', 'items': []},
        {'header': 'Team', 'items': ['T1', 'Gen.G', 'Kwangdong', 'DRX', 'LSB', 'Nongsim', 'OKB', 'DK', 'KT', 'Hanwha']}
    ]
    sorted_team = sort_items(team_items, multi_containers=True, direction="horizontal",key="1")
    return sorted_team
#     sorted_items = sort_items(sorted_items, multi_containers=True, direction="horizontal", key="1")
#     st.write(sorted_items)

def cham_body():
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    """, unsafe_allow_html=True)

#     st.markdown(custom_css_string, unsafe_allow_html=True)
    
    champ_items = [
        {'header': 'Blue Champions', 'items': []},
        {'header': 'Red Champions', 'items': []},
        {'header': 'Champions', 'items': ['AAtrox', 'Ahri', 'champ1', 'champ2', 'champ3']}
    ]
    sorted_champ = sort_items(champ_items, multi_containers=True, direction="horizontal",key="2")
    return sorted_champ

def cal_body(): 
    sorted_team=team_body()
    sorted_champ=cham_body()
        # Create the data
    gauge_data = {
        'value': 80,
        'min': 0,
        'max': 100,
        'units': '%'
    }

    # Create the gauge plot
    gauge_plot = go.Indicator(
        mode='gauge',
        value=gauge_data['value'],
#         min=gauge_data['min'],
#         max=gauge_data['max'],
#         units=gauge_data['units'],
        title='Gauge Plot'
    )
    
    
#     if get_sorted_champ() != sorted_champ:
#         gauge_data['value'] = np.random.randint(0, 100)
    
    # Display the gauge plot
    fig = go.Figure(data=[gauge_plot])
    st.plotly_chart(fig)
    st.markdown(sorted_champ[2]['items'])

if __name__ == '__main__':
     main()
