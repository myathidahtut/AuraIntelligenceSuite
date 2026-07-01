import os
import re
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Standard structural normalization mappings for payment methods
PAYMENT_MAPPING = {
    'CD': 'Cash Down',
    'CC': 'Credit Card',
    'CQ': 'Cheque',
    'MO': 'Money Order',
    'PP': 'PayPal',
    'BT': 'Bank Transfer'
}

def auto_map_columns(df):
    """
    Intelligently maps generic file columns from other customers 
    to standard internal dashboard metrics.
    """
    columns = {col.lower().replace('_', ' '): col for col in df.columns}
    mapping = {}
    
    # 1. Target Revenue Column
    for k, v in columns.items():
        if any(x in k for x in ['total amount', 'revenue', 'amount', 'total sale', 'turnover']):
            mapping['Total_Amount'] = v
            break
            
    # 2. Target Date/Time Column
    for k, v in columns.items():
        if any(x in k for x in ['date', 'time', 'timestamp', 'purchased']):
            mapping['Purchase_Date'] = v
            break

    # 3. Target Payment Method Column
    for k, v in columns.items():
        if any(x in k for x in ['payment', 'method', 'pay type']):
            mapping['Payment_Method'] = v
            break

    # 4. Target Category Column
    for k, v in columns.items():
        if any(x in k for x in ['category name', 'category', 'item group', 'department']):
            mapping['Category_Name'] = v
            break

    # 5. Target Customer Names
    for k, v in columns.items():
        if any(x in k for x in ['first name', 'customer name', 'client', 'buyer']):
            mapping['First_Name'] = v
            break
    for k, v in columns.items():
        if any(x in k for x in ['last_name', 'surname']):
            mapping['Last_Name'] = v
            break

    return mapping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    if 'files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400
        
    uploaded_files = request.files.getlist('files')
    combined_dfs = []
    
    for file in uploaded_files:
        if file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(file)
                if df.empty:
                    continue
                
                # Dynamic mapping layer for external customer files
                detected_map = auto_map_columns(df)
                
                # Standardize data framing based on detected column aliases
                standardized_df = pd.DataFrame()
                
                standardized_df['Total_Amount'] = pd.to_numeric(df[detected_map['Total_Amount']], errors='coerce') if 'Total_Amount' in detected_map else 0
                standardized_df['Purchase_Date'] = pd.to_datetime(df[detected_map['Purchase_Date']], errors='coerce') if 'Purchase_Date' in detected_map else pd.Timestamp.now()
                standardized_df['Payment_Method'] = df[detected_map['Payment_Method']].astype(str).str.strip() if 'Payment_Method' in detected_map else 'Unknown'
                standardized_df['Category_Name'] = df[detected_map['Category_Name']].astype(str).str.strip() if 'Category_Name' in detected_map else 'General'
                
                # Reconstruct full names safely
                f_name = df[detected_map['First_Name']].astype(str).str.strip() if 'First_Name' in detected_map else 'Customer'
                l_name = df[detected_map['Last_Name']].astype(str).str.strip() if 'Last_Name' in detected_map else ''
                standardized_df['Customer_Name'] = (f_name + ' ' + l_name).str.strip()
                
                combined_dfs.append(standardized_df)
            except Exception as e:
                return jsonify({'error': f'Processing error on file {file.filename}: {str(e)}'}), 500

    if not combined_dfs:
        return jsonify({'error': 'No valid records could be processed'}), 400
        
    main_df = pd.concat(combined_dfs, ignore_index=True)
    main_df = main_df.dropna(subset=['Total_Amount'])
    
    # Apply baseline dictionary cleanings
    main_df['Payment_Method'] = main_df['Payment_Method'].replace(PAYMENT_MAPPING)
    
    # Derive structural analysis attributes
    main_df['Hour'] = main_df['Purchase_Date'].dt.hour
    main_df['Month_Name'] = main_df['Purchase_Date'].dt.strftime('%B')
    
    # Generate unified lists of available periods for the interface tabs
    available_months = ['All Months'] + sorted(main_df['Month_Name'].dropna().unique().tolist(), key=lambda m: pd.to_datetime(m, format='%B').month)
    
    # Structural breakdown logic packed into an optimized dictionary
    payload = {}
    
    for current_month in available_months:
        if current_month == 'All Months':
            m_df = main_df
        else:
            m_df = main_df[main_df['Month_Name'] == current_month]
            
        # Summary Counters
        total_rev = float(m_df['Total_Amount'].sum())
        total_tx = int(len(m_df))
        
        # Hourly peak calculation
        hourly_series = m_df.groupby('Hour').size().reindex(range(24), fill_value=0)
        hourly_data = hourly_series.tolist()
        
        # Payments breakdown
        pay_series = m_df.groupby('Payment_Method').size().sort_values(ascending=False)
        pay_data = {'labels': pay_series.index.tolist(), 'values': pay_series.tolist()}
        
        # Category breakdown
        cat_series = m_df.groupby('Category_Name')['Total_Amount'].sum().sort_values(ascending=False)
        cat_data = {'labels': cat_series.index.tolist(), 'values': cat_series.round(2).tolist()}
        
        # High value spenders evaluation (cleanly filters out 'Random' customers safely)
        valid_customers_df = m_df[~m_df['Customer_Name'].str.lower().str.contains('random|customer|^[ \t]*$', regex=True, na=True)]
        top_spenders = valid_customers_df.groupby('Customer_Name')['Total_Amount'].sum().sort_values(ascending=False).head(10)
        customer_count = int(valid_customers_df['Customer_Name'].nunique())
        
        leaderboard = [{'name': name, 'value': round(val, 2)} for name, val in top_spenders.items()]
        
        payload[current_month] = {
            'kpis': {'revenue': total_rev, 'transactions': total_tx, 'unique_customers': customer_count},
            'hourly': hourly_data,
            'payments': pay_data,
            'categories': cat_data,
            'leaderboard': leaderboard
        }
        
    return jsonify({'months': available_months, 'data': payload})

if __name__ == '__main__':
    app.run(debug=True, port=5000)