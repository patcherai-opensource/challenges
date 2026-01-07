#!/bin/bash

# Write the flag from environment variable to /flag.txt
echo "${FLAG}" > /flag.txt
chgrp www-data /flag.txt
chmod 644 /flag.txt
