import django_tables2 as tables


class IndexMarketTable(tables.Table):
    market_cap_rank = tables.Column(verbose_name="Rank")
    name = tables.Column()
    current_price = tables.Column(verbose_name="Price $")

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        fields = ("market_cap_rank",)
