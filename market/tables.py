import django_tables2 as tables


class MarketTable(tables.Table):
    market_cap_rank = tables.Column(verbose_name="Rank")
    name = tables.Column()
    symbol = tables.Column()
    current_price = tables.Column(verbose_name="Price $")
    market_cap = tables.Column()
    high_24h = tables.Column(verbose_name="high in 24h $")
    low_24h = tables.Column(verbose_name="low in 24h $")
    circulating_supply = tables.Column()
    total_supply = tables.Column()

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
