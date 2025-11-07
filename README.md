# Dijkstra's Algorithm Implementation

Computes shortest travel times between sectors in a directed graph using Dijkstra's algorithm.

## Input Format
```
n m                 # number of nodes then edges
u v t               # directed edge from u to v with time t (repeated m times)
s                   # source node
```

## Output Format
```
Sector 0: Travel time = x
Sector 1: Travel time = x
...
```

## Details

- **Time Complexity:** O((m + n) log n)
- **Requirements:** Python 3.x

## How to Use
```bash
python dijkstra.py <- input.txt
```
