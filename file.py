#!/usr/bin/env python3
import os
import datetime

with open("/tmp/priv_test_log.txt", "a") as f:
    f.write(f"Executed by UID={os.getuid()} at {datetime.datetime.now()}\n")
