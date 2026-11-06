
import streamlit as st
import requests

st.set_page_config(
    page_title="AI Job Tracker",
    page_icon="💼",
    layout="wide"
)

API_URL = "http://localhost:5678/webhook/job-analytics"

st.title("💼 AI Job Tracker Dashboard")
st.write("Live analytics from your Google Sheets through n8n.")

if st.button("Refresh Analytics"):
    st.rerun()

try:
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()

    data = response.json()

    st.success("Connected to n8n successfully!")

   
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "💼 Total Job Records",
        data["total_records"],
        border=True
    )

    col2.metric(
        "🏢 Unique Companies",
        data["unique_companies"],
        border=True
    )

    col3.metric(
        "🎯 Interview Records",
        data["interview_records"],
        border=True
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "📨 Applications",
        data["application_related_records"],
        border=True
    )

    col5.metric(
        "🤝 Confirmed / Scheduled",
        data["confirmed_or_scheduled_interviews"],
        border=True
    )

    col6.metric(
        "📝 Drafts Needed",
        data["draft_needed"],
        border=True
    )


    st.markdown("---")
    st.subheader("📊 Job Analytics")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("#### Jobs by Category")

        category_data = data.get("category_counts", {})

        st.bar_chart(category_data)

    with chart_col2:
        st.markdown("#### Jobs by Status")

        status_data = data.get("status_counts", {})
        st.markdown("---")
            
    st.subheader("🏢 Company-wise Job Analytics")

    company_data = {
        company: data["companies"].count(company)
        for company in set(data["companies"])
    }

    st.bar_chart(company_data)
    st.bar_chart(status_data)

except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to n8n: {e}")

except (ValueError, KeyError) as e:
    st.error(f"Unexpected API response: {e}")

