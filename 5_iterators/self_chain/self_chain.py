from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    for iterable in iterables:
        yield from iterable

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        self.iterables = iter(iterables)
        self.current_iter = iter(next(self.iterables, []))

    def __iter__(self):
        return self

    def __next__(self) -> T:
        while True:
            try:
                return next(self.current_iter)
            except StopIteration:
                self.current_iter = iter(next(self.iterables))