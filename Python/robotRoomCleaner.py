class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 方向要顺时针或逆时针
        visited = set()
        self.dfs(0, 0, robot, 0, visited, directions)        
 
    def goBack(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnRight()
        robot.turnRight()
 
    def dfs(self, i, j, robot, start, visited, directions):
        print(i,j)
        if (i, j) in visited:
            return
        visited.add((i, j))
        robot.clean()

        for _ in range(len(directions)):
            if robot.move():
                self.dfs(i+directions[start][0], j+directions[start][1], robot, start, visited, directions)
                self.goBack(robot)
            robot.turnLeft()
            start = (start+1) % len(directions)
         