from tax_invoice.transactions.models import Transaction

def remove_duplicates():
    transactions = Transaction.objects.all()
    unique_transactions = []
    seen = set()
    for transaction in transactions:
        key = (transaction.xref, transaction.total_loan_amount)
        if key not in seen:
            seen.add(key)
            unique_transactions.append(transaction)
    # Delete all transactions
    Transaction.objects.all().delete()
    # Save unique transactions
    for transaction in unique_transactions:
        transaction.save()

remove_duplicates()
