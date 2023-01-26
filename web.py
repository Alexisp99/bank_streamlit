import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit_nested_layout
import streamlit.components.v1 as components

st.set_page_config(page_title = "AI Bank",
                   layout = "wide", 
                   )

#components.iframe("https://app.powerbi.com/reportEmbed?reportId=e084f06f-2b5d-49cb-94dd-dd3423fb222d&autoAuth=true&ctid=a2e466aa-4f86-4545-b5b8-97da7c8febf3")
#components.html('<iframe title="banque" width="1920" height="1080" src="https://app.powerbi.com/reportEmbed?reportId=e084f06f-2b5d-49cb-94dd-dd3423fb222d&autoAuth=true&ctid=a2e466aa-4f86-4545-b5b8-97da7c8febf3" frameborder="0" allowFullScreen="false"></iframe>')
st.markdown('<iframe title="banque" width="1920" height="1080" src="https://app.powerbi.com/reportEmbed?reportId=e084f06f-2b5d-49cb-94dd-dd3423fb222d&autoAuth=true&ctid=a2e466aa-4f86-4545-b5b8-97da7c8febf3" frameborder="0" allowFullScreen="false"></iframe>',unsafe_allow_html=True)