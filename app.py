import streamlit as st
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="BGC Command Center | HR Operations",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.title("🏢 BGC Command Center")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation Menu",
    [
        "📊 Executive Dashboard (Ex 3 & 7)",
        "✉️ Smart Email Assistant (Ex 1)",
        "📚 BGC Knowledge Base (Ex 2 & 4)",
        "⚙️ Process & Automation Blueprint (Ex 5 & 6)"
    ]
)
st.sidebar.markdown("---")
st.sidebar.caption("AI Fridays Hackathon Prototype")

# -----------------------------------------------------------------------------
# VIEW 1: EXECUTIVE DASHBOARD
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# VIEW 1: EXECUTIVE DASHBOARD
# -----------------------------------------------------------------------------
if page == "📊 Executive Dashboard (Ex 3 & 7)":
    st.title("Weekly Functional Status Report")
    st.markdown("### Executive Overview - BGC & Onboarding Pipeline")
    
    try:
        # 1. Load the generated CSV file
        # Make sure 'bgc_pipeline_data.csv' is saved in the exact same folder as app.py
        df = pd.read_csv('bgc_pipeline_data.csv')
        
        # 2. Calculate dynamic metrics from the dataset
        total_candidates = len(df)
        offers_pending = len(df[df['Offer_Status'] == 'Pending Signature'])
        cleared_bgc = len(df[df['BGC_Status'] == 'Cleared'])
        avg_aging = round(df['Aging_Days'].mean(), 1)
        
        # 3. Display the KPIs
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Total Candidates in Pipeline", value=total_candidates)
        col2.metric(label="Offers Pending Acceptance", value=offers_pending)
        col3.metric(label="BGC Cleared (Total)", value=cleared_bgc)
        col4.metric(label="Avg. Onboarding Delay", value=f"{avg_aging} Days")
        
        st.markdown("---")
        
        # 4. Interactive Data Table
        col_title, col_filter = st.columns([3, 1])
        with col_title:
            st.markdown("### Aging Cases & Escalations")
        with col_filter:
            # Add an interactive filter to wow the evaluators
            sla_filter = st.selectbox("Filter by SLA Status:", ["All"] + list(df['SLA_Status'].unique()))
            
        # Apply the filter
        if sla_filter != "All":
            display_df = df[df['SLA_Status'] == sla_filter]
        else:
            display_df = df
            
        # Render the dataframe (hide the ugly index numbers for a cleaner look)
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # 5. Leadership Presentation Placeholder
        with st.expander("📈 View Leadership Presentation (Exercise 7)"):
            st.write("Embed your Gamma.app slide deck link here, or summarize your future-state business impacts in bullet points.")

    except FileNotFoundError:
        st.error("⚠️ **System Error:** Could not locate `bgc_pipeline_data.csv`. Please ensure the file is saved in the same directory as this Streamlit script.")
# -----------------------------------------------------------------------------
# VIEW 2: SMART EMAIL ASSISTANT
# -----------------------------------------------------------------------------
elif page == "✉️ Smart Email Assistant (Ex 1)":
    st.title("Smart Email Assistant")
    st.markdown("Generate policy-compliant HR responses to complex candidate queries.")
    
    st.markdown("### Incoming Associate Query")
    # Paste your synthetic incoming email here
    st.info("""
    **From:** anxious.candidate@email.com
    **Subject:** URGENT: Delay in BGC Link and Joining Date Confusion
    
    *Hi HR Team, I received my offer letter but I haven't received the link to upload my BGC documents. My manager is asking if I can still join next Monday. Please help, I am very stressed!*
    """)
    
    st.markdown("### HR Response Generator")
    if st.button("✨ Generate AI Response"):
        st.success("Draft Generated Successfully")
        # Paste your AI-generated response here
        st.text_area(
            "Draft Response", 
            "Dear Candidate,\n\nThank you for reaching out. We understand your concern regarding the BGC link...\n\n[Insert your full Exercise 1 response here]", 
            height=250
        )

# -----------------------------------------------------------------------------
# VIEW 3: BGC KNOWLEDGE BASE
# -----------------------------------------------------------------------------
elif page == "📚 BGC Knowledge Base (Ex 2 & 4)":
    st.title("BGC Knowledge Base")
    
    tab1, tab2 = st.tabs(["Candidate Guidance Note (Ex 4)", "HR Internal Transcript (Ex 2)"])
    
    with tab1:
        st.markdown("### BGC Policy & Employee Guidance")
        st.write("Paste your synthesized policy explanation here.")
        
        st.markdown("#### Frequently Asked Questions")
        with st.expander("1. What documents are required for BGC?"):
            st.write("[Answer from your AI generation]")
        with st.expander("2. How long does the BGC process take?"):
            st.write("[Answer from your AI generation]")
            
    with tab2:
        st.markdown("### Transcript: HR Operations Alignment Meeting")
        st.write("Paste the chaotic meeting transcript you generated for Exercise 2 here to show the raw data.")
        st.text_area("Raw Meeting Transcript", "[HR Lead]: Okay team, we need to address the recent spike in BGC delays...", height=300, disabled=True)

# -----------------------------------------------------------------------------
# VIEW 4: PROCESS & AUTOMATION BLUEPRINT
# -----------------------------------------------------------------------------
elif page == "⚙️ Process & Automation Blueprint (Ex 5 & 6)":
    st.title("Process Engineering")
    
    st.markdown("### Current State SOP (Exercise 5)")
    st.write("Detailed step-by-step Standard Operating Procedure for the BGC Onboarding Pipeline.")
    
    # Use Markdown Mermaid for a clean flowchart
    st.markdown("""
    ```mermaid
    graph TD;
        A[Candidate Accepts Offer] --> B[HR Triggers BGC Link];
        B --> C{Candidate Uploads Docs?};
        C -- Yes --> D[Vendor Verification];
        C -- No --> E[Automated SLA Reminder];
        D --> F{Clearance Status};
        F -- Cleared --> G[Proceed to Onboarding];
        F -- Discrepancy --> H[HR Escalation Matrix];
    ```
    """)
    st.caption("Flowchart rendered using Mermaid.js")
    
    st.markdown("---")
    
    st.markdown("### Re-engineering & Automation Proposal (Exercise 6)")
    col_a, col_b = st.columns(2)
    with col_a:
        st.error("#### Identified Pain Points")
        st.markdown("""
        * Manual tracking of BGC status in Excel.
        * High volume of repetitive candidate queries.
        * Missed SLAs due to vendor dependencies.
        """)
    with col_b:
        st.success("#### Future-State Automation")
        st.markdown("""
        * **Quick Win:** Deploy Chatbot for basic BGC FAQs.
        * **Medium Term:** API integration with BGC Vendor for real-time status updates.
        * **Long Term:** Fully automated offer-to-onboarding portal.
        """)