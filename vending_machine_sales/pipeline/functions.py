from pandas import DataFrame, Series


def null_fields(df: DataFrame) -> list[tuple[str, int]]:
    try:
        null_fields_count: Series = df.isnull().sum()
    except Exception:
        raise Exception("DataFrame don't loaded")

    null_fields = list(zip(null_fields_count.index, null_fields_count))

    return [null_field for null_field in null_fields if null_field[1] > 0]
