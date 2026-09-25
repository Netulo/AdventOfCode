# Advent of Code

My solutions to [Advent of Code](https://adventofcode.com) — the yearly December
series of programming puzzles. So far: **43 days across 10 editions**, in
Python, C++, C and PHP.

For me AoC is a game: a set of riddles to crack, a way to test myself and to
compete with my colleagues. That's why **every solution here is written by me** —
solving it myself is the whole point. Some puzzles I solved in more than one
language to compare approaches, and some solutions are first attempts or
unfinished; I keep them as I wrote them.

| Year | Days | Solved days | Languages |
|---|---:|---|---|
| [2015](https://adventofcode.com/2015) | 12 | [1](<2015/Day 1>), [2](<2015/Day 2>), [3](<2015/Day 3>), [4](<2015/Day 4>), [5](<2015/Day 5>), [6](<2015/Day 6>), [7](<2015/Day 7>), [8](<2015/Day 8>), [11](<2015/Day 11>), [12](<2015/Day 12>), [13](<2015/Day 13>), [14](<2015/Day 14>) | Python, C++, PHP |
| [2016](https://adventofcode.com/2016) | 2 | [6](<2016/Day 6>), [7](<2016/Day 7>) | Python |
| [2017](https://adventofcode.com/2017) | 3 | [2](<2017/Day 2>), [8](<2017/Day 8>), [12](<2017/Day 12>) | Python |
| [2018](https://adventofcode.com/2018) | 2 | [2](<2018/Day 2>), [5](<2018/Day 5>) | Python |
| [2019](https://adventofcode.com/2019) | 1 | [2](<2019/Day 2>) | Python |
| [2020](https://adventofcode.com/2020) | 2 | [4](<2020/Day 4>), [6](<2020/Day 6>) | Python |
| [2021](https://adventofcode.com/2021) | 3 | [4](<2021/Day 4>), [9](<2021/Day 9>), [13](<2021/Day 13>) | Python |
| [2022](https://adventofcode.com/2022) | 4 | [3](<2022/Day 3>), [4](<2022/Day 4>), [7](<2022/Day 7>), [8](<2022/Day 8>) | Python |
| [2023](https://adventofcode.com/2023) | 8 | [1](<2023/Day 1>), [2](<2023/Day 2>), [3](<2023/Day 3>), [4](<2023/Day 4>), [5](<2023/Day 5>), [6](<2023/Day 6>), [7](<2023/Day 7>), [8](<2023/Day 8>) | Python, C++ |
| [2025](https://adventofcode.com/2025) | 6 | [1](<2025/Day 1>), [2](<2025/Day 2>), [3](<2025/Day 3>), [4](<2025/Day 4>), [5](<2025/Day 5>), [6](<2025/Day 6>) | Python, C |

## Layout

```
YYYY/Day N/
├── python/   p1.py, p2.py      (or one file with both parts)
├── cpp/      p1.cpp, p2.cpp
├── c/ · php/
└── input.txt                   not in the repo — see below
utils/        small shared helpers (Python)
```

## Running

Puzzle inputs are **not** included — Advent of Code
[asks not to share them](https://adventofcode.com/about). Download your own input
and save it as `input.txt` in the day's folder.

- **Python** — most solutions are run from the repository root, e.g.
  `python "2025/Day 5/aoc_2025_5.py"`. Older ones may expect a slightly different path.
- **C / C++** — compile and run from the solution's folder, e.g.
  `g++ -O2 p1.cpp -o p1 && ./p1`.
