<?php

namespace App\GraphQL\Queries;

class Hello
{
    public function __invoke(): string
    {
        return 'world!';
    }
}
