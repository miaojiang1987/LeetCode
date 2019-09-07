class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited=set()
        self.dfs(0,0,robot,0,directions,visited)
        
    def go_back(self,robot):
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
        
        
    def dfs(self,i,j,robot,start,directions,visited):
        if (i,j) in visited:
            return
        visited.add((i,j))
        robot.clean()
        
        for _ in range(len(directions)):
            if robot.move():
                self.dfs(i+directions[start][0],j+directions[start][1],robot,start,directions,visited)
                self.go_back(robot)
        
            robot.turnRight()
            start=(start+1)%(len(directions))