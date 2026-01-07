FROM aplet123/php-nginx:php7-nginx1.10

COPY app /var/www
RUN mkdir -p /var/www/memories
RUN chmod 770 /var/www/memories
RUN chgrp www-data /var/www/memories

# Create a script to write the flag from environment variable
COPY flag_writer.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/flag_writer.sh

EXPOSE 80

COPY cleardir.cron /etc/cron.d/cleardir
RUN chmod 0644 /etc/cron.d/cleardir
RUN crontab /etc/cron.d/cleardir

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# Set default flag value (placeholder)
ENV FLAG="FLAG_PLACEHOLDER"

# Use flag_writer script to create flag.txt and then start the service
CMD ["/bin/bash", "-c", "/usr/local/bin/flag_writer.sh && service nginx start && service php7.0-fpm start && service cron start && tail -f /var/log/nginx/access.log"]
