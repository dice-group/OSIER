#!/bin/bash
grep "Score" $1 | cut -c 8- | awk '{s+=$1} END {print s}'
grep "Score" $1 | wc -l
