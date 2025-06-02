import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print("Missing values per column before cleaning:\n", df.isnull().sum())

missing_rows = df[df.isnull().any(axis=1)]
print("\nRows with at least one missing value:\n", missing_rows.head())

df.fillna("Unknown", inplace=True)

print("\nMissing values per column after fillna:\n", df.isnull().sum())

num_duplicates = df.duplicated().sum()
print("\nNumber of exact-duplicate rows before drop:", num_duplicates)

df.drop_duplicates(keep="first", inplace=True)

print("Number of exact-duplicate rows after drop:", df.duplicated().sum())

if "gender" in df.columns:
    df["gender"] = df["gender"].astype(str).str.strip().str.lower()
    gender_map = {
        "m": "Male", "male": "Male",
        "f": "Female", "female": "Female",
        "unknown": "Unknown", "": "Unknown"
    }
    df["gender"] = df["gender"].map(gender_map).fillna("Other/Unspecified")
    df["gender"] = df["gender"].astype("category")

if "country" in df.columns:
    df["country"] = df["country"].astype(str).str.strip().str.title()
    country_map = {
        "Usa": "United States", "Us": "United States", "United States Of America": "United States",
        "Uk": "United Kingdom", "U.K.": "United Kingdom", "Uae": "United Arab Emirates",
    }
    df["country"] = df["country"].replace(country_map)

if "date_added" in df.columns:
    df["date_added"] = df["date_added"].astype(str).str.replace("#", "", regex=False).str.strip()
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["date_added"] = df["date_added"].fillna(pd.NaT)
    df["date_added"] = df["date_added"].dt.strftime("%d-%m-%Y")
    df["date_added"] = df["date_added"].fillna("Unknown")

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

df.rename(
    columns={
        "age ": "age",
        "date_of_birth": "dob",
    },
    inplace=True
)

print("\nColumn headers after renaming:\n", list(df.columns))

if "age" in df.columns:
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["age"] = df["age"].astype("Int64")

if "release_year" in df.columns:
    df["release_year"] = pd.to_numeric(df["release_year"], errors="coerce").astype("Int64")

if "price" in df.columns:
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

print("\nFinal data types:\n", df.dtypes)

df.to_csv("finals_clean.csv", index=False)
print("\n✅ Cleaned dataset saved as 'final_clean.csv'")
