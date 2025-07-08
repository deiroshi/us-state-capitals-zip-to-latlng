import json

# Load ZIP data and extract coordinates
with open("georef-united-states-of-america-zc-point.json", "r") as f:
    zip_data = json.load(f) # 

# Create dictionary(ZIP to {lat,lon})
zip_coords = {}
for entry in zip_data:
    zip_code = entry.get("zip_code", "").zfill(5)  # pad ZIPs with zeros
    geo = entry.get("geo_point_2d")

    if zip_code and geo and "lat" in geo and "lon" in geo:
        zip_coords[zip_code] = {
            "lat": geo["lat"],
            "lon": geo["lon"]
        }

# Load state capital data
with open("us_state_capitals.json", "r") as f:
    capital_data = json.load(f)

# Add coordinates to each capital
for capital in capital_data["state_capitals"]:
    zip_code = capital.get("zip", "").zfill(5)
    coords = zip_coords.get(zip_code, {"lat": None, "lon": None})
    capital["coordinates"] = coords # Add

# Save the result
with open("us_state_capitals_with_coords.json", "w") as f:
    json.dump(capital_data, f, indent=2) # Make it readable