use std::fs::File;
use std::io::{self, BufRead};
use std::cmp::{min, max};

fn main() {
    println!("Hello, world!");
	let file = File::open("./input.txt").expect("cant read");
	let lines = io::BufReader::new(file).lines();

	let mut c = 0;
	for resultLine in lines {
		if let Ok(line) = resultLine {
			let (x, y) = line.split_once(",").expect("idk");

			let (xMin, xMax) = x.split_once("-").expect("idk");
			let (yMin, yMax) = y.split_once("-").expect("idk");
			let xMin : i32 = xMin.parse().expect("give up");
			let xMax : i32 = xMax.parse().expect("give up");
			let yMin : i32 = yMin.parse().expect("give up");
			let yMax : i32 = yMax.parse().expect("give up");
			let overlap = min(yMax, xMax) - max(xMin, yMin);


			if overlap >= 0 {
				/*if overlap == min(xMax - xMin, yMax - yMin) {
					c += 1;
				}*/
				c+= 1;
			}
		}
	}
	println!("{c}");
}	
