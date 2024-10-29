import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt


masukan = st.text_input("Masukan data")
if masukan!="":
  kumpulkan = [int(i) for i in masukan.split(",")]
  panjang = len(kumpulkan)
  data = pd.DataFrame({'Nilai':kumpulkan})
  st.table(data)
  plt.pyplot.scatter(np.arange(panjang),np.array(kumpulkan))
  st.write(data.describe())
