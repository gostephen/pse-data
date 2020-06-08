# pse-data
Access data for the Philippine Stock Exchange with Python

## Dependencies

Pandas 

## Usage

from pseData import PseData

### Lookup ticker information from last trading day
PseData().lookup_current_info("JFC")

### Lookup price information for historical range
PseData().lookup_historical_range("JFC", "2020-06-01", "2020-06-05")
