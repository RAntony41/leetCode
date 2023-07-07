class Solution:
    def checkStraightLine(self, coordinates:int) -> bool:
        coord_len = len(coordinates) 

        if coord_len <= 2:
            return True

        # slopeA - slopeB = 0
        def calculate_slope(x1, y1, x2, y2, x, y):
            return (y2 - y1) * (x - x1) - (y - y1) * (x2 - x1) 


        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        

        for i in range(2, coord_len):
            x, y = coordinates[i]
            
            if calculate_slope(x1, y1, x2, y2, x, y) != 0:
                return False

        return True
            

sol = Solution.checkStraightLine(0,[[0,0],[0,5],[5,5],[5,0]])
print(sol)