from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    it = iter(obj)
    while (batch := tuple([x for _, x in zip(range(n), it)])):
        yield batch


class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        self.it = iter(obj)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self) -> tuple[T, ...]:
        batch = tuple(x for _, x in zip(range(self.n), self.it))
        if not batch:
            raise StopIteration
        return batch