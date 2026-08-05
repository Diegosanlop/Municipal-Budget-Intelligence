# Municipal Budget Intelligence

A minimal starter project to explore municipal budget data, calculate variances, and build a simple Streamlit dashboard.

Phase‑0 files included:

- app.py — simple Streamlit app that loads data.csv and shows basic metrics
- analysis.py — standalone script that computes variance and execution rate
- data.csv — sample fake municipal financial data
- requirements.txt — Python dependencies
- .gitignore — common ignores

Quick start

1. Clone the repo:

   git clone https://github.com/Diegosanlop/Municipal-Budget-Intelligence.git
   cd Municipal-Budget-Intelligence

2. Create a virtual environment and install dependencies:

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\Scripts\activate    # Windows
   pip install -r requirements.txt

3. Run the analysis script:

   python analysis.py

4. Run the dashboard (Streamlit):

   streamlit run app.py

Next steps

- Learn the minimal Python and Pandas operations (variables, lists, functions).
- Iterate on the dashboard: add charts, sorting, filters, and derived metrics.
- When ready, add CI and push further changes.
