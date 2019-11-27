import math

# in metres
EARTH_RADIUS = 6371000



def haversin(theta):
    return math.pow(math.sin(theta/2), 2)


def distance():
    lat1 = float(input("Write the latitude of your first point "))
    lon1 = float(input("Write the longitude of your first point "))

    lat2 = float(input("Write the latitude of your second point "))
    lon2 = float(input("Write the longitude of your second point "))

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    lambda1 = math.radians(lon1)
    lambda2 = math.radians(lon2)

    delta_phi = phi2 - phi1
    delta_lambda = lambda2 - lambda1

    # h = hav(central angle), see the formula
    h = haversin(delta_phi) + math.cos(phi1) * math.cos(phi2) * haversin(delta_lambda)

    distance_in_metres = round(2 * EARTH_RADIUS * math.asin(math.sqrt(h)))
    distance_in_kilometres = round(distance_in_metres / 1000)

    #result = [distance_in_metres, distance_in_kilometres]

    return distance_in_kilometres


