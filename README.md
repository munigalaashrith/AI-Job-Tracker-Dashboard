# AI Job Tracker Dashboard 💼

An AI-powered job tracking and analytics project built using Python, Streamlit, n8n, and Google Sheets.

## 📌 Project Overview

The AI Job Tracker helps organize job opportunities and monitor application progress through workflow automation and an interactive analytics dashboard.

The dashboard retrieves job analytics from an n8n webhook connected to Google Sheets and presents the information through metric cards and interactive charts.

## ✨ Features

- Automated job tracking using n8n.
- Google Sheets integration for storing job records.
- Analytics API using n8n Webhooks.
- Interactive Streamlit dashboard.
- Total job records and unique company metrics.
- Interview and application tracking.
- Jobs by Category chart.
- Jobs by Status chart.
- Company-wise Job Analytics chart.
- Professional light theme.

## 🛠️ Technologies Used

- Python 3.11
- Streamlit
- Pandas
- Plotly
- Requests
- n8n
- Google Sheets
- Git and GitHub

## 📂 Project Structure

```text
AI-Job-Tracker-Dashboard/
│
├── app.py
├── requirements.txt
├── .gitignore
│
└── .streamlit/
    └── config.toml
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Job-Tracker-Dashboard
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the n8n Analytics API

Make sure your n8n Analytics API workflow is active and connected to your Google Sheets data.

### 4. Configure the API URL

Open `app.py` and update `API_URL` to match your n8n webhook URL.

### 5. Run the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal.

## 📊 Dashboard Analytics

The dashboard displays:

- Total job records
- Unique companies
- Interview records
- Application-related records
- Confirmed or scheduled interviews
- Drafts needed

It also provides category-wise, status-wise, and company-wise charts.

## 🔐 Security

Never upload API keys, passwords, OAuth tokens, Google credentials, or private environment files to GitHub.

## 👨‍💻 Author

Developed as a practical project to explore workflow automation, API integration, Python development, and data visualization.