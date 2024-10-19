from pyspark.sql import DataFrame
from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import IntegerType, StringType, DoubleType, DateType, TimestampType

spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

# Function to change column data types
def change_column_schema(df: DataFrame, schema_dict: dict) -> DataFrame:
    for col_name, new_type in schema_dict.items():
        # If the target type is TimestampType, apply to_timestamp with the required format
        if isinstance(new_type, TimestampType):
            # Apply the timestamp transformation with MM/DD/YYYY HH:mm:ss format
            df = df.withColumn(col_name, to_timestamp(col_name, "M/d/yyyy H:mm"))
        else:
            # For other types, use cast() to change the column type
            df = df.withColumn(col_name, df[col_name].cast(new_type))
    
    return df
