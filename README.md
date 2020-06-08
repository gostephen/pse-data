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

> ## Functions
>
> - **all_open_stocks()**: returns list of tickers of all open stocks
> - **filter_rsi(lower_bound, upper_bound)**: returns dictionary with key as ticker and value as RSI for all stocks that have RSI values within the given range
> - **lookup_current_info(ticker)**:
> - **lookup_historical_date(ticker, date)**: returns list with ticker information from specified date
> - **lookup_historical_range(ticker, start_date, end_date)**:
