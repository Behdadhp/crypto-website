import django_tables2 as tables
from django_tables2 import A

from portfolio import models


class ActivityTable(tables.Table):
    date_created = tables.columns.DateTimeColumn(short=False, verbose_name="Date")
    price_paid = tables.Column(verbose_name="Price $")
    type = tables.LinkColumn("portfolio:detail", args=[A("pk")])
    Delete = tables.LinkColumn("portfolio:delete",
                               args=[A("pk")],
                               text="Delete",
                               verbose_name="",
                               attrs={
                                   "a": {"style": "color: red;"}
                               })
    # status = tables.Column(attrs={
    #     "class": lambda record: "bgcolor: Violet" if record.status == "Buy" else "text-danger"
    # })

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        model = models.Portfolio
        fields = ("type", "amount", "price_paid", "status",)

        row_attrs = {
            "class": lambda record: "table-success" if record.status == "Buy" else "table-danger"
        }
