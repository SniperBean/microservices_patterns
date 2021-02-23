<?php

namespace App\GraphQL\Queries;
use App\Http\Helpers\MicroservicesRequest;

class Users
{
    /**
     * @param  null  $_
     * @param  array<string, mixed>  $args
     */
    public function __invoke($_, array $args)
    {
        $ms_res = new MicroservicesRequest(
            config('app.USER_SVC'),
            "/api/users"
        );
        return json_decode($ms_res->getResponse()->getBody());
    }
}
