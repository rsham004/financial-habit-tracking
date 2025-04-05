from os.path import exists
import streamlit as st

from add_update import add_update
from analytics_by_category import analytics_by_category
from analytics_by_month import analytics_by_month

# Configure PostgreSQL connection
conn = st.connection('postgresql', type='sql')
conn.connect(
    url=st.secrets.db_credentials.url,
    # Or use individual parameters:
    # host=st.secrets.db_credentials.host,
    # port=st.secrets.db_credentials.port,
    # user=st.secrets.db_credentials.username,
    # password=st.secrets.db_credentials.password,
    # database=st.secrets.db_credentials.database
)

st.title("Expense Management System")
tab1, tab2, tab3 = st.tabs(["Add/Update Expenses","Analytics By Category", "Analytics By Month"])

with tab1:
	add_update()
with tab2:
	analytics_by_category()
with tab3:
	analytics_by_month()

