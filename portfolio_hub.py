import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE CONFIG
st.set_page_config(page_title="Ashutosh | Data Analytics Hub", layout="wide", page_icon="📊")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Project Navigator")
project = st.sidebar.selectbox(
    "Choose a Domain to Analyze:",
    ["Portfolio Home", "Sustainability Tracker", "Productivity Analyzer", "Traffic Safety", 
     "Job Market Trends", "Movie Success", "Freelance Tracker", "Social Media Trends", 
     "Food Delivery", "Review Auditor", "EdTech Analytics"]
)

st.sidebar.markdown("---")
st.sidebar.info(f"👤 **Ashutosh Dubey**\n\n🎓 **BCA Student**\n\n🛠️ **Tech Stack:** Python, SQL, Streamlit, Power BI")

# --- 1. HOME PAGE ---
if project == "Portfolio Home":
    st.title("🌟 Multi-Domain Data Analytics Portfolio")
    st.subheader("Hi, I'm Ashutosh! Exploring the world through Data.")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Welcome to my Live Project Gallery. I have built 10+ analytical dashboards 
        to solve problems in Finance, Public Safety, Marketing, and Education.
        
        ### 🛠️ Core Skills Demonstrated:
        - **Data Visualization:** Plotly, Seaborn, Streamlit
        - **Analytics Logic:** Time-Series, Financial DAX, Anomaly Detection
        - **Industry Insights:** Real-world problem solving across 10 sectors.
        """)
        st.success("👈 Select any project from the sidebar to see the Full Analysis!")
    with col2:
        skills = {'Skill': ['Python', 'SQL', 'Viz', 'Logic', 'DAX'], 'Level': [90, 85, 95, 88, 82]}
        st.plotly_chart(px.line_polar(skills, r='Level', theta='Skill', line_close=True), use_container_width=True)

# --- 2. SUSTAINABILITY ---
elif project == "Sustainability Tracker":
    st.title("🌱 UP Sustainability & Climate Tracker")
    c1, c2 = st.columns(2)
    df = pd.DataFrame({"City": ["Lucknow", "Prayagraj", "Kanpur", "Varanasi"], "AQI": [180, 150, 210, 165]})
    c1.metric("Target AQI", "100", "-50 Needed")
    c2.metric("Most Polluted", "Kanpur", "Industrial Area")
    st.plotly_chart(px.bar(df, x='City', y='AQI', color='AQI', color_continuous_scale='RdYlGn_r'), use_container_width=True)

# --- 3. PRODUCTIVITY ---
elif project == "Productivity Analyzer":
    st.title("📊 Personal Productivity & Screen Time")
    df = pd.DataFrame({'Activity': ['Study', 'Social Media', 'Projects', 'Sleep'], 'Hrs': [6, 2, 4, 8]})
    st.plotly_chart(px.pie(df, values='Hrs', names='Activity', hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu), use_container_width=True)
    st.info("💡 Insight: 60% of active hours are spent on high-value tasks.")

# --- 4. TRAFFIC SAFETY ---
elif project == "Traffic Safety":
    st.title("🚨 Road Accident & Public Safety Analysis")
    c1, c2, c3 = st.columns(3)
    c1.metric("High-Risk Zone", "NH-19", "Alert")
    c2.metric("Avg Survival", "82%")
    c3.metric("Peak Time", "4pm-8pm")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.map(pd.DataFrame({'lat': [25.43, 26.84, 26.44], 'lon': [81.84, 80.94, 80.33]}))
    with col_r:
        df = pd.DataFrame({'Time': ['4am','8am','12pm','4pm','8pm'], 'Accidents': [10, 45, 30, 80, 60]})
        st.plotly_chart(px.line(df, x='Time', y='Accidents', markers=True), use_container_width=True)

# --- 5. JOB MARKET ---
elif project == "Job Market Trends":
    st.title("💼 Job Market Demand & Salary Analyzer")
    df = pd.DataFrame({'Skill': ['SQL', 'Python', 'Power BI', 'Excel'], 'Demand': [95, 88, 75, 92], 'Salary': [8, 10, 7.5, 5]})
    st.plotly_chart(px.scatter(df, x='Skill', y='Salary', size='Demand', color='Skill'), use_container_width=True)
    st.table(df[['Skill', 'Salary']])

# --- 6. MOVIE SUCCESS ---
elif project == "Movie Success":
    st.title("🎬 Box Office Success Predictor")
    df = pd.DataFrame({'Movie': ['Avatar', 'Joker', 'Inception', 'Pathaan'], 'ROI': [12, 20, 8, 4], 'Rating': [7.9, 8.4, 8.8, 6.5]})
    st.plotly_chart(px.scatter(df, x='Rating', y='ROI', size='ROI', color='Movie', text='Movie'), use_container_width=True)

# --- 7. FREELANCE TRACKER ---
elif project == "Freelance Tracker":
    st.title("💰 Freelance Income & Client Profitability")
    df = pd.DataFrame({'Client': ['A', 'B', 'C'], 'Income': [45000, 62000, 35000], 'Delay': [5, 0, 12]})
    st.metric("Total Revenue", "₹1,42,000")
    st.plotly_chart(px.funnel(df, x='Income', y='Client', color='Client'), use_container_width=True)

# --- 8. SOCIAL MEDIA ---
elif project == "Social Media Trends":
    st.title("📱 Social Engagement & Growth Tracker")
    df = pd.DataFrame({'Day': ['Mon', 'Wed', 'Fri', 'Sun'], 'Growth': [100, 250, 400, 600]})
    st.plotly_chart(px.area(df, x='Day', y='Growth', color_discrete_sequence=['#E1306C']), use_container_width=True)

# --- 9. FOOD DELIVERY ---
elif project == "Food Delivery":
    st.title("🍕 Delivery Performance & Efficiency")
    df = pd.DataFrame({'Rest': ['Doms', 'BK', 'Haldm'], 'Time': [25, 45, 30], 'Dist': [3, 7, 4]})
    st.plotly_chart(px.bar(df, x='Rest', y='Time', color='Dist', title="Time vs Distance Intensity"), use_container_width=True)

# --- 10. REVIEW AUDITOR ---
elif project == "Review Auditor":
    st.title("🔍 Fake vs Real Review Analyzer")
    st.error("Anomaly Detected: 40% Reviews match 'Bot Pattern'")
    df = pd.DataFrame({'Type': ['Real', 'Fake'], 'Value': [60, 40]})
    st.plotly_chart(px.pie(df, values='Value', names='Type', color_discrete_sequence=['#2ecc71', '#e74c3c']), use_container_width=True)

# --- 11. EDTECH ANALYTICS ---
elif project == "EdTech Analytics":
    st.title("🎓 Online Learning Behavior")
    df = pd.DataFrame({'Stage': ['Enrolled', 'Started', 'Halfway', 'Finished'], 'Users': [1000, 850, 400, 120]})
    st.plotly_chart(px.funnel(df, x='Users', y='Stage'), use_container_width=True)
    st.warning("Insight: 50% drop-off occurs at 'Halfway Mark'. Content needs optimization.")

st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ by Ashu")
