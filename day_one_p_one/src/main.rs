use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file = File::open("./src/input.txt").expect("cant read");
    let lines = io::BufReader::new(file).lines();
    let mut largest_elves = [0, 0, 0];
    let mut currentCount: i32 = 0;
    for line in lines.flatten() {
        if line.is_empty() {
            largest_elves = check_insert_into(largest_elves, currentCount);
            currentCount = 0;
        } else {
            currentCount += line.parse::<i32>().unwrap();
        }
    }
    largest_elves = check_insert_into(largest_elves, currentCount);
    let sum: i32 = largest_elves.iter().sum();
    println!("{sum}")
}

fn check_insert_into(mut currentElves: [i32; 3], currentVal: i32) -> [i32; 3] {
    if currentElves[2] < currentVal {
        currentElves[2] = currentVal;
        if currentElves[2] > currentElves[1] {
            (currentElves[1], currentElves[2]) = (currentElves[2], currentElves[1]);
            if currentElves[1] > currentElves[0] {
                (currentElves[0], currentElves[1]) = (currentElves[1], currentElves[0]);
            }
        }
    }
    currentElves
}
