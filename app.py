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
if page == "📊 Executive Dashboard (Ex 3 & 7)":
    st.title("Weekly Functional Status Report")
    st.markdown("### Executive Overview - BGC & Onboarding Pipeline")
    
    # KPIs (Replace with your synthetic metrics)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Candidates in Pipeline", value="142", delta="12")
    col2.metric(label="Offers Pending Acceptance", value="28", delta="-3")
    col3.metric(label="BGC Cleared (This Week)", value="85", delta="15%")
    col4.metric(label="Avg. Onboarding Delay", value="4 Days", delta="-2 Days", delta_color="inverse")
    
    st.markdown("---")
    
    # Synthetic Data Table
    st.markdown("### Aging Cases & Escalations")
    st.info("💡 **Hackathon Tip:** Load your synthetic dataset (Exercise 3) here using `pd.read_csv('your_data.csv')`")
    
    # Dummy data for visualization purposes
    dummy_data = pd.DataFrame({
        "Candidate ID": ["C-101", "C-102", "C-103", "C-104"],
        "Name": ["John Doe", "Jane Smith", "Alice Jones", "Bob Brown"],
        "Status": ["Pending Vendor", "Offer Sent", "Cleared", "Pending Documents"],
        "SLA Status": ["Breached", "On Track", "Completed", "At Risk"],
        "Aging (Days)": [14, 2, 0, 8]
    })
    st.dataframe(dummy_data, use_container_width=True)
    
    st.markdown("---")
    
    # Leadership Presentation Placeholder
    with st.expander("📈 View Leadership Presentation (Exercise 7)"):
        st.write("Embed your Gamma.app slide deck link here, or summarize your future-state business impacts in bullet points.")

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