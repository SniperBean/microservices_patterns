FROM php:7.4.15-apache

RUN apt-get update && apt-get install -y libmcrypt-dev \
    libmagickwand-dev --no-install-recommends \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY ./conf/laravel.conf /etc/apache2/sites-enabled/000-default.conf

COPY ./laravel /var/www/laravel

COPY /entrypoint.sh /entrypoint.sh

RUN chown -R www-data.www-data /var/www/laravel \
    && chmod -R 755 /var/www/laravel \
    && chmod -R 755 /var/www/laravel/storage \
    && chmod 755 /entrypoint.sh

WORKDIR /var/www/laravel

RUN cp .env.example .env

RUN php artisan route:clear \
    && php artisan key:generate \ 
    && composer install

RUN a2enmod ssl &&  a2enmod proxy && a2enmod proxy_balancer && a2enmod proxy_http

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
