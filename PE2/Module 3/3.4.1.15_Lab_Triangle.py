'''
Estimated time

30-60 minutes
Level of difficulty

Medium
Objectives

    improving the student's skills in defining classes from scratch;
    using composition.

Scenario

Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:

    the constructor accepts three arguments - all of them are objects of the Point class;
    the points are stored inside the object as a private list;
    the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)

Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Below you can copy the Point class code we used in the previous lab:


Expected output

3.414213562373095
'''

import math

class NotPointInstance(Exception):
    pass

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        dx = self.getx() - x
        dy = self.gety() - y
        return math.hypot(dx,dy)
    
    def distance_from_point(self, point):
        if isinstance(point, tuple|list):
            return self.distance_from_xy(point[0],point[1])
        elif not isinstance(point, Point):
            raise NotPointInstance("The parameter given is not an instance of Point class nor a two-argument tuple or list.")
        else:
            dx = self.getx() - point.getx()
            dy = self.gety() - point.gety()
        
            return math.hypot(dx,dy)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__lofv = [vertice1, vertice2, vertice3]
        if not all(isinstance(i,Point) for i in self.__lofv):
            raise NotPointInstance("Vertices should be passed as Point class instances.")

    def perimeter(self):
        a = self.__lofv[0].distance_from_point(self.__lofv[1])
        b = self.__lofv[1].distance_from_point(self.__lofv[2])
        c = self.__lofv[2].distance_from_point(self.__lofv[0])
        return a+b+c


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
