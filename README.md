# 📊 RetailPulse – Consumer Behavior Analytics Platform

**RetailPulse** is a Flask-based analytics dashboard that uncovers key insights from customer transaction data. It helps identify churn-risk customers, spot top buyers, visualize category performance, and track sales trends — all through a clean, interactive interface.

---

## 🚀 Features

- 🔍 **Churn-Risk Detection** – Highlights customers inactive for 90+ days  
- 💰 **Top Buyers** – Displays top spenders with transaction value  
- 🛍️ **Best Product Categories** – Shows high-performing categories  
- 👥 **Gender-Based Sales** – Compares purchases between genders  
- 📈 **Sales Over Time** – Line chart showing time-based sales trends  
- 🌗 **Dark Mode Toggle** – Eye-friendly UI for night use  
- 📥 **Download CSV** – Export raw transaction data

---

## 📁 Project Structure

```
RetailPulse/
├── app.py                 # Flask backend logic
├── transactions.csv       # Sample transactional dataset
├── templates/
│   └── dashboard.html     # Main HTML dashboard template
├── static/
│   └── style.css          # (Optional) external CSS
├── README.md              # This file
```

---

## 📊 Dashboard Overview

- ✅ **Churn KPI Tile** – Shows count of customers who haven’t purchased in over 90 days  
- 📈 **Top 10 Spending Customers** – Bar chart  
- 🛍️ **Best Product Categories** – Horizontal bar chart  
- 👩‍🦰👨‍🦱 **Gender-based Sales Distribution** – Pie chart  
- 📉 **Sales Over Time** – Line chart  
- 🌗 **Dark Mode Toggle** – Button on navbar  
- 📁 **Download CSV Button** – Easily export all data

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/retailpulse.git
cd retailpulse
```

### 2. Install Requirements

```bash
pip install flask pandas plotly pymysql
```

### 3. Prepare MySQL Database

- Create a MySQL database (e.g., `RetailPulseDB`)
- Create a `transactions` table using this schema:

```sql
CREATE TABLE transactions (
    CustomerID VARCHAR(20),
    ProductCategory VARCHAR(100),
    Price FLOAT,
    Quantity INT,
    TransactionDate DATE,
    Age INT,
    Gender VARCHAR(10),
    Location VARCHAR(100)
);
```

- Insert your data or use `transactions.csv` to import into MySQL

### 4. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧮 Tech Stack

| Layer          | Tools Used              |
|----------------|--------------------------|
| Backend        | Python, Flask            |
| Database       | MySQL                    |
| Data Handling  | Pandas                   |
| Charts         | Plotly.js                |
| Frontend       | HTML5, Jinja2, CSS       |
| UI Features    | Dark Mode, CSV Export    |

---

## 📸 Screenshots

### 💡 Light Mode  
![Light Mode Dashboard](screenshots/dashboard_light.png)

### 🌙 Dark Mode  
![Dark Mode Dashboard](screenshots/dashboard_dark.png)


---

## 👨‍💻 Author

**Jeevarathinam V**  
📧 jeevav62@gmail.com  
🔗 [LinkedIn](http://www.linkedin.com/in/jeevarathinam-v-)  
🔗 [GitHub](https://github.com/Jeevav62)


---

## ⭐️ Support

If you find this project useful, please consider giving it a ⭐ on GitHub and sharing it with your peers.
