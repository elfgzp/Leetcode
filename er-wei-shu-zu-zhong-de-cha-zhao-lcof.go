func findNumberIn2DArray(matrix [][]int, target int) bool {
    if len(matrix) < 1 || len(matrix[0]) < 1 {
        return false
    }
    
    row, col := 0, len(matrix[0]) - 1
    for row < len(matrix) && col >= 0 {
        if target > matrix[row][col] {
            row ++ 
        } else if target < matrix[row][col] {
            col --
        } else {
            return true
        }
    }
    return false
}
