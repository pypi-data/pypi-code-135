import numpy as np
import math
import collections
import matplotlib.pyplot as plt
import cv2 
from shapely.geometry import Polygon, Point

def get_version():
    return "0.0.1"

def cvContour2ShapelyPolygon(contour):
    """
    This method converts an OpenCV contour into a Shapely Polygon. 
        
        array([[[100, 200]], [[105, 205]], [[108, 208]]]) into POLYGON ((100 200, 105 205, 108 208))
        
    Input: 
    - contour: OpenCV contour
        
    Returns: 
    - Shapely Polygon
    """
    contour = np.squeeze(contour)
    polygon = Polygon(contour)
    return polygon
	
def shapelyPolygon2CvContour(poly):
    """
    This method converts a Shapely polygon into an OpenCV contour which is a specific numpy array structure.
    
        POLYGON ((100 200, 105 205, 108 208)) into array([[[100, 200]], [[105, 205]], [[108, 208]]])
    
    Input: 
    - poly: Shapely Polygon
    
    Returns: 
    - cont : OpenCV contour
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    x, y = poly.exterior.coords.xy
    arr_rep = zip(list(x), list(y))
    list_arr_rep = list(arr_rep)
    list_of_lists = [list(i) for i in list_arr_rep]
    x_cont = np.expand_dims(np.array(list_of_lists), 1)
    cont = x_cont.astype(int)
    return cont

def compactness(poly):
    """
    This method calculates the compactness of a polygon according to the Polsby-Popper Test
    Source: https://en.wikipedia.org/wiki/Polsby%E2%80%93Popper_test
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, Compactness value, or -1 if the input is not a valid Shapely Polygon 
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    area = poly.area
    perimeter = poly.length

    # (4 * PI * area) / perimeter ^ 2
    return (4*math.pi*area)/(perimeter**2)

def direction(poly):
    """
    This method calculates the angle of rotation of the minimum bounding box that covers the polygon. 
    
    Input: 
    - poly: shapely.geometry.polygon.Polygon
    
    Returs:
    - Float, direction in radians, or -1 if the input is not a valid Shapely Polygon
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    rotated_box = list(poly.minimum_rotated_rectangle.exterior.coords)
    len_edge_1 = math.hypot(rotated_box[3][0] - rotated_box[0][0], rotated_box[3][1] - rotated_box[0][1]) 
    len_edge_2 = math.hypot(rotated_box[1][0] - rotated_box[0][0], rotated_box[1][1] - rotated_box[0][1]) 
    print(len_edge_1, len_edge_2)

    if len_edge_1 <= len_edge_2:
        p1 = rotated_box[0]
        p2 = rotated_box[1]
    else:
        p1 = rotated_box[0]
        p2 = rotated_box[3]
        
    angle = np.arctan2(p2[0] - p1[0], p2[1] - p1[1])
    if angle > 0:
        rot_angle = np.degrees(angle)
    else: 
        rot_angle = np.degrees(angle) + 180
        
    return math.radians(rot_angle)

def aspectRatio(poly):
    """
    This method calculates the aspect ratio of a polygon. 
    Aspect ratio is the ratio of the longest edge of the rotated bounding box of the polygon to the shortest edge of it. 
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, aspect ratio value, or -1 if the input is not a valid Shapely Polygon 
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    box = poly.minimum_rotated_rectangle # get minimum bounding box around polygon
    x, y = box.exterior.coords.xy # get coordinates of polygon vertices
    edge_length = (Point(x[0], y[0]).distance(Point(x[1], y[1])), Point(x[1], y[1]).distance(Point(x[2], y[2]))) # get length of bounding box edges
    length = max(edge_length) # get length of polygon as the longest edge of the bounding box
    width = min(edge_length) # get width of polygon as the shortest edge of the bounding box
    aspectRatio = length / width

    return aspectRatio

