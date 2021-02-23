<?php

namespace App\GraphQL\Queries;
use App\Http\Helpers\MicroservicesRequest;

class Orders
{
    /**
     * @param  null  $_
     * @param  array<string, mixed>  $args
     */
    public function __invoke($_, array $args)
    {
        $ms_res = new MicroservicesRequest(
            config('app.ORDER_SVC'),
            "/api/orders"
        );
        return json_decode($ms_res->getResponse()->getBody());
    }
}
