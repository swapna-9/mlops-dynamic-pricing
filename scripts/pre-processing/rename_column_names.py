# Function to rename columns
def rename_columns(df: DataFrame, columns_dict: dict) -> DataFrame:
    for old_name, new_name in columns_dict.items():
        df = df.withColumnRenamed(old_name, new_name) 
    return df