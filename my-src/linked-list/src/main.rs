// Define a Node struct to represent each element in the linked list
struct Node<T> {
    data: T,
    next: Option<Box<Node<T>>>,
}

// Define a LinkedList struct to manage the list
struct LinkedList<T> {
    head: Option<Box<Node<T>>>,
}

impl<T> LinkedList<T> {
    // Create an empty linked list
    fn new() -> Self {
        LinkedList { head: None }
    }

    // Add a new element to the front of the list
    fn push(&mut self, data: T) {
        let new_node = Box::new(Node {
            data,
            next: self.head.take(),
        });

        self.head = Some(new_node);
    }

    // Remove the first element from the list and return its value
    fn pop(&mut self) -> Option<T> {
        self.head.take().map(|node| {
            self.head = node.next;
            node.data
        })
    }

    // Check if the list is empty
    fn is_empty(&self) -> bool {
        self.head.is_none()
    }
}

fn main() {
    let mut list: LinkedList<i32> = LinkedList::new();

    list.push(1);
    list.push(2);
    list.push(3);

    while let Some(value) = list.pop() {
        println!("{}", value);
    }
}
