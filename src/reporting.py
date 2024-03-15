from tax_invoice.transactions.models import Transaction
from django.db.models import Count, Sum, Max
from datetime import date

def generate_data_extraction_report():
    transactions = Transaction.objects.all()[:10]  # Example: Retrieve first 10 transactions
    print("Data Extraction Report:")
    for transaction in transactions:
        print(transaction)

def generate_data_storage_report():
    total_transactions = Transaction.objects.count()
    print("Data Storage Report:")
    print("Total transactions stored:", total_transactions)

def generate_deduplication_report():
    total_unique_transactions = Transaction.objects.count()
    print("Deduplication Report:")
    print("Total unique transactions after deduplication:", total_unique_transactions)

def generate_sql_operations_report():
    # SQL Operation 1: Calculate the total loan amount during a specific time period
    start_date = '2024-01-01'
    end_date = date.today()
    total_loan_amount = calculate_total_loan_amount(start_date, end_date)
    print("Total loan amount during the specific time period:", total_loan_amount)

    # SQL Operation 2: Calculate the highest loan amount given by a broker
    broker = 'Example Broker'
    highest_loan_amount = calculate_highest_loan_amount_by_broker(broker)
    print("Highest loan amount given by the broker:", highest_loan_amount)

def generate_reporting_report():
    # Reporting 1: Generate a report for the broker, sorting loan amounts in descending order
    # covering daily, weekly, and monthly periods
    generate_broker_report()

    # Reporting 2: Generate a report of the total loan amount grouped by date
    generate_loan_amount_by_date_report()

    # Reporting 3: Define tier level of each transaction
    define_tier_level()

    # Reporting 4: Generate a report of the number of loans under each tier group by date
    generate_loans_by_tier_and_date_report()

def calculate_total_loan_amount(start_date, end_date):
    total_loan_amount = Transaction.objects.filter(settlement_date__range=(start_date, end_date)).aggregate(Sum('total_loan_amount'))['total_loan_amount__sum']
    return total_loan_amount

def calculate_highest_loan_amount_by_broker(broker):
    highest_loan_amount = Transaction.objects.filter(broker=broker).aggregate(Max('total_loan_amount'))['total_loan_amount__max']
    return highest_loan_amount

def generate_broker_report():
    brokers = Transaction.objects.values('broker').annotate(total_loan_amount=Sum('total_loan_amount')).order_by('-total_loan_amount')
    for broker in brokers:
        print(f"Broker: {broker['broker']}, Total Loan Amount: {broker['total_loan_amount']}")

def generate_loan_amount_by_date_report():
    loan_amount_by_date = Transaction.objects.values('settlement_date').annotate(total_loan_amount=Sum('total_loan_amount'))
    for item in loan_amount_by_date:
        print(f"Date: {item['settlement_date']}, Total Loan Amount: {item['total_loan_amount']}")

def define_tier_level():
    tiers = {
        'Tier 1': 100000,
        'Tier 2': 50000,
        'Tier 3': 10000
    }
    for tier, threshold in tiers.items():
        transactions = Transaction.objects.filter(total_loan_amount__gt=threshold)
        for transaction in transactions:
            print(f"Transaction ID: {transaction.id}, Tier Level: {tier}")

def generate_loans_by_tier_and_date_report():
    tiers = {
        'Tier 1': 100000,
        'Tier 2': 50000,
        'Tier 3': 10000
    }
    for tier, threshold in tiers.items():
        loans_by_tier = Transaction.objects.filter(total_loan_amount__gt=threshold).values('settlement_date').annotate(total_loans=Count('id'))
        for item in loans_by_tier:
            print(f"Tier: {tier}, Date: {item['settlement_date']}, Total Loans: {item['total_loans']}")


if __name__ == "__main__":
    generate_data_extraction_report()
    generate_data_storage_report()
    generate_deduplication_report()
    generate_sql_operations_report()
    generate_reporting_report()
