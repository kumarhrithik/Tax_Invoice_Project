import PyPDF2
import pandas as pd

def extract_transactions(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        # Initialize variables to store extracted data
        transactions = []
        transaction = {}

        # Loop through each page of the PDF
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text = page.extractText()
            
            # Split the text by newline character to process each line
            lines = text.split('\n')
            
            # Iterate through each line to extract transaction details
            for line in lines:
                # Check if the line contains relevant information
                if 'App ID:' in line:
                    transaction['App ID'] = line.split('App ID:')[1].strip()
                elif 'Xref:' in line:
                    transaction['Xref'] = line.split('Xref:')[1].strip()
                elif 'Settlement Date:' in line:
                    transaction['Settlement Date'] = line.split('Settlement Date:')[1].strip()
                elif 'Broker:' in line:
                    transaction['Broker'] = line.split('Broker:')[1].strip()
                elif 'Sub Broker:' in line:
                    transaction['Sub Broker'] = line.split('Sub Broker:')[1].strip()
                elif 'Borrower Name:' in line:
                    transaction['Borrower Name'] = line.split('Borrower Name:')[1].strip()
                elif 'Description:' in line:
                    transaction['Description'] = line.split('Description:')[1].strip()
                elif 'Total Loan Amount:' in line:
                    transaction['Total Loan Amount'] = line.split('Total Loan Amount:')[1].strip()
                elif 'Commission Rate:' in line:
                    transaction['Commission Rate'] = line.split('Commission Rate:')[1].strip()
                elif 'Upfront:' in line:
                    transaction['Upfront'] = line.split('Upfront:')[1].strip()
                elif 'Upfront Incl GST:' in line:
                    transaction['Upfront Incl GST'] = line.split('Upfront Incl GST:')[1].strip()
                    
                    # Append the transaction details to the transactions list
                    transactions.append(transaction)
                    # Reset transaction dictionary for the next transaction
                    transaction = {}

    return transactions

def main():
    pdf_path = 'data/Test PDF.pdf'
    transactions = extract_transactions(pdf_path)
    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(transactions)
    
    print(df)

if __name__ == "__main__":
    main()
