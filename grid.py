t=int(input())
ans=[]
for ti in range(t):
    nm=input().split()
    n=int(nm[0])
    m=int(nm[1])
    mt=[]
    for j in range(n):
        mt.append(list(map(int,input().split())))

    #making possible paths
    allPaths = []
    def findPaths(maze,m,n):
        path = [0 for d in range(m+n-1)]
        findPathsUtil(maze,m,n,0,0,path,0)        
    def findPathsUtil(maze,m,n,i,j,path,index):
        global allPaths
        if i==m-1:
            for k in range(j,n):
                path[index+k-j] = maze[i][k]
                if(maze[i][k]>0):
                    maze[i][k]-=1
            allPaths.append(path)
            return
        if j == n-1:
            for k in range(i,m):
                path[index+k-i] = maze[k][j]
                if(maze[k][j]>0):
                    maze[k][j]-=1

            allPaths.append(path)
            return
        
        path[index] = [i,j]
        
        findPathsUtil(maze, m, n, i+1, j, path, index+1)
        
        findPathsUtil(maze, m, n, i, j+1, path, index+1)

    def check_zeros(mt,n,m):
        zeros=0
        for i in range(n):
            for j in range(m):
                if mt[i][j]<0:
                    zeros=-1
                    break
                elif mt[i][j]==0:
                    zeros+=1

        if zeros == n*m :
            ans.append("YES")
        elif zeros == -1:
            ans.append("NO")
        else:
            findPaths(mt,n,m)
            print(allPaths)
            check_zeros(mt,n,m)

    check_zeros(mt,n,m)

print(ans)


