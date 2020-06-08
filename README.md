# pse-data
Access data for the Philippine Stock Exchange with Python

## Dependencies
```
pip install pandas
```
## Usage
```python
from pseData import PseData
```
### Lookup ticker information from last trading day
```python
PseData().lookup_current_info("JFC")
```
### Lookup price information for historical range
```python
PseData().lookup_historical_range("JFC", "2020-06-01", "2020-06-05")
```
