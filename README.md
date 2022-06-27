# prometheus_num_exporter

This is a Prometheus basic exporter implemented in Python, 
which generates random numbers, exports the numbers in 
Gauge and the sum of the numbers as Counter metric, publish
the data on port 9001 for Prometheus to consume and Grafana 
to visualize. 


### Usage:

pip3 install -r requirements.txt
python3 rand_num.py
