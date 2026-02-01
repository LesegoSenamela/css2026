import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Research Profile", layout="wide")

# Title of the app
st.title("Research Profile for Lesego Senamela")

# Collect basic information
name = "Lesego Senamela"
field = "CyberSecurity, AI and Machine Learning"
institution = "University of Pretoria"


# Display basic profile information
st.header("Researcher Overview",  divider="blue")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    
    # Research Intrests
    st.header("Research Intrests", divider="blue")
    st.write("""
             - Data Poisoning
             - Threat Detection
             - Digital Forensics
             - Honeypot Implementations
             """)
with col2:
    st.image(
    "Profile.png",
    width=400
)



# Research overview
st.header("Research Paper Abstract", divider="blue")
st.subheader("Problem we were trying to solve in data poisoning attacks")

st.write("""The increasing reliance on Machine Learning (ML) models across 
critical applications makes them a high-value target for adversarial attacks. 
Data poisoning, a particularly insidious threat, involves an adversary 
injecting maliciously crafted samples into a model’s training data to 
compromise its integrity during or after deployment. Traditional security 
measures often fail to detect such attacks as they occur.The end product of 
this is the design and implementation of a novel honeypot-based framework for 
the proactive detection of data poisoning attempts. Our system deploys decoy 
data points, strategically placed within the feature space, that are designed 
to be attractive to poisoning algorithms. Any interaction or manipulation of a 
dataset is flagged and analyzed as a potential attack by the honeypot. We 
developed a prototype that simulates a dataset collection environment and 
evaluated its efficacy against several common poisoning techniques, including 
label-flipping and backdoor insertion attacks. The results demonstrate that our
honeypot system can achieve a high detection rate witha low false-positive rate, 
providing an effective early-warning mechanism. This research confirms the 
viability of using deceptive security elements, traditionally used in network 
security, to safeguard the machine learning pipeline, offering a proactive 
layer of defense for ML-powered systems.""")

st.write("*Key components used in this are Clustering, Random Forest, XGBoost, KMeans, KModes*")

st.header("Publications relating to data poisoning", divider="blue")

uploaded_file = pd.read_csv("CitationPapers.csv")
uploaded_file = uploaded_file.sort_values(
    by="Cites",
    ascending=False
)
st.dataframe(uploaded_file)

# Add filtering for year or keyword
keyword = st.text_input("Filter by keyword (For effective search results try searching the year of publication.)", "")
if keyword:
        filtered = uploaded_file[
            uploaded_file.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends from 2015", divider="blue")
year_counts = uploaded_file["Year"].value_counts().sort_index()
st.bar_chart(year_counts)


# contact section
st.header("Contact Information", divider="blue")
email = "senamelalesego@gmail.com"
academic = "u22683837@tuks.co.za"
linkedin = "www.linkedin.com/in/lesegosenamela"
st.write(f""" 
         - Email (Personal): {email} 
         - Email (academic): {academic}
         - LinkedIn: {linkedin}""")
