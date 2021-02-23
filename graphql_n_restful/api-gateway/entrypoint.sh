#!/bin/bash
service apache2 start
php artisan config:cache
php artisan serve
