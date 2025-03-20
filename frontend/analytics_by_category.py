from os.path import exists
import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from unicodedata import category

API_URL="http://localhost:8000"

def analytics_by_category():
	col1, col2 = st.columns(2)
	with col1:
		start_date = st.date_input("Start Date:", datetime(2024,8,1))

	with col2:
		end_date = st.date_input("End Date:", datetime(2024, 8, 5))

	if st.button("Get Analytics By Category"):
		payload = {
			"start_date": start_date.strftime("%Y-%m-%d"),
			"end_date": end_date.strftime("%Y-%m-%d")
		}
		response = requests.post(f"{API_URL}/analytics", json = payload)
		data = response.json()
		df = pd.DataFrame({
			"Category": list(data.keys()),
			"Total": [data[category]["total"] for category in data],
			"Percentage": [data[category]["percentage"] for category in data]
		})
		df_sorted = df.sort_values(by="Percentage", ascending=False)
		st.title("Expense Breakdown by Category")
		st.bar_chart(data = df_sorted.set_index("Category")["Percentage"], width =0, height = 0, use_container_width=5)
		df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
		df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
		st.table(df_sorted)


