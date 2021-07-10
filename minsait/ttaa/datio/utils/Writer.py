from pyspark.sql import DataFrame

from minsait.ttaa.datio.common.Constants import *
from minsait.ttaa.datio.common.naming.PlayerInput import *


class Writer:
    def write(self, df: DataFrame):
        df \
            .coalesce(2) \
            .write \
            .partitionBy(teamPosition.name) \
            .mode(OVERWRITE) \
            .parquet(OUTPUT_PATH);
