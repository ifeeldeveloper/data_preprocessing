import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration

st.set_page_config(
    page_title="Heart Disease Dashboard",
    page_icon="❤️",
    layout="wide"
)

# Load Dataset

heart_df = pd.read_excel("data/heart_disease_cleaned.xlsx")

# Title

st.title("❤️ Heart Disease Dashboard")
st.write("Interactive dashboard for exploring the Heart Disease dataset.")

# Sidebar Filters

st.sidebar.header("Filters")

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(heart_df["Gender"].unique().tolist())
)

age_group = st.sidebar.selectbox(
    "Age Group",
    ["All"] + sorted(heart_df["AgeGroup"].astype(str).unique().tolist())
)

smoker = st.sidebar.selectbox(
    "Current Smoker",
    ["All", 0, 1]
)

diabetes = st.sidebar.selectbox(
    "Diabetes",
    ["All", 0, 1]
)

# Apply Filters

filtered_df = heart_df.copy()

if gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == gender]

if age_group != "All":
    filtered_df = filtered_df[filtered_df["AgeGroup"].astype(str) == age_group]

if smoker != "All":
    filtered_df = filtered_df[filtered_df["currentSmoker"] == smoker]

if diabetes != "All":
    filtered_df = filtered_df[filtered_df["Diabetes"] == diabetes]

# KPI Metrics

st.subheader("Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Participants", len(filtered_df))
col2.metric("Average Age", round(filtered_df["Age"].mean(), 1))
col3.metric("Average BMI", round(filtered_df["BMI"].mean(), 1))
col4.metric("Average Cholesterol", round(filtered_df["totChol"].mean(), 1))

# Charts

left, right = st.columns(2)

# Gender Distribution

with left:

    st.subheader("Gender Distribution")

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.countplot(
        data=filtered_df,
        x="Gender",
        ax=ax
    )

    plt.tight_layout()

    st.pyplot(fig)

# Age Group Distribution

with right:

    st.subheader("Age Group Distribution")

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.countplot(
        data=filtered_df,
        x="AgeGroup",
        order=sorted(filtered_df["AgeGroup"].astype(str).unique()),
        ax=ax
    )

    plt.xticks(rotation=30)

    plt.tight_layout()

    st.pyplot(fig)

left, right = st.columns(2)

# BMI Histogram

with left:

    st.subheader("BMI Distribution")

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.histplot(
        filtered_df["BMI"],
        bins=15,
        kde=True,
        ax=ax
    )

    plt.tight_layout()

    st.pyplot(fig)

# Cholesterol Histogram

with right:

    st.subheader("Cholesterol Distribution")

    fig, ax = plt.subplots(figsize=(5, 4))

    sns.histplot(
        filtered_df["totChol"],
        bins=15,
        kde=True,
        ax=ax
    )

    plt.tight_layout()

    st.pyplot(fig)

# Heart Disease Distribution

st.subheader("Heart Disease Distribution")

heart_counts = filtered_df["heartStroke"].value_counts()

fig, ax = plt.subplots(figsize=(5, 5))

ax.pie(
    heart_counts,
    labels=["No", "Yes"],
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Heart Disease")

st.pyplot(fig)

# Dataset

st.subheader("Filtered Dataset")

st.dataframe(filtered_df)
