class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # record the past points, search to tell if met
        points = [(0, 0)]

        # map directions to the movings
        dt_to_value = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
        }

        last_point = (0, 0)
        for dt in path:
            # print(dt)
            # detect if path cross itself

            # calculate the new point
            new_x = last_point[0] + dt_to_value[dt][0]
            new_y = last_point[1] + dt_to_value[dt][1]

            # check crossing
            if (new_x, new_y) in points:
                return True
            else:
                points.append((new_x, new_y))
                last_point = (new_x, new_y)
                
        return False
        
        
        
        