declare type WeightedAdjacencyMatrix = number[][];

const bfs = (
  graph: WeightedAdjacencyMatrix,
  source: number,
  needle: number
) => {
  let seen = new Array(graph.length).fill(false);
  let prev = new Array(graph.length).fill(-1);
  let q = [source];

  while (q.length) {
    const curr = q.shift() as number;
    // console.log(curr);
    seen[curr] = true;

    if (curr == needle) break;

    const adjs = graph[curr];
    for (let i = 0; i < adjs.length; ++i) {
      if (adjs[i] === 0) {
        continue;
      }
      if (seen[i]) continue;

      prev[i] = curr;

      q.push(i);
    }
  }

  //   console.log("seen", seen);
  //   console.log("prev", prev);
  //   console.log("q", q);

  const path = [];

  let curr = prev[needle];

  while (curr !== -1) {
    path.push(curr);
    curr = prev[curr];
  }

  if (path.length == 0) return null;

  return path.reverse().concat([needle]);
};

//     >(1)<--->(4) ---->(5)
//    /          |       /|
// (0)     ------|------- |
//    \   v      v        v
//     >(2) --> (3) <----(6)
export const matrix2: WeightedAdjacencyMatrix = [
  [0, 3, 1, 0, 0, 0, 0], // 0
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 7, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 5, 0, 2, 0],
  [0, 0, 18, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 1],
];

console.log(bfs(matrix2, 0, 5)); // [ 0, 1, 4, 5 ]
console.log(bfs(matrix2, 0, 6)); // [ 0, 1, 4, 5, 6 ]
console.log(bfs(matrix2, 5, 2)); // [ 5, 2 ]
console.log(bfs(matrix2, 5, 3)); // [ 5, 6, 3 ]
console.log(bfs(matrix2, 5, 1)); // null
console.log(bfs(matrix2, 3, 2)); // null
console.log(bfs(matrix2, 1, 0)); // null
