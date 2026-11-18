"""
Shortest trip with fuel and gas stations
Category: Graphs
Core algorithm: BFS on an expanded state (city, fuel)

Cities are connected by undirected roads. A car starts at `begin` with a full
tank of capacity c. Each road costs 1 unit of fuel. Arriving at a gas station
refills the tank to c. Return the fewest roads from `begin` to `end`, or -1 if
the car can't make it (it can run out of fuel). The graph is connected.

Example 1: roads 1-2-3-4, begin 1, end 4, c = 3, stations [2, 3] -> 3
Example 2: begin 0, end 6, c = 4, stations [4] -> 7 (0-1-2-3-4-3-5-6)
    0
    |
    1
    |
    2
    |
    3 - 4 (gas)
    |
    5
    |
    6

Approach: BFS where the state is (city, fuel), not just city. Example 2 needs
to visit city 3 twice: first with fuel 1, then with fuel 3 after refilling at
4. The visited set on (city, fuel) also stops loops like 3 -> 4 -> 3 -> 4.
Time O((V + E) * C), Space O(V * C) for visited/queue, plus O(V + E) for the graph
(simplified in the interview as O(N * C)).
"""
from collections import defaultdict, deque


def shortestTrip(begin: int, end: int, roads: list[list[int]],
                 gas_stations: list[int], c: int) -> int:
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)  # undirected: add both directions
    stations = set(gas_stations)

    queue = deque([(begin, c)])
    visited = {(begin, c)}
    dist = 0
    while queue:
        for _ in range(len(queue)):
            city, fuel = queue.popleft()
            if city == end:
                return dist
            if fuel == 0:
                continue  # stuck here, drop this path
            for nxt in graph[city]:
                nxt_fuel = c if nxt in stations else fuel - 1
                if (nxt, nxt_fuel) not in visited:
                    visited.add((nxt, nxt_fuel))
                    queue.append((nxt, nxt_fuel))
        dist += 1
    return -1


if __name__ == "__main__":
    assert shortestTrip(1, 4, [[1, 2], [2, 3], [3, 4]], [2, 3], 3) == 3

    sample = [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [5, 6]]
    assert shortestTrip(0, 6, sample, [4], 4) == 7
    assert shortestTrip(0, 6, sample, [], 4) == -1    # runs out of fuel
    assert shortestTrip(0, 6, sample, [], 6) == 5     # enough fuel, no detour
    assert shortestTrip(0, 0, sample, [], 0) == 0     # already there
    assert shortestTrip(0, 6, sample, [4], 0) == -1   # can't leave

    # Unreachable, but 1 -> 2 -> 1 refills forever (c = 2): must still terminate.
    assert shortestTrip(0, 4, [[0, 1], [1, 2], [2, 3], [3, 4]], [1], 2) == -1
    print("ok")
