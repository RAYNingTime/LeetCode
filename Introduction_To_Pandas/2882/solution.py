import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    emails = []
    for index, row in customers.iterrows():
        if row.email in emails:
            customers = customers.drop(index)
        else: 
            emails.append(row.email)
    return customers
    
