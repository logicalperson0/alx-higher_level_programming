#!/bin/bash
# Displays all HTTP methods the server will accept
curl -sI ALLOW $1 | grep "ALLOw" | cut -d " " -f2
