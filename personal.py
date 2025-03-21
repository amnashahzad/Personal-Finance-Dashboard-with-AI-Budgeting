import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

def load_budget():
    budget = pd.read_csv(r'C:\Users\Naveed Computers\OneDrive\Desktop\strem lit\New folder\Budget.csv')
    return budget

def load_transactions():
    transactions = pd.read_csv(r'C:\Users\Naveed Computers\OneDrive\Desktop\strem lit\New folder\personal_transactions.csv')
    transactions['Date'] = pd.to_datetime(transactions['Date'], format='%m/%d/%Y')
    return transactions

# Preprocess transaction data
def preprocess_transactions(transactions):
    # Filter out non-debit transactions (e.g., credits like paychecks)
    transactions = transactions[transactions['Transaction Type'] == 'debit']
    return transactions

# Train a model to categorize transactions
def train_model(transactions):
    # Use 'Description' to predict 'Category'
    X = transactions['Description']
    y = transactions['Category']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create a pipeline with TF-IDF and Naive Bayes
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    st.write("Model Evaluation:")
    st.write(classification_report(y_test, y_pred))
    
    return model

# Categorize new transactions
def categorize_transactions(model, new_transactions):
    new_transactions['predicted_category'] = model.predict(new_transactions['Description'])
    return new_transactions

# Main Streamlit app
def main():
    st.title("Personal Finance Dashboard with AI Budgeting")
    
    # Load data
    budget = load_budget()
    transactions = load_transactions()
    transactions = preprocess_transactions(transactions)
    
    # Display raw data
    if st.checkbox("Show raw data"):
        st.subheader("Budget Data")
        st.write(budget)
        st.subheader("Transaction Data")
        st.write(transactions)
    
    # Train model
    if st.button("Train Model"):
        model = train_model(transactions)
        st.session_state['model'] = model
    
    # Categorize new transactions
    if 'model' in st.session_state:
        st.subheader("Categorize New Transactions")
        new_transactions = st.text_area("Enter new transactions (one per line):")
        if new_transactions:
            new_transactions = new_transactions.split('\n')
            new_transactions = pd.DataFrame({'Description': new_transactions})
            categorized_transactions = categorize_transactions(st.session_state['model'], new_transactions)
            st.write(categorized_transactions)
    
    # Analyze spending vs budget
    st.subheader("Spending vs Budget")
    
    # Merge transactions with budget
    spending_summary = transactions.groupby('Category')['Amount'].sum().reset_index()
    spending_summary = spending_summary.merge(budget, on='Category', how='left')
    spending_summary['Budget'] = spending_summary['Budget'].fillna(0)  # Fill missing budgets with 0
    spending_summary['Difference'] = spending_summary['Budget'] - spending_summary['Amount']
    
    # Display spending vs budget
    st.write(spending_summary)
    
    # Visualize spending vs budget
    fig = px.bar(spending_summary, x='Category', y=['Amount', 'Budget'], barmode='group', 
                 title="Spending vs Budget by Category")
    st.plotly_chart(fig)
    
    # Provide recommendations
    st.subheader("Budget Recommendations")
    overspent_categories = spending_summary[spending_summary['Difference'] < 0]
    if not overspent_categories.empty:
        st.write("You have overspent in the following categories:")
        st.write(overspent_categories[['Category', 'Amount', 'Budget', 'Difference']])
    else:
        st.write("You are within budget for all categories. Great job!")

if __name__ == "__main__":
    main()