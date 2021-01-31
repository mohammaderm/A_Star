import numpy as np 
from queue import PriorityQueue
# Python 3.7.9

class Tile:
    def __init__(self, char):
        self.char = char
        self.g = 0
        self.h = 0
        self.f = 0
        self.location = [] 
        self.parent = None
    
    def __repr__(self):
        return self.char
    
    def __str__(self):
        return str(self.char)
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.location == other.location


grid = np.array([
    [Tile('s'), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('e')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
    [Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''), Tile(''),Tile(''),Tile('')],
])

blok = [
       [[0,7],[0,8]],[[2,0],[2,1]],[[0,2],[0,3]],[[3,2],[4,2]],[[1,1],[1,2]],[[0,4],[0,5]],[[4,1],[5,1]],[[6,1],[7,1]],[[8,1],[9,1]],[[2,3],[2,4]],[[1,8],[1,9]],[[2,5],[3,5]],[[7,4],[8,4]],[[2,6],[2,7]],[[0,1],[1,1]],[[1,4],[2,4]],[[5,2],[6,2]],[[1,5],[1,6]],
       [[1,7],[1,8]],[[3,0],[3,1]],[[1,2],[1,3]],[[3,3],[4,3]],[[2,1],[2,2]],[[1,4],[1,5]],[[4,3],[5,3]],[[6,2],[7,2]],[[8,3],[9,3]],[[3,3],[3,4]],[[2,8],[2,9]],[[2,6],[3,6]],[[7,5],[8,5]],[[5,6],[5,7]],[[0,3],[1,3]],[[1,5],[2,5]],[[5,5],[6,5]],
       [[4,7],[4,8]],[[4,0],[4,1]],[[2,2],[2,3]],[[3,5],[4,5]],[[3,1],[3,2]],[[4,4],[4,5]],[[4,4],[5,4]],[[6,6],[7,6]],[[8,4],[9,4]],[[5,3],[5,4]],[[7,8],[7,9]],[[2,7],[3,7]],[[7,6],[8,6]],[[6,6],[6,7]],[[0,6],[1,6]],[[1,7],[2,7]],[[5,8],[6,8]],
       [[5,7],[5,8]],[[6,0],[6,1]],[[7,2],[7,3]],[[3,6],[4,6]],[[5,1],[5,2]],[[6,4],[6,5]],[[4,6],[5,6]],[[6,7],[7,7]],[[8,5],[9,5]],[[7,3],[7,4]],[[8,8],[8,9]],[[2,8],[3,8]],[[7,7],[8,7]],
       [[7,7],[7,8]],[[7,0],[7,1]],[[8,2],[8,3]],[[3,7],[4,7]],[[8,1],[8,2]],[[7,4],[7,5]],[[4,9],[5,9]],[[6,9],[7,9]],[[8,6],[9,6]],
       [[8,7],[8,8]],[[8,0],[8,1]],[[9,2],[9,3]],[[3,8],[4,8]],
       [[9,7],[9,8]]
       ]


def A_start_Search(maze):
    open = PriorityQueue()
    close = []
    
    start_position = [0,0]
    end_position = [7,9]
    
    maze[start_position[0],start_position[1]].location = start_position
    maze[end_position[0],end_position[1]].location = end_position
    
    open.put(maze[start_position[0],start_position[1]])
                
    while open.qsize() > 0:
        
        current_node = open.get()
        close.append(current_node)
        
        if current_node.location == end_position:
            
            path = []
            while current_node.location != start_position:
                
                path.append(current_node.location)
                current_node = current_node.parent
            
            return path[::-1]
        
        neighbors = [[current_node.location[0]-1, current_node.location[1]],
                     [current_node.location[0]+1, current_node.location[1]],
                     [current_node.location[0], current_node.location[1]-1],
                     [current_node.location[0], current_node.location[1]+1]]
        
        for next in neighbors:
            
            if [current_node.location,next] in blok or [next,current_node.location] in blok:
                continue
            
            if next[1] < 0 or next[0] < 0 or next[0] > len(maze)-1 or next[1] > len(maze)-1:
                continue
            
            neighbor = Tile('')
            neighbor.location = next
            neighbor.parent = current_node
            
            if neighbor in close:
                continue
            
            neighbor.g = len(close)
            neighbor.h = abs(neighbor.location[0] - end_position[0]) + abs(neighbor.location[1] - end_position[1])
            neighbor.f = neighbor.g + neighbor.h
            
            if add_open(open, neighbor) == True:
                open.put(neighbor)
                
    return None
                                    
def add_open(open, neighbor):
    for node in open.queue:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True


step = 1
for i in A_start_Search(grid):
    if not grid[i[0],i[1]].char in ['s','e']: 
        grid[i[0],i[1]].char = str(step)
        step += 1  
   
print('\n')
print('\n'.join([''.join(['{:4}'.format(item.char) for item in row]) 
      for row in grid]))
print('\n')

print(A_start_Search(grid))









        
# def mergesort(list):
#     if len(list) > 1:
        
#         mid = (len(list)) / 2
#         mergesort(list[0:int(mid)])
#         mergesort(list[int(mid):len(list)])
        
#         i = j = k = 0
#         list1 = list[0:int(mid)]
#         list2 = list[int(mid):len(list)]
        
#         while i < len(list1) and j < len(list2):
#             if list1[i] < list2[j]:
#                 list[k] = list1[i]
#                 i += 1
#             else:
#                 list[k] = list2[j]
#                 j += 1
#             k += 1
            
#         while i < len(list1):
#             list[k] = list1[i]
#             i += 1
#             k += 1
 
#         while j < len(list2):
#             list[k] = list2[j]
#             j += 1
#             k += 1
#         print(list)
#     print(list)
    
# list = [5,8,2,12,1,33]
# mergesort(list)
# print(list)