# Stubs for pyspark.context (Python 3.5)
#

from typing import Any, Dict, Iterable, List, Optional, Tuple, TypeVar
from pyspark.accumulators import Accumulator, AccumulatorParam
from pyspark.broadcast import Broadcast
from pyspark.conf import SparkConf
from pyspark.profiler import Profiler
import pyspark.rdd as rdd
from pyspark.serializers import Serializer
from pyspark.status import StatusTracker
from py4j.java_gateway import JavaGateway, JavaObject  # type: ignore

T = TypeVar('T')
U = TypeVar('U')

class SparkContext:
    PACKAGE_EXTENSIONS = ...  # type: Iterable[str]
    def __init__(self, master: Optional[str] = ..., appName: Optional[str] = ..., sparkHome: Optional[str] = ..., pyFiles: Optional[List[str]] = ..., environment: Optional[Dict[str, str]] = ..., batchSize: int = ..., serializer: Serializer = ..., conf: Optional[SparkConf] = ..., gateway: Optional[JavaGateway] = ..., jsc: Optional[JavaObject] = ..., profiler_cls: type = ...) -> None: ...
    def __getnewargs__(self): ...
    def __enter__(self): ...
    def __exit__(self, type, value, trace): ...
    @classmethod
    def getOrCreate(cls, conf: Optional[SparkConf] = ...) -> 'SparkContext': ...
    def setLogLevel(self, logLevel: str) -> None: ...
    @classmethod
    def setSystemProperty(cls, key: str, value: str) ->  None: ...
    @property
    def version(self) -> str: ...
    @property
    def applicationId(self) -> str: ...
    @property
    def uiWebUrl(self) -> str: ...
    @property
    def startTime(self) -> int: ...
    @property
    def defaultParallelism(self) -> int: ...
    @property
    def defaultMinPartitions(self) -> int: ...
    def stop(self) -> None: ...
    def emptyRDD(self) -> rdd.RDD[None]: ...
    def range(self, start: int, end: Optional[int] = ..., step: int = ..., numSlices: Optional[int] = ...) -> rdd.RDD[int]: ...
    def parallelize(self, c: Iterable[T], numSlices: Optional[int] = ...) -> rdd.RDD[T]: ...
    def pickleFile(self, name: str, minPartitions: Optional[int] = ...) -> rdd.RDD[Any]: ...
    def textFile(self, name: str, minPartitions: Optional[int] = ..., use_unicode: bool = ...) -> rdd.RDD[str]: ...
    def wholeTextFiles(self, path: str, minPartitions: Optional[int] = ..., use_unicode: bool = ...) -> rdd.RDD[Tuple[str, str]]: ...
    def binaryFiles(self, path: str, minPartitions: Optional[int] = ...) -> rdd.RDD[Tuple[str, bytes]]: ...
    def binaryRecords(self, path: str, recordLength: int) -> rdd.RDD[bytes]: ...
    def sequenceFile(self, path: str, keyClass: Optional[str] = ..., valueClass: Optional[str] = ..., keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., minSplits: Optional[int] = ..., batchSize: int = ...) -> rdd.RDD[Tuple[T, U]]: ...
    def newAPIHadoopFile(self, path: str, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[Dict[str, str]] = ..., batchSize: int = ...) -> rdd.RDD[Tuple[T, U]]: ...
    def newAPIHadoopRDD(self, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[Dict[str, str]] = ..., batchSize: int = ...) -> rdd.RDD[Tuple[T, U]]: ...
    def hadoopFile(self, path: str, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[Dict[str, str]] = ..., batchSize: int = ...) -> rdd.RDD[Tuple[T, U]]: ...
    def hadoopRDD(self, inputFormatClass: str, keyClass: str, valueClass: str, keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[Dict[str, str]] = ..., batchSize: int = ...) -> rdd.RDD[Tuple[T, U]]: ...
    def union(self, rdds: Iterable[rdd.RDD[Any]]) -> rdd.RDD[Any]: ...
    def broadcast(self, value: T) -> Broadcast[T]: ...
    def accumulator(self, value, accum_param: Optional[AccumulatorParam] = ...) -> Accumulator: ...
    def addFile(self, path: str, recursive: bool = ...) -> None: ...
    def addPyFile(self, path: str) -> None: ...
    def setCheckpointDir(self, dirName: str) -> None: ...
    def setJobGroup(self, groupId: str, description: str, interruptOnCancel: bool = ...) -> None: ...
    def setLocalProperty(self, key: str, value: str) -> None: ...
    def getLocalProperty(self, key: str) -> Optional[str]: ...
    def sparkUser(self) -> str: ...
    def setJobDescription(self, value: str) -> None: ...
    def cancelJobGroup(self, groupId: str) -> None: ...
    def cancelAllJobs(self) -> None: ...
    def statusTracker(self) -> StatusTracker: ...
    def runJob(self, rdd: rdd.RDD[T], partitionFunc, partitions: Optional[List[int]] = ..., allowLocal: bool = ...) -> List[T]: ...
    def show_profiles(self) -> None: ...
    def dump_profiles(self, path: str) -> None: ...
    def getConf(self) -> SparkConf: ...
