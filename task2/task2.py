import sys

circle_file_path = sys.argv[1]
points_file_path = sys.argv[2]

with open(circle_file_path, 'r', encoding='utf-8') as file:
    circle_data = file.readlines()

center_coordinates = circle_data[0].strip().split()
circle_center = [float(center_coordinates[0]), float(center_coordinates[1])]
circle_radius = float(circle_data[1].strip())

with open(points_file_path, 'r', encoding='utf-8') as file:
    points_data = file.readlines()

points = []
for line in points_data:
    coordinates = line.strip().split()
    point = [float(coordinates[0]), float(coordinates[1])]
    points.append(point)


def point_position(center, radius, point):
    x_center, y_center = center
    x_point, y_point = point
    distance_squared = (x_point - x_center) ** 2 + (y_point - y_center) ** 2
    radius_squared = radius ** 2
    if distance_squared == radius_squared:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


for point in points:
    position = point_position(circle_center, circle_radius, point)
    print(position)
