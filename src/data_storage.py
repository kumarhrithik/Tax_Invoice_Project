from .data_extraction import extract_transactions
from tax_invoice.transactions.models import Transaction

def store_transactions_from_pdf(pdf_path):
    transactions = extract_transactions(pdf_path)  # Extract transactions from the PDF
    store_transactions(transactions)


def store_transactions(transactions):
    for transaction in transactions:
        Transaction.objects.create(
            app_id=transaction['AppID'],
            xref=transaction['Xref'],
            settlement_date=transaction['SettlementDate'],
            broker=transaction['Broker'],
            sub_broker=transaction['SubBroker'],
            borrower_name=transaction['BorrowerName'],
            description=transaction['Description'],
            total_loan_amount=transaction['TotalLoanAmount'],
            commission_rate=transaction['CommissionRate'],
            upfront=transaction['Upfront'],
            upfront_incl_gst=transaction['UpfrontInclGST']
        )

store_transactions_from_pdf('data\Test PDF.pdf')