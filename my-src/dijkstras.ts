declare type WeightedAdjacencyList = GraphEdge[][];
declare type GraphEdge = { to: number; weight: number };

const hasUnvisited = (seen, dists): boolean => {
  return seen.some((s, i) => !s && dists[i] < Infinity);
};

const getLowestUnvisited = (seen, dists): number => {
  let lowest = [-1, Infinity];
  dists.forEach((d, i) => {
    if (d < lowest[1] && !seen[i]) {
      lowest = [i, d];
    }
  });

  return lowest[0];
};

const dijkstra = (
  graph: WeightedAdjacencyList,
  source: number,
  needle: number
) => {
  let dists = new Array(graph.length).fill(Infinity);
  dists[source] = 0;
  let prev = new Array(graph.length).fill(-1);
  let seen = new Array(graph.length).fill(false);

  while (hasUnvisited(seen, dists)) {
    const curr = getLowestUnvisited(seen, dists);
    console.log(curr);
    seen[curr] = true;
    const adjs = graph[curr];

    //update
    for (let i = 0; i < adjs.length; i++) {
      const edge = adjs[i];

      if (seen[edge.to]) continue;

      const newDist = dists[curr] + edge.weight;

      if (newDist < dists[edge.to] || dists[edge.to] === -1) {
        dists[edge.to] = newDist;
        prev[edge.to] = curr;
      }
    }
  }

  console.log("dists", dists);
  console.log("prev", prev);
  console.log("seen", seen);
};
export const list2: WeightedAdjacencyList = [];

//     >(1)<--->(4) ---->(5)
//    /          |       /|
// (0)     ------|------- |
//    \   v      v        v
//     >(2) --> (3) <----(6)
list2[0] = [
  { to: 1, weight: 3 },
  { to: 2, weight: 1 },
];
list2[1] = [{ to: 4, weight: 1 }];
list2[2] = [{ to: 3, weight: 7 }];
list2[3] = [];
list2[4] = [
  { to: 1, weight: 1 },
  { to: 3, weight: 5 },
  { to: 5, weight: 2 },
];
list2[5] = [
  { to: 2, weight: 18 },
  { to: 6, weight: 1 },
];
list2[6] = [{ to: 3, weight: 1 }];
list2[7] = [{ to: 6, weight: 1 }];

dijkstra(list2, 0, 6);
