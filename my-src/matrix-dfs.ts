declare type WeightedAdjacencyList = GraphEdge[][];
declare type GraphEdge = { to: number; weight: number };

const walk = (
  graph: WeightedAdjacencyList,
  curr: number,
  needle: number,
  seen: boolean[],
  path: number[]
): boolean => {
  // pre
  seen[curr] = true;
  if (curr === needle) return true;

  path.push(curr);

  //recurse
  const adjs = graph[curr];
  for (let i = 0; i < adjs.length; i++) {
    if (seen[adjs[i].to]) continue;

    const success = walk(graph, adjs[i].to, needle, seen, path);

    if (success) return true;
  }

  //post
  path.pop();
  return false;
};

const dfs = (graph: WeightedAdjacencyList, source: number, needle: number) => {
  let seen = new Array(graph.length).fill(false);
  let path = [];
  const found = walk(graph, source, needle, seen, path);

  if (!found) return null;

  return path.concat([needle]);
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
console.log(dfs(list2, 0, 5)); // [ 0, 1, 4, 5 ]
console.log(dfs(list2, 0, 6)); // [ 0, 1, 4, 5, 6 ]
console.log(dfs(list2, 5, 2)); // [ 5, 2 ]
console.log(dfs(list2, 5, 3)); // [ 5, 6, 3 ]
console.log(dfs(list2, 5, 1)); // null
console.log(dfs(list2, 3, 2)); // null
console.log(dfs(list2, 1, 0)); // null
