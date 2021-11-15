#!/bin/bash
source /opt/conda/etc/profile.d/conda.sh
python parsing.py /home/jovyan/swefs_group1/correct_test_data/FiberPhoSig2020-08-22T09_00_59.csv
python plotting.py
python functions.py
