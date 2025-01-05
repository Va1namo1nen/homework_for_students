from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    while True:
        yield from obj


class Cycle:
    def __init__(self, iterable: Iterable[T]):
        self.iterable = iterable
        self.it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self) -> T:
        try:
            return next(self.it)
        except StopIteration:
            self.it = iter(self.iterable)
            return next(self.it)