let all_numbers = document.getElementsByTagName('h1')[0].textContent
let numbers = all_numbers.split(',');

// creating an array of matrix
let arrayMatrix = new Array(100)
for(let i = 0; i < 100; i++){
	arrayMatrix[i] = Array(5).fill(1);
	for(let j = 0; j < 5; j++){
		arrayMatrix[i][j] = Array(5).fill("1");
	}
}

AllrowMatrix = document.getElementsByTagName('p')
let element = 0;	//rappresent the index of a line for example the index of: <p>30 46 94 20 2</p>
for(matrix = 0; matrix < 100; matrix++){
	for(let row = 0; row < 5; row++, element++){
		arrayRow = AllrowMatrix[element].textContent.split(' ') //transform "30 46 94 20 2" in an array of string
		for(let i = 0; i < 5; i++){
			arrayMatrix[matrix][row][i] = arrayRow[i];
		}
	}
}

var numberWinner = 0;
var counterWinner = 0;
var matrix_remaining = new Array(100).fill(1);
go_on = true;

for(let num = 0; num < numbers.length && go_on; num++){
	for(matrix = 0; matrix < 100 && go_on; matrix++){
		for(let row = 0; row < 5 && go_on; row++, element++){
			for(let i = 0; i < 5 && go_on; i++){
				if(arrayMatrix[matrix][row][i] == numbers[num]){
					arrayMatrix[matrix][row][i] = "X";
				}
			}
		}
	}
	numberWinner = numbers[num];
	go_on = checkWinner(arrayMatrix)
}

let result = 0;
for(let lastMatrix = 0; lastMatrix < matrix_remaining.length; lastMatrix++){
	if(matrix_remaining[lastMatrix] == 1){
		for(let row = 0; row < 5; row++){
			for (let i = 0; i < 5; i++){
				if(arrayMatrix[lastMatrix][row][i] != "X" && arrayMatrix[lastMatrix][row][i] != "O"){
					result += Number(arrayMatrix[lastMatrix][row][i])
				}
			}
		}
	}
}
console.log(result * numberWinner)

function checkWinner(arrayMatrix){
	let counterRow = 0;
	let counterColumn = 0;
	let go_on = true;

	for(matrix = 0; matrix < 100 && go_on; matrix++){
		for(let row = 0; row < 5 && go_on; row++){
			for(let i = 0; i < 5 && go_on; i++){
				if(arrayMatrix[matrix][row][i] == "X"){
					counterRow++
				}
				if(arrayMatrix[matrix][i][row] == "X"){
					counterColumn++
				}
			}
			if(counterRow == 5 || counterColumn == 5){
				if(counterWinner < 99){	//stop modifying when only 1 matrix remains
					matrix_remaining[matrix] = 0;
					for(let row2 = 0; row2 < 5; row2++){
						arrayMatrix[matrix][row2].fill("O");
					}
				}
				counterWinner++;
				if(counterWinner == 100){
					go_on = false;
				}
			}
			counterRow = 0;
			counterColumn = 0;
		}
	}
	return go_on;
}