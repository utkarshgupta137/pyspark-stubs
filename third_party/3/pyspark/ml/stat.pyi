# Stubs for pyspark.ml.stat (Python 3)

from typing import Any, Optional

from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.wrapper import JavaWrapper
from pyspark.sql.column import Column
from pyspark.sql.dataframe import DataFrame

from py4j.java_gateway import JavaObject  # type: ignore

class ChiSquareTest:
    @staticmethod
    def test(dataset: DataFrame, featuresCol: str, labelCol: str) -> DataFrame: ...

class Correlation:
    @staticmethod
    def corr(dataset: DataFrame, column: str, method: str = ...) -> DataFrame: ...

class KolmogorovSmirnovTest:
    @staticmethod
    def test(
        dataset: DataFrame, sampleCol: str, distName: str, *params: float
    ) -> DataFrame: ...

class Summarizer:
    @staticmethod
    def mean(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def sum(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def variance(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def std(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def count(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def numNonZeros(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def max(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def min(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def normL1(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def normL2(col: Column, weightCol: Optional[Column] = ...) -> Column: ...
    @staticmethod
    def metrics(*metrics: str) -> SummaryBuilder: ...

class SummaryBuilder(JavaWrapper):
    def __init__(self, jSummaryBuilder: JavaObject) -> None: ...
    def summary(
        self, featuresCol: Column, weightCol: Optional[Column] = ...
    ) -> Column: ...

class MultivariateGaussian:
    mean: Vector
    cov: Matrix
    def __init__(self, mean: Vector, cov: Matrix) -> None: ...

class ANOVATest:
    @staticmethod
    def test(dataset: DataFrame, featuresCol: str, labelCol: str) -> DataFrame: ...

class FValueTest:
    @staticmethod
    def test(dataset: DataFrame, featuresCol: str, labelCol: str) -> DataFrame: ...
