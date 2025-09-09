def nth_lucky_number(n: int) -> int:
    """
    4と7のみからなる10桁の整数のうち、N番目のものを返す。
    (memo 4を0, 7を1と捉えると2進数で考えられる)

    @param n: 1から始まる整数
    """
    digits = []
    n -= 1  # 0-indexedにする
    for _ in range(10):
        digits.append("4" if n % 2 == 0 else "7")
        n //= 2
    return int("".join(reversed(digits)))


if __name__ == "__main__":
    N = int(input())
    print(nth_lucky_number(N))
