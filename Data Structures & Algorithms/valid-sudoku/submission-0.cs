public class Solution
{
    public bool IsValidSudoku(char[][] board)
    {
        Dictionary<int, HashSet<char>> columns = new();
        Dictionary<int, HashSet<char>> rows = new();
        Dictionary<int, HashSet<char>> subGrid = new();

        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[i].Length; j++)
            {
                char current = board[i][j];

                if (current != '.')
                {
                    // ROWS
                    if (!rows.TryGetValue(i, out HashSet<char> rowSet))
                    {
                        rowSet = new HashSet<char>();
                        rows[i] = rowSet;
                    }

                    if (rowSet.Contains(current))
                    {
                        return false;
                    }
                    else
                    {
                        rows[i].Add(current);
                    }

                    // COLUMNS
                    if (!columns.TryGetValue(j, out HashSet<char> columnSet))
                    {
                        columnSet = new HashSet<char>();
                        columns[j] = columnSet;
                    }

                    if (columnSet.Contains(current))
                    {
                        return false;
                    }
                    else
                    {
                        columns[j].Add(current);
                    }

                    // SECTIONS
                    int index = (i / 3) * 3 + (j / 3);
                    
                    if (!subGrid.TryGetValue(index, out HashSet<char> gridSet))
                    {
                        gridSet = new HashSet<char>();
                        subGrid[index] = gridSet;
                    }

                    if (gridSet.Contains(current))
                    {
                        return false;
                    }
                    else
                    {
                        subGrid[index].Add(current);
                    }
                }
            }
        }

        return true;
    }
}