import math
import numpy as np


# Convert latitude and longitude to Cartesian coordinates
def latlon_to_xy(lat, lon, origin_lat, origin_lon):
    earth_radius = 6371000  # meters
    dx = (lon - origin_lon) * (math.pi / 180.0) * earth_radius * math.cos(math.radians(lat))
    dy = (lat - origin_lat) * (math.pi / 180.0) * earth_radius
    return dx, dy

# Find the closest point on the path to the current vehicle position
def find_closest_point(path_x, path_y, x, y):
    dx = np.array(path_x) - x
    dy = np.array(path_y) - y
    dist = np.hypot(dx, dy)
    closest_idx = np.argmin(dist)
    closest_point = (path_x[closest_idx], path_y[closest_idx])
    return closest_point, closest_idx

# Calculate the lookahead point based on current speed
def calculate_lookahead_point(path_x, path_y, x, y, speed, min_lookahead, max_lookahead, min_speed, max_speed):
    _, closest_idx = find_closest_point(path_x, path_y, x, y)
    
    # Scale the lookahead distance based on current speed
    if speed < min_speed:
        speed = min_speed
    elif speed > max_speed:
        speed = max_speed

    lookahead_distance = min_lookahead + (max_lookahead - min_lookahead) * ((speed - min_speed) / (max_speed - min_speed))
    
    total_distance = 0
    for i in range(closest_idx, len(path_x) - 1):
        dx = path_x[i+1] - path_x[i]
        dy = path_y[i+1] - path_y[i]
        segment_length = math.hypot(dx, dy)
        total_distance += segment_length
        
        if total_distance > lookahead_distance:
            lookahead_point = (path_x[i+1], path_y[i+1])
            return lookahead_point

# Stanley controller to compute the steering angle for path following
def stanley_controller(path_x, path_y, x, y, yaw, speed,
                       wheelbase, max_steer, min_lookahead, max_lookahead, min_speed, max_speed):
    lookahead_point = calculate_lookahead_point(path_x, path_y, x, y, speed, min_lookahead, max_lookahead, min_speed, max_speed)
    if lookahead_point is None:
        return 0  # No lookahead point could be found, so don't steer

    # Compute the heading error
    heading_error = math.atan2(lookahead_point[1] - y, lookahead_point[0] - x)
    heading_error -= yaw
    
    # Wrap the error to [-pi, pi]
    heading_error = (heading_error + math.pi) % (2 * math.pi) - math.pi
    
    # Compute cross track error
    closest_point, _ = find_closest_point(path_x, path_y, x, y)
    cross_track_error = math.hypot(closest_point[0] - x, closest_point[1] - y)
    
    # Compute the steering angle using Stanley controller
    steer_angle = heading_error + math.atan2(2 * wheelbase * math.sin(heading_error), speed)
    
    # Limit the steering angle to the maximum steering capability of the vehicle
    steer_angle = np.clip(steer_angle, -max_steer, max_steer)
    
    return steer_angle

# Test the Stanley controller
path_lat = [
    37.2988071, 37.298808199999996, 37.2988103, 37.298814199999995,
    37.2988213, 37.2988289, 37.2988357, 37.2988424, 37.2988494,
    37.2988572, 37.2988648, 37.2988721, 37.2988777, 37.2988852,
    37.298893199999995, 37.298901199999996, 37.298908999999995, 37.2989171,
    37.2989254, 37.2989332, 37.2989405, 37.2989471, 37.2989525,
    37.2989564, 37.2989572
]

path_lon = [
    126.83789519999999, 126.8378936, 126.8378918, 126.83788999999999,
    126.8378857, 126.8378814, 126.83787699999999, 126.8378723, 126.83786819999999,
    126.83786339999999, 126.8378585, 126.8378534, 126.8378482, 126.83784379999999,
    126.83783989999999, 126.8378352, 126.83783039999999, 126.8378243, 126.8378185,
    126.8378132, 126.8378084, 126.83780469999999, 126.837801, 126.8377982,
    126.83779779999999
]

origin_lat, origin_lon = path_lat[0], path_lon[0]
path_x, path_y = [], []

for lat, lon in zip(path_lat, path_lon):
    x, y = latlon_to_xy(lat, lon, origin_lat, origin_lon)
    path_x.append(x)
    path_y.append(y)

current_lat, current_lon = 37.0005, 127.0005
current_speed = 10.0  # m/s
current_yaw = 0.1  # radians

x, y = latlon_to_xy(current_lat, current_lon, origin_lat, origin_lon)

wheelbase = 1.35  # meters
max_steer = np.radians(30)  # 30 degrees to radians
min_lookahead = 5.0  # meters
max_lookahead = 20.0  # meters
min_speed = 1.0  # m/s
max_speed = 20.0  # m/s

steer_angle = stanley_controller(path_x, path_y, x, y, current_yaw, current_speed,
                                wheelbase, max_steer, min_lookahead, max_lookahead, min_speed, max_speed)

# Convert the steer angle from radians to degrees for easier interpretation
steer_angle_deg = np.degrees(steer_angle)
print(steer_angle_deg)
