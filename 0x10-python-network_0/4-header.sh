#!/bin/bash
# sends a GET request and gets response with header variable
curl -s GET $1 -H "X-School-User-Id: 98"
