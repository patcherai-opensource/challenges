FROM php:7.2-apache
RUN docker-php-ext-install mysqli
COPY source/ /var/www/
COPY source/public/ /var/www/html/
