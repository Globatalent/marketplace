#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A marketplace.taskapp worker -l INFO
