# Customer Churn Analysis — Banking Dataset

**Tools:** MySQL · Python (pandas, matplotlib)  
**Dataset:** 10,000 banking customers (Kaggle)  
**Goal:** Identify key churn drivers and recommend retention strategies

## Project Structure
- `sql/churn_queries.sql` — 10 business questions answered in MySQL
- `notebooks/churn_eda.py` — Python EDA with pandas + matplotlib
- `churn_analysis.png` — 6 visualizations
- `data/` — raw dataset

## Key Findings
| Question | Finding |
|----------|---------|
| Overall churn rate | 20.4% |
| Highest churn geography | Germany 32.4% |
| Highest churn age group | 45-60 at 51.1% |
| Products vs churn | 3 products = 82.7%, 4 = 100% |
| Complaint impact | Complained = 99.5% churn |
| Balance difference | Churned avg $91,109 vs $72,742 |

## Top 5 Insights
1. Age 45-60 churns at 51.1% — 6x higher than under-30s
2. Customers with 3-4 products churn at 82-100% — cap cross-selling at 2
3. 99.5% of complainers churn — complaint resolution is highest ROI action
4. Germany churns at 2x France and Spain — needs regional investigation
5. Churned customers hold 25% higher balances — bank is losing best customers

## Recommendations
1. Launch Germany-specific retention campaign
2. Cap product cross-selling at 2 products per customer
3. Build complaint fast-track resolution process
4. Target 45-60 age segment with loyalty rewards
5. Proactively reach out to high-balance inactive members

## How to Run
```bash
pip install sqlalchemy pymysql pandas matplotlib
python setup_db.py
python notebooks/churn_eda.py
```
