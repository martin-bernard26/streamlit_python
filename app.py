import streamlit as st
import numpy as np
import pandas as pd


masukan = st.text_input("Masukan data")
if masukan!="":
  kumpulkan = [int(i) for i in masukan.split(",")]
  data = pd.DataFrame({'Nilai':kumpulkan})
  st.table(data)
  st.write(data.describe())
