from maybe.maybe import Maybe
from maybe.safe import safe, safe_return, do

def safe_div_with_bind(mx: Maybe[int], my: Maybe[int]) -> Maybe[float]:
    return mx @ (lambda x: (
            my @ (lambda y: (safe_return(x / y)))
    ))


@safe
def div(mx: Maybe[int], my: Maybe[int]) -> Maybe[float]:
    x = do(mx)
    y = do(my)
    return safe_return(x / y)


def main():
    mx = Maybe[int](3)
    my = Maybe[int](10)
    mz = Maybe[int]()
    mr = safe_div_with_bind(my, mx)
    mr_2 = div(my, mz)
    print(mr, mr_2)


if __name__ == '__main__':
    main()
