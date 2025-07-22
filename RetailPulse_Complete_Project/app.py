from flask import Flask, render_template
import pymysql
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)

def db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='jeeva',
        database='RetailPulseDB'
    )

@app.route('/')
def dashboard():
    conn = db_connection()
    cursor = conn.cursor()

    # 1. Churn-risk customers
    cursor.execute("""
        SELECT COUNT(DISTINCT CustomerID) 
        FROM transactions 
        WHERE TransactionDate < (CURRENT_DATE - INTERVAL 90 DAY);
    """)
    churn_count = cursor.fetchone()[0]

    # 2. Top 10 Customers by Spend
    cursor.execute("""
        SELECT CustomerID, SUM(Price * Quantity) AS TotalSpent 
        FROM transactions 
        GROUP BY CustomerID 
        ORDER BY TotalSpent DESC 
        LIMIT 10;
    """)
    df_top_customers = pd.DataFrame(cursor.fetchall(), columns=["CustomerID", "TotalSpent"])
    fig_top_customers = px.bar(df_top_customers, x="CustomerID", y="TotalSpent", title="Top 10 Customers by Spend")
    chart1 = json.dumps(fig_top_customers, cls=plotly.utils.PlotlyJSONEncoder)

    # 3. Top Product Categories
    cursor.execute("""
        SELECT ProductCategory, SUM(Quantity) AS TotalSold 
        FROM transactions 
        GROUP BY ProductCategory 
        ORDER BY TotalSold DESC 
        LIMIT 10;
    """)
    df_top_categories = pd.DataFrame(cursor.fetchall(), columns=["ProductCategory", "TotalSold"])
    fig_top_categories = px.bar(df_top_categories, x="ProductCategory", y="TotalSold", title="Top Product Categories")
    chart2 = json.dumps(fig_top_categories, cls=plotly.utils.PlotlyJSONEncoder)

    # 4. Sales by Gender
    cursor.execute("""
        SELECT Gender, SUM(Price * Quantity) AS TotalSales 
        FROM transactions 
        GROUP BY Gender;
    """)
    df_gender_sales = pd.DataFrame(cursor.fetchall(), columns=["Gender", "TotalSales"])
    fig_gender_sales = px.pie(df_gender_sales, names="Gender", values="TotalSales", title="Sales by Gender")
    chart3 = json.dumps(fig_gender_sales, cls=plotly.utils.PlotlyJSONEncoder)

    # 5. Monthly Sales Trend
    cursor.execute("""
        SELECT DATE_FORMAT(TransactionDate, '%Y-%m') AS Month, 
               SUM(Price * Quantity) AS MonthlySales
        FROM transactions
        GROUP BY Month
        ORDER BY Month;
    """)
    df_monthly = pd.DataFrame(cursor.fetchall(), columns=["Month", "MonthlySales"])
    fig_monthly_sales = px.area(
        df_monthly,
        x="Month",
        y="MonthlySales",
        title="Sales Over Time (Monthly)",
        markers=True
    )
    fig_monthly_sales.update_traces(line_color="#636EFA", fill='tozeroy')
    fig_monthly_sales.update_layout(template="plotly_white")
    chart5 = json.dumps(fig_monthly_sales, cls=plotly.utils.PlotlyJSONEncoder)

    conn.close()

    return render_template(
        "dashboard.html", 
        churn_count=churn_count,
        chart1=chart1,
        chart2=chart2,
        chart3=chart3,
        chart5=chart5
    )

@app.route('/download_csv')
def download_csv():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    data = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    conn.close()

    return data.to_csv(index=False), 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename=retailpulse_transactions.csv'
    }

if __name__ == "__main__":
    app.run(debug=True)