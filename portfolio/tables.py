import django_tables2 as tables
from django_tables2 import A

from portfolio import models


class ActivityTable(tables.Table):
    date_created = tables.columns.DateTimeColumn(short=False, verbose_name="Date")
    price_paid = tables.Column(verbose_name="Price $")
    type = tables.LinkColumn("portfolio:detail", args=[A("type_id")])
    Delete = tables.LinkColumn("portfolio:delete",
                               args=[A("pk")],
                               text="Delete",
                               verbose_name="",
                               attrs={
                                   "a": {"style": "color: red;"}
                               })

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        model = models.Portfolio
        fields = ("type", "amount", "price_paid", "status",)

        row_attrs = {
            "class": lambda record: "table-success" if record.status == "Buy" else "table-danger"
        }


class DetailTable(tables.Table):
    price_paid = tables.Column(verbose_name="Price $")
    date_created = tables.DateTimeColumn(short=False, verbose_name="Date")

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        model = models.Portfolio
        fields = ("status", "amount", "price_paid", "date_created")
