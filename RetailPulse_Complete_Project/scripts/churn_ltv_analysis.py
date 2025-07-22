import pandas as pd
from datetime import datetime
import os

# Load dataset
df = pd.read_csv(r"C:\Users\jeevarathinam\OneDrive\Documents\RetailPulse_Complete_Project\data\retail_data.csv")
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

# Calculate 'today' as 1 day after the most recent transaction
today = df['TransactionDate'].max() + pd.Timedelta(days=1)

# Group by CustomerID to compute Recency, Frequency, and Monetary value
customer_metrics = df.groupby('CustomerID').agg({
    'TransactionDate': [lambda x: (today - x.max()).days, 'count'],
    'Price': 'sum'
})

# Rename columns
customer_metrics.columns = ['Recency', 'Frequency', 'Monetary']

# Lifetime Value (LTV) calculation
avg_order_value = customer_metrics['Monetary'] / customer_metrics['Frequency']
purchase_freq = customer_metrics['Frequency'] / customer_metrics.shape[0]
customer_metrics['LTV'] = avg_order_value * purchase_freq * 12  # Assuming 12-month lifespan

# Churn Risk: Customers who haven't purchased in the last 90 days
customer_metrics['ChurnRisk'] = customer_metrics['Recency'] > 90

# Output directory path (relative to script location)
output_dir = r"C:\Users\jeevarathinam\OneDrive\Documents\RetailPulse_Complete_Project\data"
os.makedirs(output_dir, exist_ok=True)

# Save results
output_path = os.path.join(output_dir, "churn_ltv_metrics.csv")
customer_metrics.to_csv(output_path)

print(f"✅ Churn & LTV metrics saved to: {output_path}")
print(customer_metrics.head())
