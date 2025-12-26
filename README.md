# Ipo-business-intelligence-dashboard
End-to-end Business Intelligence solution analyzing IPO performance using Python and Power BI, with automated data pipelines, sector-wise insights, and SELL vs HOLD decision support.


Overview
This project is an end-to-end Business Intelligence solution that analyzes IPO performance using subscription and pricing data. It transforms raw IPO datasets into validated metrics and interactive dashboards to support data-driven SELL vs HOLD decisions.
The focus is on clarity, metric accuracy, and decision support, following real-world BI workflows.


Business Problem
IPO decisions are often driven by hype rather than evidence. Subscription numbers alone do not always indicate post-listing performance.
This project addresses questions such as:

Do highly subscribed IPOs deliver better returns?
Which investor category (Retail, QIB, HNI) is a stronger signal?
Is it better to SELL on listing day or HOLD for 30 days?
How does IPO performance vary across sectors?



Key Metrics
Listing Gain % – Return on listing day relative to issue price
30-Day Return % – Return after 30 trading days
Subscription Ratios – Retail, QIB, and HNI participation
Decision Flag (SELL / HOLD)
HOLD if 30-Day Return % > Listing Gain %


Tech Stack
Python (Pandas, NumPy) – Data cleaning, validation, and metric computation
SQL (analytical design) – Aggregation and correlation logic
Power BI – Interactive dashboards and visual storytelling
CSV-based ingestion – Simple and reliable data sourcing



Dashboard Design
The Power BI dashboard is organized into three layers:
Executive Overview
High-level KPIs, sector-wise performance, and overall SELL vs HOLD distribution.

Sector & Subscription Analysis
Comparison of Retail, QIB, and HNI participation with sector-level performance trends.

IPO Decision Explorer
Company-level metrics with clear SELL / HOLD recommendations and interactive filters.



Key Insights
Institutional (QIB) participation shows a stronger relationship with IPO performance than retail demand.
Some IPOs perform well on listing day but underperform over a 30-day holding period.
Sector-level aggregation helps reduce noise from individual IPO volatility.
Simple, explainable decision logic improves investment clarity.


Future Enhancements
Automated ingestion of the latest 10–20 IPOs
Incremental update pipeline with duplicate handling
API-based live IPO data integration
Scheduled Power BI refresh
Extended holding-period analysis (60/90 days)



Author
Karanvir Singh Osahan
Computer Science Undergraduate | Aspiring Business Intelligence Engineer
GitHub: KaranOsahan | LinkedIn: KaranOsahan
SELL otherwise

All metrics are calculated programmatically to ensure consistency.
