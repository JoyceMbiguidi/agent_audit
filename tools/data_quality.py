
import pandas as pd


def profile_csv(file_path: str) -> dict:
    """
    Analyse structurelle et statistique d'un fichier CSV.
    Retourne un profil de données sérialisable en JSON.
    """

    df = pd.read_csv(file_path, sep=None, engine="python")

    row_count, column_count = df.shape

    columns_profile = {}

    for column in df.columns:
        series = df[column]

        missing_count = int(series.isna().sum())
        distinct_count = int(series.nunique(dropna=True))

        sample_values = (
            series.dropna()
            .astype(str)
            .unique()[:3]
            .tolist()
        )

        columns_profile[column] = {
            "type": str(series.dtype),
            "missing_count": missing_count,
            "missing_percentage": float(
                round(missing_count / row_count * 100, 2)
            ) if row_count else 0.0,
            "distinct_count": distinct_count,
            "sample_values": sample_values
        }

    profile = {
        "file": file_path,
        "row_count": int(row_count),
        "column_count": int(column_count),
        "duplicate_rows": int(df.duplicated().sum()),
        "columns": columns_profile
    }

    return profile
