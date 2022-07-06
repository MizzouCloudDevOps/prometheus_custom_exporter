# prometheus_custom_exporter

This repository includes two Prometheus basic exporters implemented in Python.  
- #1: random number generator: generates random numbers, exports the numbers in Gauge,
and the sum of the numbers as Counter metric, publish the data on port 9001 for 
Prometheus to consume and Grafana to visualize. 

- #2: log metric extractor: extract Http requests from Apache log file on any web server,
exports two Counter metrics, one for total number of http requests, and the other one 
for the total bytes for all the http requests. 

## Usage

Install client library:
```bash
$ pip3 install -r requirements.txt
```

- #1: 
```bash
$ python3 rand_num.py
```

- #2:
```bash
$ python3 log.py
```
