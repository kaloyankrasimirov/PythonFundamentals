import re
places = input()
travel_points = 0
pattern = r"([=\/])([A-Z][a-zA-z]{2,})\1"
matches = re.findall(pattern, places)
locations = [location[1] for location in matches]
for location in locations:
    travel_points += len(location)
print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")

