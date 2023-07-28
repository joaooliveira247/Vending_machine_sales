from pandas import DataFrame, Series
from typing import Any


def null_fields(df: DataFrame) -> list[tuple[str, int]]:
    try:
        null_fields_count: Series = df.isnull().sum()
    except Exception:
        raise Exception("DataFrame don't loaded")

    null_fields = list(zip(null_fields_count.index, null_fields_count))

    return dict(
        [null_field for null_field in null_fields if null_field[1] > 0]
    )


def replace_null_values(df: DataFrame, replace: dict[str, Any]) -> DataFrame:
    for k, v in replace.items():
        try:
            df[k] = df[k].fillna(v)
        except Exception:
            raise KeyError(f"field {k} not found.")
    return df
