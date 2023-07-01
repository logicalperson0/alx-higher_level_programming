#!/bin/bash
# sends a POST request to passed URL and display response with the data passed in as arg
curl -s POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD"
