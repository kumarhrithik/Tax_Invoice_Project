from tax_invoice.transactions.models import Transaction
from django.db.models import Sum, Max
from datetime import date

def calculate_total_loan_amount(start_date, end_date):
    """
    Calculate the total loan amount during a specific time period.

    Args:
        start_date (str): The start date of the time period in 'DD-MM-YYYY' format.
        end_date (str): The end date of the time period in 'DD-MM-YYYY' format.

    Returns:
        Decimal: The total loan amount during the specified time period.
    """
    total_loan_amount = Transaction.objects.filter(settlement_date__range=(start_date, end_date)).aggregate(Sum('total_loan_amount'))['total_loan_amount__sum']
    return total_loan_amount

def calculate_highest_loan_amount_by_broker(broker):
    """
    Calculate the highest loan amount given by a specific broker.

    Args:
        broker (str): The name of the broker.

    Returns:
        Decimal: The highest loan amount given by the specified broker.
    """
    highest_loan_amount = Transaction.objects.filter(broker=broker).aggregate(Max('total_loan_amount'))['total_loan_amount__max']
    return highest_loan_amount

start_date = '01-01-2024'
today_date = date.today()
end_date = today_date.strftime('%d-%m-%Y')
total_loan_amount = calculate_total_loan_amount(start_date, end_date)
print("Total loan amount during the specific time period:", total_loan_amount)

broker = 'Example Broker'
highest_loan_amount = calculate_highest_loan_amount_by_broker(broker)
print("Highest loan amount given by the broker:", highest_loan_amount)
