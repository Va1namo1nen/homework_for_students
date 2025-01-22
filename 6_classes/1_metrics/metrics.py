import csv
from datetime import datetime, timezone
from typing import Protocol

class FileStorage(Protocol):
    def write_to_file(self, records: list[list[str | int]]) -> None:
        pass

class CSVFileStorage:
    def __init__(self, path: str):
        self.path = path
        self._initialize_file()

    def write_to_file(self, records: list[list[str | int]]) -> None:
        with open(self.path, "a", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerows(records)

    def _initialize_file(self) -> None:
        with open(self.path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";", lineterminator="\n")
            writer.writerow(["date", "metric", "value"])

class TextFileStorage:
    def __init__(self, path: str):
        self.path = path
        self._initialize_file()

    def write_to_file(self, records: list[list[str | int]]) -> None:
        with open(self.path, "a", newline="") as file:
            for record in records:
                date, metric, value = record
                file.write(f"{date} {metric} {value}\n")

    def _initialize_file(self) -> None:
        with open(self.path, "w", newline="") as _:
            pass

class Statsd:
    def __init__(self, buffer_size: int, storage: FileStorage):
        self.buffer_size = buffer_size
        self.storage = storage
        self.buffer = []

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._flush_buffer()

    def _record_metric(self, metric: str, value: int) -> None:
        self.buffer.append([_current_utc_time(), metric, value])
        if len(self.buffer) >= self.buffer_size:
            self._flush_buffer()

    def _flush_buffer(self) -> None:
        if self.buffer:
            self.storage.write_to_file(self.buffer)
            self.buffer.clear()

    def incr(self, metric_name: str) -> None:
        self._record_metric(metric_name, 1)

    def decr(self, metric_name: str) -> None:
        self._record_metric(metric_name, -1)

def _current_utc_time() -> str:
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")


def get_txt_statsd(path: str, buffer_size: int = 10) -> Statsd:
    if not path.endswith(".txt"):
        raise ValueError("Файл должен быть с расширением '.txt'")
    return Statsd(buffer_size, TextFileStorage(path))


def get_csv_statsd(path: str, buffer_size: int = 10) -> Statsd:
    if not path.endswith(".csv"):
        raise ValueError("Файл должен быть с расширением '.csv'")
    return Statsd(buffer_size, CSVFileStorage(path))