import datetime as dt
import json as j
import math as m
import requests as r
import sys as s
import time as t
import yaml as y

def initialize_constants():
    c = {
        "check_interval": 15,
        "max_latency": dt.timedelta(seconds=0.5),
        "start_time": t.perf_counter(),
    }
    return c

def read_yaml_config():
    try:
        with open(s.argv[1]) as file:
            config = y.safe_load(file)
    except:
        print("ERROR: YAML config file required.")
        quit()
    for endpoint in config:
        endpoint["domain"] = endpoint["name"].split(" ")[0]
        endpoint["request_count"] = 0
        endpoint["up_count"] = 0
        endpoint["down_count"] = 0
        if "method" not in endpoint:
            endpoint["method"] = "GET"
        endpoint["method"] = endpoint["method"].lower()
    return config

def check_site_availability(endpoint, max_latency):
    res_code = 0
    res_time = dt.timedelta()
    arguments = {
        "url": endpoint["url"]
    }
    if "headers" in endpoint:
        arguments["headers"] = endpoint["headers"]
    if "body" in endpoint:
        arguments["json"] = j.loads(endpoint["body"])
    with getattr(r, endpoint["method"])(**arguments) as response:
        res_code = response.status_code
        res_time = response.elapsed
        endpoint["request_count"] += 1
    if res_time < max_latency and (res_code >= 200 and res_code <= 299):
        endpoint["up_count"] += 1
    else:
        endpoint["down_count"] += 1

def print_domain_availability(domain_list, config):
    for domain in domain_list:
        for endpoint in config:
            if domain[0] == endpoint["domain"]:
                domain[1] += endpoint["request_count"]
                domain[2] += endpoint["up_count"]
        percent_value = m.floor(100*(domain[2]/domain[1]))
        print(f"{domain[0]} has {percent_value}% availability percentage")

def main():
    config = read_yaml_config()
    c = initialize_constants()
    time_stamp = c["start_time"]
    is_start = True
    while True:
        # If check interval is passed, calculate and print results.
        if t.perf_counter() >= time_stamp + c["check_interval"] or is_start:
            is_start = False
            time_stamp = t.perf_counter()
            domain_list = []
            for endpoint in config:
                check_site_availability(endpoint, c["max_latency"])
                if not [endpoint["domain"],0 ,0] in domain_list:
                    domain_list.append([endpoint["domain"], 0, 0])
            print_domain_availability(domain_list, config)

print("START SCRIPT...")
try:
    main()
except KeyboardInterrupt:
    print("...END SCRIPT")