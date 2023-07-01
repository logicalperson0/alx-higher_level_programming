#!/bin/bash
# sends request to URL, displays size of the body
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
