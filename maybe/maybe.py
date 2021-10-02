import dataclasses
from typing import Generic, TypeVar, Callable

T = TypeVar('T')
U = TypeVar('U')

Nothing = object()


@dataclasses.dataclass
class Maybe(Generic[T]):
    value: T = Nothing

    def bind(self: 'Maybe[T]', func: Callable[[T], 'Maybe[U]']) -> 'Maybe[U]':
        if self.value is Nothing:
            return self
        return func(self.value)

    def __matmul__(self, func: Callable[[T], 'Maybe[U]']) -> 'Maybe[U]':
        return self.bind(func)

    def __str__(self):
        return f'Just({self.value})' if self else 'Nothing'

    def __bool__(self):
        return self.value is not Nothing
