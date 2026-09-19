from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round as spark_round, when

spark = SparkSession.builder.appName("ProjetoSemantix").getOrCreate()

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("../data/base_capitais_educacao_2023.csv")
)

df = df.withColumn("delta_ideb", spark_round(col("ideb_2023") - col("ideb_2021"), 2))

df.select(
    "capital","uf","ideb_2021","ideb_2023","delta_ideb","ioeb_2023"
).show(30, truncate=False)

df.groupBy(
    when(col("ideb_2023") <= 5.0, "Até 5,0")
    .when(col("ideb_2023") < 6.0, "5,1 a 5,9")
    .otherwise("6,0 ou mais")
    .alias("faixa_ideb")
).count().show()

spark.stop()
