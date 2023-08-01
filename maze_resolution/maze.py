import curses
from curses import wrapper
import queue
import time

maze=[["#","#","#","#","#","O","#","#","#"],
      ["#"," "," "," "," "," "," "," ","#"],
      ["#"," ","#","#"," ","#","#"," ","#"],
      ["#"," ","#"," "," "," ","#"," ","#"],
      ["#"," ","#"," ","#"," ","#"," ","#"],
      ["#"," ","#"," ","#"," ","#"," ","#"],
      ["#"," ","#"," ","#"," ","#","#","#"],
      ["#"," "," "," "," "," "," "," ","#"],
      ["#","#","#","#","#","#","#","X","#"]]

def possible_points(maze,point):
    row=point[0]
    col=point[1]
    points_list=list()
    if row-1>0: #UP
        points_list.append((row-1, col))
    if row+1<len(maze): #DOWN
        points_list.append((row+1, col))
    if col-1>0: #LEFT
        points_list.append((row, col-1))
    if col+1<len(maze[0]): #RIGHT
        points_list.append((row, col+1))
    return points_list

def building_path(maze):
    #We first look for the starting point
    for i in range(0,len(maze[0])): #len(maze) da el número de filas, len (maze[0]) da el número de columnas
        if maze[0][i]=="O":
            starting_point=(0,i)
    #already_visited={starting_point}
    q=queue.Queue()
    q.put((starting_point,[starting_point])) # The second part refers to the path followed
    #Now we have to analise the first point in the queue
    already_visited=set()
    final=False
    while final!=True:
        visit=q.get()
        path=visit[1]
        points_list=possible_points(maze,visit[0])
        already_visited.add(visit[0])
        for i in points_list:
            if maze[i[0]][i[1]]=="#":
                continue
            elif i in already_visited==True:
                continue
            elif maze[i[0]][i[1]]=="X":
                final_point=i
                final_path=path+[i]
                final=True
            else:
                q.put((i,path+[i]))

    return final_point, final_path

def maze_parts(maze,stdscr):
    for i,row in enumerate(maze):
        for j, value in enumerate(maze[i]):
            stdscr.addstr(i,j*2,value)

def main(stdscr):
    stdscr.clear()
    maze_parts(maze,stdscr)
    #stdscr.refresh()
    result, path=building_path(maze)
    for i in path:
        stdscr.addstr(i[0],i[1]*2,'.')
    stdscr.refresh()
    stdscr.getch()

wrapper(main)