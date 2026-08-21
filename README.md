<img width="1438" height="806" alt="Sales   Inventory Performance Dashboard" src="https://github.com/user-attachments/assets/1e236f83-0b75-45b1-a59b-8173db4257f3" />


# Sales & Inventory Performance Analytics Dashboard

An end-to-end data analytics project featuring custom Python data pipelines, MySQL database management, and interactive Power BI dashboard reporting.

## 🛠️ Project Architecture & Tech Stack
- **Database:** MySQL (Relational schemas for `sales`, `products`, and `customers`)
- **Data Ingestion:** Python (`mysql-connector`) for automated batch record insertion
- **Analytics & Visualization:** Power BI (Power Query transformation, DAX modeling, interactive visuals)

## 📊 Key Features
- **Stockout Risk Gauge:** Live capacity tracking comparing units sold against baseline inventory thresholds.
- **Dynamic Cross-Filtering:** Interactive date range slider and stock availability filter (Low Stock vs. Sufficient Stock) across all KPIs.
- **Low Stock Tracking:** Automated alerting and count tracking for inventory items falling below safety stock limits.

## 📁 Repository Structure
- `schema.sql`: Database table structures and constraints
- `db_insert.py`: Python script for inserting transactional records
