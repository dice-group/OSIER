#!/bin/bash

RUN_NUM=$1

nosetests -s test_rdfize_all_tables.py > rdfize_test_run_$RUN_NUM 2> rdfize_test_run_$RUN_NUM.err
