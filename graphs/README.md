# Graphs

**Core idea:** on an unweighted graph, BFS level by level gives the shortest path. When the answer depends on more than the node (fuel, keys, steps left), make the state `(node, extra)` and put the full state in both the queue and the visited set.

**Clarify first:** directed or undirected (decides how the graph is built; for directed, ask about cycles), and what to return when the target is unreachable (usually -1).


| # | Problem | Core algorithm | Time | Space |
|---|---------|----------------|------|-------|
| — | [Shortest Trip with Fuel and Gas Stations](gas_station_shortest_path.py) | BFS on state (city, fuel), refill to c at stations | O((V + E) · C) | O(V · C) |

## Mistakes to remember

**Shortest Trip with Fuel and Gas Stations**
- Didn't ask whether the graph is directed. Built it one way, so the car couldn't go back 4 → 3. Undirected: add both directions.
- `visited` on city only blocks 3 → 4 → 3 (city 3 is needed twice, with fuel 1 and then 3). The state is (city, fuel).
- One shared `fuel` variable for the whole BFS. Fuel belongs to each queue entry: `city, fuel = queue.popleft()`, `queue.append((nxt, fuel - 1))`.
- `if not beginCity ...: return 0`: city 0 is falsy, so the sample (begin = 0) returns right away. Unreachable should return -1, not 0.
- `if currCity == endCity` was nested inside the gas-station check, so the end was only detected at a station.
- `visited = set(fuel, city)` is invalid (`set` takes one iterable) and was never checked in the loop. Use `visited = {(begin, c)}`.
- `queue.append(city, fuel - 1)` passes two arguments; it needs a tuple. Typos: `defualtdict`, `gasStaion`, `fule`; type hint `list(list(int))` → `list[list[int]]`.
- Pruning is needed for termination, not just speed: without `visited`, an unreachable end plus a refill loop (3 ↔ 4) runs forever. Without a station, fuel alone bounds the search.
