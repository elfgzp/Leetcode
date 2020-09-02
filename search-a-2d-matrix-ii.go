package Leetcode

//选左上角，往右走和往下走都增大，不能选
//
//选右下角，往上走和往左走都减小，不能选
//
//选左下角，往右走增大，往上走减小，可选
//
//选右上角，往下走增大，往左走减小，可选

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) <= 0 {
		return false
	}

	rows := len(matrix)

	row := 0
	col := len(matrix[0]) - 1

	for row < rows && col >= 0 {
		if matrix[row][col] == target {
			return true
		}

		if matrix[row][col] > target {
			col -= 1
		} else {
			row += 1
		}
	}
	return false
}