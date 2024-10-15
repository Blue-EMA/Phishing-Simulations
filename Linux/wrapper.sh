#!/bin/bash
# Define the cron job
cron_job="* * * * * DISPLAY=:0 ~/Phishing-Simulations/auto.sh > ~/Phishing-Simulations/test_log.txt 2>&1"

# Add the cron job if it doesn't already exist
(crontab -l 2>/dev/null | grep -Fxq "$cron_job") || (echo "$cron_job" | crontab -)

echo "Cron job added: $cron_job"
