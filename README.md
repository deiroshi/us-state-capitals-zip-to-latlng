# U.S. State Capitals – Coordinate Enrichment Script

This project enriches a JSON file of U.S. state capitals by adding **latitude and longitude** to each entry using ZIP codes.  
The original file (`us_state_capitals.json`) included state names, capital names, addresses, and ZIPs, but it lacked geographic coordinates.  
This script fills in that missing data using a public ZIP code dataset.


## Features

- Reads U.S. capital info from a JSON file
- Uses ZIP codes to match each capital to its coordinates
- Loads a full ZIP code geolocation dataset in JSON format
- Outputs a new JSON file with coordinates added to each capital


## How It Works

1. **Input Files**  
   - Loads `us_state_capitals.json` (missing coordinates)
   - Loads `georef-united-states-of-america-zc-point.json` (ZIP -> lat/lon)

2. **ZIP Matching**  
   - For each capital, finds the matching ZIP code in the geolocation file
   - Extracts latitude and longitude

3. **Output**  
   - Generates a new file: `us_state_capitals_with_coords.json`
   - Each capital now includes its lat/lon under a `"coordinates"` field


## Notes

- No external API is used — all data is processed locally
- CSV version of the ZIP dataset was available, but JSON parsing was easier
- Coordinates are approximate, based on the center of each ZIP code
- Script can be reused for any ZIP-to-coordinates task in the U.S.


## Files

`main.py` - Python script that performs the ZIP -> coordinates mapping  
`us_state_capitals.json` - original input file (missing lat/lon)  
`georef-united-states-of-america-zc-point.json` - ZIP code geolocation dataset  
`us_state_capitals_with_coords.json` - final output with coordinates added
