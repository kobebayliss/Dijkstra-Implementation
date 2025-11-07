# Dijkstra's Algorithm Implementation

Computes shortest travel times between sectors in a directed graph using Dijkstra's algorithm.

## Input and Output Format
**Input**
```
n m                 # number of nodes then edges
u v t               # directed edge from u to v with time t (repeated m times)
s                   # source node
```

**Output**
```
Sector 0: Travel time = x
Sector 1: Travel time = x
...
```

## Details

- **Time Complexity:** O((m + n) log n)
- **Requirements:** Python 3.x

**Usage**
```bash
python dijkstra.py <- input.txt
```
