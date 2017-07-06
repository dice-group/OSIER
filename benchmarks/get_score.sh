#!/bin/bash
grep "Score" test_run_cat_super | cut -c 8- | awk '{s+=$1} END {print s}'
