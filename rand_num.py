import time
import random
from os import path
import yaml
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server
totalRandomNumber = 0
class RandomNumberCollector(object):
    def __init__(self):
        pass
    def collect(self):
        rand_num = random.randint(1,20)
        gauge = GaugeMetricFamily("random_number", "A random number gauge", labels=["randomNum"])
        gauge.add_metric(['random_num'], rand_num)
        yield gauge
        count = CounterMetricFamily("random_number_2", "A random number counter", labels=['randomNum'])
        global totalRandomNumber
        totalRandomNumber += rand_num
        count.add_metric(['random_num'], totalRandomNumber)
        yield count

if __name__ == "__main__":
    port = 9001
    frequency = 1

    start_http_server(port)
    REGISTRY.register(RandomNumberCollector())
    while True:
        # period between collection
        time.sleep(frequency)
