<?php

namespace App\GraphQL\Queries;
use App\Http\Helpers\MicroservicesRequest;
class User
{
    /**
     * @param  null  $_
     * @param  array<string, mixed>  $args
     */
    public function __invoke($_, array $args)
    {
        $ms_res = new MicroservicesRequest(
            config('app.USER_SVC'),
            "/api/user",
            $args['id']
        );
        return json_decode($ms_res->getResponse()->getBody());
    }
}
