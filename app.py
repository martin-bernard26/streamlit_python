import streamlit as st
import numpy as np
import pandas as pd


masukan = st.text_input("Masukan data")
if masukan!="":
  kumpulkan = [int(i) for i in masukan.split(",")]
  data = pd.DataFrame(kumpulkan,column=['Nilai'])
  st.table(data)
