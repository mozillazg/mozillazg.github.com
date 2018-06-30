#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

git add .
git commit -am "new posts"
git push
