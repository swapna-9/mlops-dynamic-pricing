# Function to handle duplicate rows
def handle_duplicates(df: DataFrame, subset=None) -> DataFrame:
    df = df.dropDuplicates(subset=subset)
    return df