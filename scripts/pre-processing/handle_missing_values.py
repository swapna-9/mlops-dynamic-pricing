from pyspark.sql.functions import col, when, count

def handle_missing_values(df):
    # Calculate null value percentages for each column
    null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
    total_count = df.count()
    null_percentages = null_counts.rdd.flatMap(lambda x: x).collect()
    null_percentages_dict = {df.columns[i]: null_percentages[i] / total_count * 100 for i in range(len(df.columns))}

    # Iterate through columns and apply handling logic
    for column, percentage in null_percentages_dict.items():
        if percentage > 50:
            # Fill nulls with 'unknown' if percentage is greater than 50%
            df = df.withColumn(column, when(col(column).isNull(), "unknown").otherwise(col(column)))
        elif percentage > 0:  # Only drop rows if there are null values
            # Drop rows with nulls if percentage is less than 50%
            df = df.dropna(subset=[column])
    
    return df