allPaths = []
def findPaths(maze,m,n):
    path = [0 for d in range(m+n-1)]
    findPathsUtil(maze,m,n,0,0,path,0)
     
def findPathsUtil(maze,m,n,i,j,path,index):
    global allPaths
    if i==m-1:
        for k in range(j,n):
            path[index+k-j] = maze[i][k]

        print(path)
        allPaths.append(path)
        return
    if j == n-1:
        for k in range(i,m):
            path[index+k-i] = maze[k][j]

        print(path)
        allPaths.append(path)
        return
     
    path[index] = maze[i][j]
     
    findPathsUtil(maze, m, n, i+1, j, path, index+1)
     
    findPathsUtil(maze, m, n, i, j+1, path, index+1)
 
# Driver Code
mat = [[1, 2, 3],
	[4, 5, 6]]

findPaths(mat, 2, 3)
