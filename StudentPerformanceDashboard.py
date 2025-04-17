import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st

# Load dataset — change this path to your correct CSV file
df = pd.read_csv("stude.csv")


# Page config
st.set_page_config(layout="wide", page_title="Student Dashboard")

# Title
st.markdown(
    "<h1 style='color:#90caf9'>🎓 Student Performance Dashboard</h1>",
    unsafe_allow_html=True,
)

# First row: 3 columns for Pie Charts
col1, col2, col3 = st.columns(3)

with col1:
    gender_fig = px.pie(
        df,
        names="Gender",
        title="Gender Distribution",
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    st.plotly_chart(gender_fig, use_container_width=True)

with col2:
    caste_fig = px.pie(
        df,
        names="Caste",
        title="Caste Distribution",
        color_discrete_sequence=px.colors.sequential.Agsunset,
    )
    st.plotly_chart(caste_fig, use_container_width=True)

with col3:
    perf_fig = px.pie(
        df,
        names="Performance",
        hole=0.6,
        title="Overall Performance",
        color_discrete_sequence=px.colors.sequential.Plasma,
    )
    st.plotly_chart(perf_fig, use_container_width=True)

# Heading
st.markdown("### 📊 Coaching & Performance Analysis")

# Bar chart: Coaching vs Performance
coaching_perf = pd.crosstab(df["coaching"], df["Performance"])
bar_fig = px.bar(
    coaching_perf,
    barmode="group",
    title="Coaching vs Performance",
    color_discrete_sequence=px.colors.sequential.Viridis,
)
st.plotly_chart(bar_fig, use_container_width=True)

# Second row: 2 columns for Line chart and Heatmap
col4, col5 = st.columns(2)

with col4:
    st.markdown("### 📈 Time Spent vs Performance")
    time_perf = pd.crosstab(df["time"], df["Performance"])
    line_fig = px.line(
        time_perf,
        title="Study Time vs Performance",
        markers=True,
        color_discrete_sequence=px.colors.sequential.Bluered,
    )
    st.plotly_chart(line_fig, use_container_width=True)

with col5:
    st.markdown("### 🔥 XII Grade vs Class_X_Percentage Heatmap")
    heatmap_xii = pd.crosstab(df["Class_XII_Percentage"], df["Class_X_Percentage"])
    heat_fig = px.imshow(
        heatmap_xii,
        text_auto=True,
        title="Class XII vs Class X Percentage Heatmap",
        color_continuous_scale="Magma",
    )
    st.plotly_chart(heat_fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    "<center style='color:gray;'>Designed with ❤️ using Streamlit, By Vivek & Shruti P</center>",
    unsafe_allow_html=True,
)
