import sys

def solve(s: str) -> None:
    gc_count = s.count("G") + s.count("C")
    gc_percentage = (gc_count / len(s)) * 100

    print(f"{gc_percentage:.2f}")


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    solve(s)