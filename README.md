# **Personal Finance Dashboard with AI Budgeting**
### **🚀 Overview**
The Personal Finance Dashboard with AI Budgeting is a Streamlit-based app designed to help you track your expenses, analyze spending patterns, and improve financial health using AI. The app reads budget and transaction data, trains an AI model to automatically categorize transactions, and provides insights on how your spending compares to your budget.

## **🌟 Features**
### ✅ Load Budget and Transaction Data
- Load budget and personal transaction data from CSV files.
- Display raw data for easy verification.
### ✅ AI-Based Transaction Categorization
- Trains a Naive Bayes classifier to categorize transactions based on their descriptions.
- Predicts categories for new transactions entered by the user.
### ✅ Spending vs Budget Analysis
- Compares spending across different categories against your budget.
- Provides a detailed summary of overspending and budget gaps.
### ✅ Interactive Visualizations
- Generates interactive bar charts using Plotly to visualize spending vs budget.
- Highlights categories where spending exceeds the budget.
### ✅ Recommendations
- Provides actionable recommendations based on spending patterns.
---
## **🏗️ How It Works**
1. Load Data:
- The app loads budget data and personal transaction data from CSV files.
2. Preprocess Data:
- Filters out non-debit transactions to focus on actual spending.
3. Train Model:
- Trains a Naive Bayes model using TF-IDF vectorization to predict transaction categories.
4. Categorize Transactions:
- Predicts categories for new user-entered transactions.
5. Analyze Spending vs Budget:
- Merges transaction data with budget data.
- Calculates differences between actual spending and budgeted amounts.
6. Visualize Data:
- Generates bar charts to display spending vs budget.
7. Recommendations:
- Suggests areas where spending can be reduced.
---
## **📂 File Structure**
``` bash
├── app.py                # Main Streamlit app  
├── Budget.csv            # Sample budget data  
├── personal_transactions.csv # Sample transaction data  
└── README.md             # Project documentation
```
## **🔧 Setup Instructions**
1. Clone the Repository:
``` bash
git clone https://github.com/username/finance-dashboard.git
cd finance-dashboard
```
2. Install Dependencies:
``` bash
pip install -r requirements.txt
```
3. Run the App:
``` bash
streamlit run app.py
```
## **📊 Sample Data Format**

### **Budget.csv**  
| Category      | Budget |  
|--------------|--------|  
| Groceries     | 500    |  
| Dining Out    | 200    |  
| Utilities     | 150    |  
| Entertainment | 100    |  

### **personal_transactions.csv**  
| Date         | Description        | Amount | Transaction Type | Category   |  
|--------------|---------------------|--------|------------------|------------|  
| 01/02/2025  | Grocery Store       | 100    | debit            | Groceries   |  
| 02/02/2025  | Electricity Bill    | 150    | debit            | Utilities   |  
## **📈 Technologies Used**
- **Python** – Core programming language
- **Streamlit** – Frontend framework for building the dashboard
- **Pandas** – Data manipulation and analysis
- **Plotly** – Data visualization
- **Scikit-learn** – Machine learning library for AI-based categorization
## **✅ Future Improvements**
- ✅ Add user authentication
- ✅ Include more detailed visualizations
- ✅ Add the ability to export categorized data
---
## **💡 Why Use This Dashboard?**
- 🔹 Easy to use and customizable
- 🔹 AI-powered transaction classification
- 🔹 Provides actionable insights and recommendations
- 🔹 Interactive and visually appealing dashboard
---
## **👨‍💻 Contributors**
Amna Shahzad – Developer and Data Scientist
## **📄 License**
This project is licensed under the MIT License.
