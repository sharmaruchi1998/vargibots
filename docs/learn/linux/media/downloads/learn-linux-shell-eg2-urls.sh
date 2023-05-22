#!/bin/bash

# Store URLs in two variables
URL1="https://www.e-yantra.org/"
URL2="http://www.iitb.ac.in/"

# Print some message
echo "** Opening $URL1 and $URL2 in Firefox **"

# Use firefox to open the two URLs in separate windows
firefox -new-window $URL1 $URL2