def shapeFactor(poly):
    """
    This method calculates the shape factor of a polygon. 
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, shape factor value, or -1 if the input is not a valid Shapely Polygon 
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    area = poly.area
    perimeter = poly.length
    equivalentRadius = math.sqrt(area / math.pi)
    equivalentPerimeter = 2 * math.pi * equivalentRadius
    shapeFactor = perimeter / equivalentPerimeter
    return shapeFactor

def equivalentDiameter(poly):
    """
    This method calculates the equivalent diameter of a polygon. 
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, equivalent diameter value, or -1 if the input is not a valid Shapely Polygon 
    """
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    equivalentRadius = math.sqrt(poly.area / math.pi)
    equivalentDiameter = 2 * equivalentRadius
    return equivalentDiameter

def minorAndMajorAxisLength(poly):
    """
    This method calculates the minor and major axes of the minimum rotated bounding box of a polygon.
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, Float >> minor_axis, major_axis length values, or -1 if the input is not a valid Shapely Polygon 
    """
    from shapely.geometry import LineString
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    mbr_points = list(zip(*poly.minimum_rotated_rectangle.exterior.coords.xy)) # get the minimum bounding rectangle and zip coordinates into a list of point-tuples
    mbr_lengths = [LineString((mbr_points[i], mbr_points[i+1])).length for i in range(len(mbr_points) - 1)] # calculate the length of each side of the minimum bounding rectangle
    
    # get major/minor axis measurements
    minor_axis = min(mbr_lengths)
    major_axis = max(mbr_lengths)
    
    return minor_axis, major_axis

def eccentricity(poly):
    """
    A parameter of an ellipse (or a closed shape) indicating its deviation from the circularity whose value ranging from 0 (circle) to 1 (line).

    Eccentricity (also known as ellipticity) is the ratio of the length of the short (minor) axis to the length of the long (major) axis of an object:

    – The result is a measure of object eccentricity, given as a value between 0 and 1.

    eccentricity = minor_axis_length / major_axis_length
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, eccentricity value, or -1 if the input is not a valid Shapely Polygon 
    
    """
    from shapely.geometry import LineString
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    minor_axis_length, major_axis_length = minorAndMajorAxisLength (poly)
    
    return minor_axis_length / major_axis_length

def convexArea(poly):
    """
    This method returns the area of the convex hull (i.e., the smallest convex shape that contains the polygon) of a polygon. 
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, area of the convex hull of the polygon, or -1 if the input is not a valid Shapely Polygon 
    """
    from shapely.geometry import LineString
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    convexHullArea = poly.convex_hull.area
    return convexHullArea

def solidity(poly):
    """
    This method calculates the solidity of a polygon. 
    Solidity is a measure of density that is calculated as the ratio of the area of a polygon to the area of the convex hull of the polygon.
    
        solidity = area / convexArea

    A value close to 1 indicates a solid polygon while a value less than 1 indicates a polygon that contains holes or that has irregular boundaries.
    
    Input:
    - poly: shapely.geometry.polygon.Polygon
    
    Returns: 
    - Float, solidity value, or -1 if the input is not a valid Shapely Polygon 
    """
    from shapely.geometry import LineString
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    area = poly.area
    convexHullArea = poly.convex_hull.area
    return area / convexHullArea

def roundness(poly):
    """
    
    """
    from shapely.geometry import LineString
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    area = poly.area
    convex_perimeter = poly.convex_hull.length
    roundness = (4* math.pi * area) / (convex_perimeter ** 2)
    return roundness

def getAngleBetweenVectors(v1, v2):
    '''
    Calculates the angle between two vectors. 
    Input vectors must be provided as Numpy arrays. 
    
    INPUTS: v1 and v2: Numpy array.
    
    OUTPUT: angle between the two vectors. A value between 0 - 180. 
    
    '''
    o = np.array([0, 0])
    a = v1 - o
    b = v2 - o
    
    angle = 0
    
    if np.array_equal(a, b):
        angle = 0
        return(np.degrees(angle))
    else: 
        cosine_angle = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        #print("cosine angle: ", cosine_angle)
        angle = np.arccos(cosine_angle)
        #print("angle", angle)
        if math.isnan(angle):
            angle = 0
        return(np.degrees(angle))

    return(-1)


def uniqueness(poly, t=5, verbose=False):
    '''
    This method calculates the uniqueness metric of a closed polygon. 
    Uniqueness is the entropy of the histogram of the angle differences between consequtive tangents of a polygon. 
    The histogram is calculated in two steps:
        1) Compute the tangent vector of each point of the contour,
        2) Compute the histogram of the angle difference between consecutive tangents.  
    
    Implemented using the formulas in Liu et al, 2016. 
    
    INPUTS: 
    poly: The contour, in the format of an OpenCV contour.
    t: The number of points to skip when comparing tangents. 
    
    OUTPUT: 
    uniqueness: A value between 0 and 1. 
        A small entropy indicates a skewed histogram, thus, polygon containing more of  a single kind of angle, either acute or obtuse.
        A large entropy means a uniform distribution on the histogram, thus, a more complicated shape that contains both acute and obtuse angles. 
    '''
    
    if str(type(poly)) != "<class 'shapely.geometry.polygon.Polygon'>":
        print("Input is not a shapely.geometry.polygon ")
        return -1
    
    uniqueness = 0
    v_list = []
    dict_angle = {}
    poly_type = "cv_contour"
    #print(poly[-2][0][0])
    
    poly = list(poly.exterior.coords)
            
    
    ### STEP 1: Calculate the tangents for each point on the contour.
    for i in range(len(poly)):             
        p1_x = poly[i-2][0]
        p1_y = poly[i-2][1]
        p2_x = poly[(i+2)%len(poly)][0]
        p2_y = poly[(i+2)%len(poly)][1]
        #print(p1_x, p1_y, p2_x, p2_y)
        
        #print(i, [p1_x, p1_y], [p2_x, p2_y])
        deltaY = p2_y - p1_y
        deltaX = p2_x - p1_x
        tangent = np.array([deltaX, deltaY])
        #print(i, tangent)
        v_list.append(tangent)
        
    ### STEP 2: Compare the angle differences between t-consecutive tangents.
    count = 0
    for i in range(0, len(v_list), t):
        #print(i, v_list[(i+1)%len(v_list)], v_list[i])
        angle = math.floor(getAngleBetweenVectors(v_list[(i+1)%len(v_list)], v_list[i]))
        count = count + 1
        #angle = getVectorAngle(v_list[((i+1)*t)%len(v_list)] - v_list[i]*t)
        if verbose:
            print(i, math.floor(angle))

        if angle in dict_angle.keys():
            dict_angle[angle] = dict_angle[angle] + 1 
        else:
            dict_angle[angle] = 1 
    if verbose: 
        print("Number of tangent angle difference calculations: ", count)
    for key in dict_angle.keys():
        hist_value = dict_angle[key] / count
        uniqueness += np.log10(hist_value) * hist_value
    
    od = collections.OrderedDict(sorted(dict_angle.items()))
    for key in od.keys():
        od[key] = od[key] / count
    
    if verbose:
        print("Uniqueness: ", -uniqueness)
        print(od)
    return -uniqueness

