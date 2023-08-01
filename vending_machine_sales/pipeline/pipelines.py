from vending_machine_sales.pipeline.functions import (
    null_fields,
    replace_null_values,
)
from vending_machine_sales.pipeline.utils import numeric_format
from pandas import DataFrame
from vending_machine_sales.pipeline.options import (
    GroupOptions,
    PlotOptions,
    Aggregator,
)


class BasePipeline:
    def __init__(self, df: DataFrame) -> None:
        self.df = df

    @staticmethod
    def _group_by(df: DataFrame, options: GroupOptions) -> DataFrame:
        group = (
            df[options.fields]
            .groupby(by=options.group_fields)
            .agg({options.agg_field: options.agg})
            .rename(columns={options.agg_field: options.rename})
        )

        group = group.sort_values(options.rename, ascending=False)
        return group

    @staticmethod
    def _plot(df: DataFrame, options: PlotOptions) -> None:
        df = df.head(options.n_plot)
        df.plot.pie(
            y=options.field,
            figsize=(18, 18),
            autopct=lambda x: numeric_format(
                options.type_, x, df[options.field].sum()
            ),
            title=options.title,
        )
        return


class MostSellPipeline(BasePipeline):
    def by_amount(self, n_plot: int = None) -> DataFrame | None:
        most_sell_amount = super()._group_by(
            self.df,
            GroupOptions(
                ["Product", "MQty"],
                ["Product"],
                "MQty",
                Aggregator.count,
                "Amount",
            ),
        )

        if n_plot:
            super()._plot(
                most_sell_amount,
                PlotOptions(
                    n_plot, "Amount", "percentage", "Most Sell Products"
                ),
            )
            return

        return most_sell_amount

    def by_income(self, n_plot: int = None) -> DataFrame | None:
        most_sell_income = super()._group_by(
            self.df,
            GroupOptions(
                ["Product", "MPrice"],
                ["Product"],
                "MPrice",
                Aggregator.sum,
                "Income",
            ),
        )

        if n_plot:
            super()._plot(
                most_sell_income,
                PlotOptions(
                    n_plot, "Income", "money", "Most Profitable Products"
                ),
            )
            return

        return most_sell_income


class BestPlacePipeline(BasePipeline):
    ...
