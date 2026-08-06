# Municipal Budget Intelligence

Minimal starter project to visualize, explore , analyze, predict and calculate variances of big data budgets, and build a  Streamlit dashboard.

Phase 0 files included:

- app.py — simple Streamlit app that loads data.csv and shows basic metrics
- analysis.py — standalone script that computes variance and execution rate
- data.csv — sample fake municipal financial data
- requirements.txt — Python dependencies
- .gitignore — common ignores

steps

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

overview 

phase 0

- Cleansing and upload of budget data
- calculate basic metrics (budget variation, execution percentage, budget vs expenses)
- initial streamlit dashboard

1-2 months

phase 1
-Bring out new data sets
-develop interactive visualization
-Create reports and index for better data interpretation

phase 2
Amplify analitic capabilities to obtain better value and info from data

-Analysis of trends across different time periods or entities
-implementation of basic predictive analytics models
-Automatization of metrics  and indicators for financial analysis
