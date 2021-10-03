from maybe.maybe import Maybe
from maybe.safe import safe, safe_return, do


def safe_div_with_bind(mx: Maybe[int], my: Maybe[int]) -> Maybe[float]:
    return mx @ (lambda x: (
            my @ (lambda y: (safe_return(x / y)))
    ))


def drop_zero(x: int) -> Maybe[float]:
    return Maybe(x) if x != 0 else Maybe()


@safe
def div(mx: Maybe[int], my: Maybe[int]) -> Maybe[float]:
    x = do(mx)
    y = do(my @ drop_zero)
    return safe_return(x / y)


def main():
    print(div(
        Maybe[int](3), Maybe[int](0)
    ))
    print(div(
        Maybe[int](9), Maybe[int](3)
    ))


if __name__ == '__main__':
    main()
