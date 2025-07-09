# US State Capitals Geo-Enricher

This Python script enriches a JSON file of U.S. state capitals adresses by adding *latitude* and *longitude* using ZIP codes.  

I wanted a lightweight, code-based way to enhance location data, with no heavy tools.
It helped me explore working with structured files, dictionaries, and basic geodata.

## What it does

- Takes a JSON file with state capitals and their ZIP codes  
- Looks up geographic coordinates for each ZIP code  
- Adds `latitude` and `longitude` to each capital  
- Outputs a new JSON file that includes coordinates for each capital

## Files

- `main.py` — Main script  
- `us_state_capitals.json` — Input file with capitals and ZIPs  
- `us_state_capitals_with_coords.json` — Output file with coordinates added
