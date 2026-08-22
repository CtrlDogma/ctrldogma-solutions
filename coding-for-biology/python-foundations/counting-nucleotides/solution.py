import sys


def solve(s: str) -> None:
    a = s.count("A")
    c = s.count("C")
    g = s.count("G")
    t = s.count("T")

    print(a, c, g, t)


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    solve(s)