<?php

namespace App\GraphQL\Queries;
use GuzzleHttp\Client;
use App\Http\Helpers\MicroservicesRequest;
use App\Http\Helpers\TestClass;

class Items
{
    /**
     * @param  null  $_
     * @param  array<string, mixed>  $args
     */
    public function __invoke($_, array $args)
    {
        $ms_res = new MicroservicesRequest(
            config('app.ITEM_SVC'),
            "/api/items"
        );
        return json_decode($ms_res->getResponse()->getBody());
    }
}
