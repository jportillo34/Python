#!/bin/bash

log_file=$1

if [ -e $log_file ]; then
    `python errors_users_reports.py $log_file`
else
    echo "Log file does not exist!"
fi