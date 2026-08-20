import sys


def solve(s: str) -> None:
    complement = str.maketrans("ACGT", "TGCA")
    reverse_complement = s.translate(complement)[::-1]
    print(reverse_complement)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    solve(s)