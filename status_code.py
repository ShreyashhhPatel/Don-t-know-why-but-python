def stat_code(stat:int)->str:
    match stat:        
        case 200: return "OK"
        case 404: return "Not Found"
        case 500: return "Internal Server Error"
        case 403: return "Forbidden"
        case 301: return "Moved Permanently"
        case 302: return "Found"
        case 400: return "Bad Request"

    return "Unknown Status Code"


# tuples to check co-ordianates
# **Practice**
# 1. Use `match` to classify a tuple `(x, y)` as `"origin"`, `"x-axis"`, `"y-axis"`, or `"quadrant"`.  
#    _Expected_: (0,0)→origin; (0,5)→y-axis; etc.

def check_coordinates(coord:tuple)->str:
    match coord:
        case (0, 0): return "Origin"
        case (x, 0): return "X-axis"
        case (0, y): return "Y-axis"
        case (x, y) if x > 0 and y > 0: return "Quadrant 1"
        case (x, y) if x < 0 and y > 0: return "Quadrant 2"
        case (x, y) if x < 0 and y < 0: return "Quadrant 3"
        case (x, y) if x > 0 and y < 0: return "Quadrant 4"
        case _: return "On an axis"

point1 = (0, 0)
point2 = (5, 0) 
point3 = (0, 7)
point4 = (3, 4) 

print(f"Point {point1} is in {check_coordinates(point1)}")
print(f"Point {point2} is in {check_coordinates(point2)}")
print(f"Point {point3} is in {check_coordinates(point3)}")
print(f"Point {point4} is in {check_coordinates(point4)}")
