let data = [2, 3, 1, 3, 2, 2, 1, 1, 3];
function changeFormat(data) {
	// get from the array, put in an array size of 3
	// get the starting from big and --, if it's less than 1 start over
	const big = 3;
	const size = 3;
	
	let result = [];
	let curr = big
	let start = big
	let newArr = []
	while (data.length > 0) {
		data.forEach((el, i) => {
			// Check if the current is 1, start over
			if(el == curr) {
				if(curr <= 1){
					curr = big
				} else {
					curr--
				}
				// Add the data to the array
				newArr.push(el)
				data.splice(i, 1)

				// Check if the array is full (3)
				// if it full, push and start over with different starting number.
				if(newArr.length == size) {
					result.push(newArr)
					newArr = [];
					start--
					curr = start
				}
			}
		});
	}

	return result
}

console.log(changeFormat(data));
