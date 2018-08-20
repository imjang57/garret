case class Bank(age: Integer, job: String, marital: String, education: String, balance: Integer)

/*
 * Create RDD and convert to Dataset
 */
// val bankTextRdd = sc.textFile("file:///Users/youngho/workspace/sample_data/bank/bank.csv")
// val bankDs = bankTextRdd.map(s=>s.split(";")).filter(s=>s(0)!="\"age\"").map(
//     s=>Bank(s(0).toInt, 
//             s(1).replaceAll("\"", ""),
//             s(2).replaceAll("\"", ""),
//             s(3).replaceAll("\"", ""),
//             s(5).replaceAll("\"", "").toInt
//         )
// ).toDS()

/*
 * Create DataFrame and convert to Dataset
 */
val bankDf = spark.read.option("header", "true").option("delimiter", ";").csv("file:///Users/youngho/workspace/sample_data/bank/bank.csv")
val bankDs = bankDf.select($"age", $"job", $"marital", $"education", $"balance").withColumn("age", $"age".cast(org.apache.spark.sql.types.IntegerType)).withColumn("balance", $"balance".cast(org.apache.spark.sql.types.IntegerType)).as[Bank]


bankDs.schema
bankDs.printSchema
bankDs.describe("age").show
bankDs.summary("mean").show
bankDs.groupBy($"age", $"job").count().withColumnRenamed("count", "cnt").show()

val countInAgeAndJob = bankDs.groupBy($"age", $"job").count()
countInAgeAndJob.withColumnRenamed("count", "cnt").show()
countInAgeAndJob.withColumnRenamed(countInAgeAndJob.columns(2), "cnt").show()

countInAgeAndJob.explain
bankDs.rdd.take(5)
bankDs.storageLevel

val bankRdd = bankDs.rdd.map(bank => ((bank.age, bank.job), (bank.marital, bank.education, bank.balance)))
bankRdd.take(5)
bankRdd.mapValues(data => data._3).reduceByKey((a, b) => a + b).take(5)

