import streamlit as st
import pandas as pd
import plotly.express as px

# Dashboard Setup
st.set_page_config(page_title="Ashu Productivity Pro", layout="wide")

st.title("📊 Personal Productivity & Screen Time Analyzer")
st.markdown("Track your daily study vs social media trends.")

# --- DUMMY DATA (Aap ise baad mein Google Sheets/CSV se connect kar sakte hain) ---
data = {
    'Category': ['Study (SQL/Python)', 'Social Media', 'Entertainment', 'Productive Work', 'Gaming'],
    'Hours': [5, 2.5, 1.5, 3, 1],
    'Type': ['Productive', 'Unproductive', 'Unproductive', 'Productive', 'Unproductive']
}
df = pd.DataFrame(data)

# --- CALCULATED KPIs (Like DAX) ---
total_hours = df['Hours'].sum()
productive_hours = df[df['Type'] == 'Productive']['Hours'].sum()
productivity_score = (productive_hours / total_hours) * 100

# --- METRICS SECTION ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Screen Time", f"{total_hours} hrs")
col2.metric("Productive Time", f"{productive_hours} hrs", "Goal: 6 hrs")
col3.metric("Productivity Score", f"{productivity_score:.1f}%", "Target: 70%")

st.divider()

# --- CHARTS SECTION ---
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Category-wise Time Distribution")
    fig_bar = px.bar(df, x='Category', y='Hours', color='Type', 
                     color_discrete_map={'Productive': '#2ecc71', 'Unproductive': '#e74c3c'})
    st.plotly_chart(fig_bar, width='stretch')

with right_col:
    st.subheader("Productive vs Unproductive Share")
    fig_pie = px.pie(df, values='Hours', names='Type', hole=0.5,
                     color='Type', color_discrete_map={'Productive': '#2ecc71', 'Unproductive': '#e74c3c'})
    st.plotly_chart(fig_pie, width='stretch')

# --- DATA TABLE ---
st.subheader("Weekly Activity Log")
st.dataframe(df, width='stretch')

st.success("Keep it up, Ashu! Aaj ka score badhiya hai. 🚀")
