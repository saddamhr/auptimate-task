# import pandas
import pandas as pd

# Sample dataset as a list of dictionaries
transaction_records = [
    {"InvestorID": 1, "SyndicateID": 101, "Amount": 1000, "Date": "2021-01-01"},
    {"InvestorID": 2, "SyndicateID": 102, "Amount": 1500, "Date": "2021-01-02"},
    {"InvestorID": 2, "SyndicateID": 102, "Amount": 1500, "Date": "2021-01-02"},
    {"InvestorID": 2, "SyndicateID": 102, "Amount": 1500, "Date": "2021-01-02"},
    {"InvestorID": 1, "SyndicateID": 103, "Amount": 800, "Date": "2021-01-03"},
    {"InvestorID": 1, "SyndicateID": 101, "Amount": 1200, "Date": "2021-01-04"},
    {"InvestorID": 0, "SyndicateID": 101, "Amount": 1200, "Date": "2021-01-04"},
    {"InvestorID": 0, "SyndicateID": 101, "Amount": 2000, "Date": "2021-01-04"},
    {"InvestorID": 3, "SyndicateID": 101, "Amount": 1200, "Date": "2021-01-04"},
    {"InvestorID": 4, "SyndicateID": 101, "Amount": 2000, "Date": "2021-01-04"},
    # Add more data here
]

def get_top_investors(transaction_records):
    # Create a DataFrame from the dataset
    df = pd.DataFrame(transaction_records)

    try:
        # Group by InvestorID to count unique SyndicateIDs
        investor_syndicate_counts = df.groupby('InvestorID')['SyndicateID'].nunique()

        # Sort the investors by the number of unique syndicates in descending order
        investor_syndicate_counts = investor_syndicate_counts.sort_values(ascending=False)

        # Get the top 5 investors with the highest unique syndicate counts
        top_investors = investor_syndicate_counts.head(5)

        # Create a list of dictionaries to store the results
        results = []
        for investor_id, syndicate_count in top_investors.items():
            total_investment = df[df['InvestorID'] == investor_id]['Amount'].sum()
            results.append({
                'InvestorID': investor_id,
                'UniqueSyndicateCount': syndicate_count,
                'TotalInvestment': total_investment
            })

        return results

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    results = get_top_investors(transaction_records)
    
    if isinstance(results, list):
        # Print the top 5 investors with unique syndicate counts and total investment
        for result in results:
            print(result)
    else:
        print(results)
