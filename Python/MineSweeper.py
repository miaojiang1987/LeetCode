class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row=len(board)
        col=len(board[0])
        stack = [(click[0],click[1])]
        
        visited=set()
        
        while stack!=[]:
            x,y=stack.pop()
            visited.add((x,y))
            
            if board[x][y]=='M':
                board[x][y]='X'
            
            else:
                temp=[]
                count=0
                
                for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    if 0<=x+i<len(board) and 0<=y+j<len(board[0]):
                        if board[x+i][y+j]=='M':
                            count += 1
                        if (x+i,y+j) not in visited:
                            temp.append((x+i,y+j))
                if count == 0:
                    board[x][y] = 'B'
                    stack += temp
                else:
                    board[x][y] = str(count)
        return board
                