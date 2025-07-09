# US State Capitals – With Coordinates

This Python script adds latitude and longitude to each U.S. state capital using ZIP codes. The original JSON file (`us_state_capitals.json`) already had state names, capital names, adresses, and ZIPs, but it was missing geographic coordinates.

## What I Did

At first, I thought about using an API or doing it through Ubuntu or Gloodata, but most API services either needed authentication or cost money, and I didn’t want to deal with that. So I decided to just write the whole thing myself.

I found a free dataset of U.S. ZIP codes with coordinates. I downloaded it as a CSV file first (because it's smaller), but parsing CSV with JSON was a hassle, so I re-downloaded the same file as JSON and used that instead.


## Files

- `main.py`- the script
- `us_state_capitals.json` - list of state capitals (without coordinates)
- `georef-united-states-of-america-zc-point.json` - big US geodataset with lat/lon
- `us_state_capitals_with_coords.json` - final output with coordinates added
