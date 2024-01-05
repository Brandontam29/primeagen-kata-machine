use rand::Rng;

fn bubble_sort(list: &mut Vec<i32>) {
    for i in 0..list.len() {
        for j in 0..list.len() - 1 - i {
            let current_value = list[j];
            let next_value = list[j + 1];
            if current_value > next_value {
                list[j] = next_value;
                list[j + 1] = current_value;
            }
        }
    }
}

fn main() {
    let mut random_numbers: Vec<i32> = (0..1000)
        .map(|_| rand::thread_rng().gen_range(0..1000))
        .collect();

    // print!("{:?}", random_numbers);

    bubble_sort(&mut random_numbers);

    print!("{:?}", random_numbers);
}
