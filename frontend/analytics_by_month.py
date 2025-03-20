from os.path import exists
import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from unicodedata import category

API_URL="http://localhost:8000"

def analytics_by_month():

	if st.button("Get Analytics"):
		response = requests.get(f"{API_URL}/analytics/")
		data = response.json()
		df = pd.DataFrame(data)


		st.bar_chart(data = df.set_index("month"), width =0, height = 0, use_container_width=5)
		df["Total"] = df["Total"].map("${:.2f}".format)
		st.table(df)



