from os.path import exists
import streamlit as st
from add_update import add_update
from analytics_by_category import analytics_by_category
from analytics_by_month import analytics_by_month

st.title("Expense Management System")
tab1, tab2, tab3 = st.tabs(["Add/Update Expenses","Analytics By Category", "Analytics By Month"])

with tab1:
	add_update()
with tab2:
	analytics_by_category()
with tab3:
	analytics_by_month()

