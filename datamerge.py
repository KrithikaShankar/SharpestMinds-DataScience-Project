# defining function to aggregate data
import pandas as pd

def mergeData():
    # Loading Data
    telco_demo_df = pd.read_excel('Telco_customer_churn_demographics.xlsx')
    telco_loc_df = pd.read_excel('Telco_customer_churn_location.xlsx')
    telco_pop_df = pd.read_excel('Telco_customer_churn_population.xlsx')
    telco_serv_df = pd.read_excel('Telco_customer_churn_services.xlsx')
    telco_status_df = pd.read_excel('Telco_customer_churn_status.xlsx')
    df1 = pd.DataFrame()
    df1 = pd.merge(telco_loc_df, telco_demo_df.loc[:, telco_demo_df.columns != 'Count'],
                   how='inner', on=('Customer ID'))
    df1 = pd.merge(df1, telco_serv_df.loc[:, telco_serv_df.columns != 'Count'], how='inner', on=('Customer ID'))
    df1 = pd.merge(df1, telco_status_df.loc[:, telco_status_df.columns != 'Quarter'], how='inner', on=('Customer ID'))
    # Final Combined Dataset
    final_telco_df = pd.merge(df1, telco_pop_df, how='inner', on=('Zip Code'))
    # Renaming duplicate columns
    final_telco_df = final_telco_df.rename(columns={"Count_x": "Count"})
    final_telco_df = final_telco_df.drop("Count_y", axis=1)
    return final_telco_df
