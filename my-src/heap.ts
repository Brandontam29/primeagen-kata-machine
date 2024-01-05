class Heap<T extends number> {
  data: T[];

  constructor() {
    this.data = [];
  }
  insert(datum: T) {
    this.data.push(datum);

    this.heapifyUp(this.data.length - 1);
  }

  delete(i: number) {}

  private heapifyDown(i: number) {}
  private heapifyUp(i: number) {
    const parent = this.getParent(i);
    const parentV = this.data[parent];
    this.data[parent] = this.data[i];
    this.data[i] = parentV;
    this.heapifyUp(parent);
  }

  private getChildren(i: number) {
    return [i * 2 + 1, i * 2 + 2];
  }
  private getParent(i: number) {
    return Math.floor((i - 1) / 2);
  }
}

export default Heap;
