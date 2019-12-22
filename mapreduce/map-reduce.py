#!/usr/bin/env python
"""map-reduce.py"""

import subprocess
import datetime

subprocess.check_call(["/usr/local/hadoop/bin/hdfs", "dfs", "-mkdir", "-p", "/user/root/data/"])

subprocess.check_call(["/usr/local/hadoop/bin/hdfs", "dfs", "-copyFromLocal", "-f", "/data/youtube-statistics/", "/user/root/data/"])

current_date = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
output_path = "/user/root/output-" + current_date
subprocess.check_call(["/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar", "-file", "/mapreduce/mapper.py", "-mapper", "/mapreduce/mapper.py", "-file", "/mapreduce/reducer.py", "-reducer", "/mapreduce/reducer.py", "-input", "/user/root/data/youtube-statistics/trending-statistics", "-output", output_path])

subprocess.check_call(["/usr/local/hadoop/bin/hdfs", "dfs", "-copyToLocal", output_path, "/output"])
