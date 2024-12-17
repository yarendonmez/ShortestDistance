from math import sqrt

def generate_combinations(points):
    combinations = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            combinations.append((points[i], points[j]))
    return combinations

def distancePoints(cordinates_list):
    results = []  # Tüm mesafeleri saklamak için bir liste
    for item in cordinates_list:
        point1 = item[0]
        point2 = item[1]
        distance = euclideanDistance(point1, point2)
        print(f"Distance of point {point1} and point {point2} is {distance}")
        results.append(distance)  # Mesafeyi listeye ekle
    return results

def euclideanDistance(point1, point2):
    point1_x = point1[0]
    point1_y = point1[1]

    point2_x = point2[0]
    point2_y = point2[1]

    result = sqrt(((point1_x - point2_x) ** 2) + ((point1_y - point2_y) ** 2))  # ** ile düzeltildi
    return result

# Ana program
point_list = [(2, 5), (14, 6), (3, 9)]
combinations = generate_combinations(point_list)

# Tüm noktalar arasındaki mesafeleri hesapla
distances = distancePoints(combinations)
print("All distances:", distances)


def find_shortest_distance(points):
    combinations = generate_combinations(points)
    min_distance = float('inf')
    closest_points = None

    for point1, point2 in combinations:
        distance = euclideanDistance(point1, point2)
        if distance < min_distance:
            min_distance = distance
            closest_points = (point1, point2)

    print(f"En kısa mesafe: {min_distance} iki nokta arasında: {closest_points}")
    return min_distance, closest_points

find_shortest_distance(point_list)

