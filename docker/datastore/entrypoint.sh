#!/bin/sh

set -e

if [[ -z "${DATASTORE_PROJECT_ID}" ]]; then
    echo "Missing DATASTORE_PROJECT_ID environment variable" >&2
    exit 1
fi

# Configure project
gcloud config set project ${DATASTORE_PROJECT_ID}

# Start emulator
gcloud beta emulators datastore start \
    --host-port=0.0.0.0:8001 \
    --quiet \
    --consistency=1.0 \
    --data-dir /data
