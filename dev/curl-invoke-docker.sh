#!/bin/bash

set -e

execution_mode=$1
mock_io=true
port=4000
results_url=/workflow/results  # must be consistent with volume mount set in docker-run.sh
params=$(yq -c '."month-grouper".params' test-cases.yaml)

max_attempts=10
attempt=1
wait_seconds=2
while [ $attempt -le $max_attempts ]; do
    echo "Health check; attempt $attempt of $max_attempts..."

    curl -sf -o /dev/null -S http://localhost:${port}/docs && break

    echo "Service not ready. Waiting $wait_seconds seconds before next attempt..."
    sleep $wait_seconds

    ((attempt++))
done
echo "Service ready!"

curl --fail-with-body \
-X POST "http://localhost:${port}/?execution_mode=${execution_mode}&mock_io=${mock_io}&results_url=${results_url}" \
-H "Content-Type: application/json" \
-d '{"params": '"${params}"'}'
