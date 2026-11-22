
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



def run_quality_checks(file_path: str) -> dict:
    """
    Exécute des contrôles déterministes de qualité des données.
    """

    df = pd.read_csv(file_path, sep=None, engine="python")

    issues = []

    # 1. Détection des lignes dupliquées
    duplicate_count = int(df.duplicated().sum())

    if duplicate_count > 0:
        issues.append({
            "rule": "duplicate_rows",
            "severity": "high",
            "count": duplicate_count,
            "message": f"{duplicate_count} ligne(s) dupliquée(s) détectée(s)."
        })

    # 2. Détection des valeurs manquantes
    for column in df.columns:

        missing_count = int(df[column].isna().sum())

        if missing_count > 0:
            issues.append({
                "rule": "missing_values",
                "column": column,
                "severity": "medium",
                "count": missing_count,
                "message": (
                    f"{missing_count} valeur(s) manquante(s) "
                    f"dans la colonne {column}."
                )
            })

    # 3. Vérification du format des emails
    if "email" in df.columns:

        invalid_email = (
            df["email"].notna()
            & ~df["email"].astype(str).str.match(
                r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
            )
        )

        invalid_count = int(invalid_email.sum())

        if invalid_count > 0:
            issues.append({
                "rule": "invalid_email",
                "column": "email",
                "severity": "high",
                "count": invalid_count,
                "message": f"{invalid_count} adresse(s) email invalide(s)."
            })

    # 4. Vérification des âges
    if "age" in df.columns:

        age = pd.to_numeric(df["age"], errors="coerce")

        invalid_age = age.notna() & ((age < 0) | (age > 120))
        invalid_count = int(invalid_age.sum())

        if invalid_count > 0:
            issues.append({
                "rule": "invalid_age",
                "column": "age",
                "severity": "high",
                "count": invalid_count,
                "message": f"{invalid_count} âge(s) incohérent(s)."
            })

    return {
        "total_issues": len(issues),
        "issues": issues
    }
