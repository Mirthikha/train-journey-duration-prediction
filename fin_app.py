import streamlit as st
import numpy as np
from model import train_model
from visuals_and_feat_analys import fin_table

st.title("Train journey duration prediction")

distance = st.slider("Distance", min_value=fin_table['Distance'].min(), max_value=fin_table['Distance'].max())

stops = st.slider("Stops", min_value=fin_table['Total_Stops'].min(), max_value=fin_table['Total_Stops'].max())


model=train_model()

input_val=np.array([[distance,stops]])

if st.button("PREDICT"):
    duration = model.predict(np.array([[distance, stops]]))
    duration = max(0.1, duration[0]) 
    st.write("Predicted duration in hours:", round(duration/3600,2))
