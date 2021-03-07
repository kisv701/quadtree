from quadtree import QuadTree, Point
from matplotlib import pyplot as plt
import random
import math

def draw_quadtree(ax, qt):
  nodes = [qt] # Traverse tree, starts at root

  # Draw a rectangle around covered area
  x1 = qt.bottomLeft.x
  x2 = qt.topRight.x
  y1 = qt.bottomLeft.y
  y2 = qt.topRight.y
  ax.plot([x1, x2], [y1, y1], '-k')
  ax.plot([x1, x2], [y2, y2], '-k')
  ax.plot([x1, x1], [y1, y2], '-k')
  ax.plot([x2, x2], [y1, y2], '-k')

  while nodes: # Go over every node
    node = nodes.pop()
    if node.is_leaf(): # Leafes are not drawn, they are just an area, so continue
      continue
    
    x1 = node.bottomLeft.x
    x2 = node.topRight.x
    y1 = node.bottomLeft.y
    y2 = node.topRight.y

    # Draw cross boundering the 4 children
    ax.plot([(x1+x2) / 2, (x1+x2) / 2], [y1, y2], '-k')
    ax.plot([x1, x2], [(y1+y2) / 2, (y1+y2) / 2], '-k')

    # Add every child node to the list of nodes
    nodes.append(node.northWest)
    nodes.append(node.northEast)
    nodes.append(node.southWest)
    nodes.append(node.southEast)

def draw_query_result(ax, qt, circle):
  # Draw a circle around queried area

  # Generate a full circle of small samples
  angles = [(i/100.0 * 2.0 * 3.14) for i in range(101)] 
  xs = [circle.x + circle.value * math.cos(a) for a in angles]
  ys = [circle.y + circle.value * math.sin(a) for a in angles]

  ax.plot(xs, ys, '-r', label="Query boundary")

  points_in_circle = qt.get_points_in_circle(circle)

  ax.plot([p.x for p in points_in_circle], [p.y for p in points_in_circle], '*r', label="Selected Points")


if __name__ == '__main__':
  points = []
  qt = QuadTree()

  # Make equally spaced 2D points
  for x in range(-100, 100, 10):
    for y in range(-100,100, 10):
      # Generate some noise to make things interresting
      rx = random.normalvariate(0, 20)
      ry = random.normalvariate(0, 20)
      # Add noisy point to list of points
      points.append(Point(x + rx, y + ry))
  
  fig, ax = plt.subplots()  #create figure and axes
  ax.plot([p.x for p in points], [p.y for p in points], '.', label="Points") # Plot points

  # Add points to quadtree
  for p in points:
    qt.add_point(p)
  
  # Plot the quadtree
  draw_quadtree(ax, qt)
  draw_query_result(ax, qt, Point(-23, -18, 30))
  plt.legend()
  plt.show()
