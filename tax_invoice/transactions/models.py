from django.db import models

class Transaction(models.Model):
    app_id = models.CharField(max_length=255)
    xref = models.CharField(max_length=255)
    settlement_date = models.DateField()
    broker = models.CharField(max_length=255)
    sub_broker = models.CharField(max_length=255)
    borrower_name = models.CharField(max_length=255)
    description = models.TextField()
    total_loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2)
    upfront = models.DecimalField(max_digits=12, decimal_places=2)
    upfront_incl_gst = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Transaction {self.id}: {self.app_id}"