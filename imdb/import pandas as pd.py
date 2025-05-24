import pandas as pd

# Specify the full file path
file_path = r"D:\re 4\imdb\imdb_movies_sample.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Drop rows with missing movie titles
df = df.dropna(subset=["title"])

# Fill missing numerical fields with their mean
for col in ["rating", "runtime", "votes", "budget", "revenue"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")  # Convert to numeric, forcing errors to NaN
        df[col] = df[col].fillna(df[col].mean())  # Fill NaN values with the column's mean

# Convert year to integer if possible
df["year"] = pd.to_numeric(df["year"], errors="coerce")  # Convert to numeric, forcing errors to NaN
df = df.dropna(subset=["year"])  # Drop rows where year is NaN
df["year"] = df["year"].astype(int)  # Convert year to integer

# Drop duplicate rows
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("imdb_movies_cleaned.csv", index=False)

print("Cleaned dataset saved as imdb_movies_cleaned.csv")
