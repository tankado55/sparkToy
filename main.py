import pyspark
import pandas as pd
from pyspark.sql import SparkSession


def main():
    data = pd.read_csv('dataset.csv')
    print(data)
    spark = SparkSession.builder.appName('Practise').getOrCreate()
    df_pyspark = spark.read.option('header', 'true').csv('dataset.csv')

    df_pyspark.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
