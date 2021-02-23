<?php

namespace App\GraphQL\Queries;
use App\Http\Helpers\MicroservicesRequest;

class Item
{
    /**
     * @param  null  $_
     * @param  array<string, mixed>  $args
     */
    public function __invoke($_, array $args)
    {
        $ms_res = new MicroservicesRequest(
            config('app.ITEM_SVC'),
            "/api/item",
            $args['item_id']
        );
        return json_decode($ms_res->getResponse()->getBody());
    }
}
