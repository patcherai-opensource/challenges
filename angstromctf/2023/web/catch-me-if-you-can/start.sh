#!/bin/sh

# Set default flag if not provided
FLAG=${FLAG:-"actf{placeholder_flag}"}

# Substitute the flag placeholder in the HTML template
sed "s/FLAG_PLACEHOLDER/$FLAG/g" /usr/share/nginx/html/index.html.template > /usr/share/nginx/html/index.html

# Start nginx
exec nginx -g "daemon off;"