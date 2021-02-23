<?php

namespace App\Http\Helpers;

use GuzzleHttp\Client;
use GuzzleHttp\Exception\GuzzleException;
use Psr\Http\Message\ResponseInterface;
use \Illuminate\Support\Facades\Log;

class MicroservicesRequest {
    protected string $domain;
    protected string $path;
    protected string $id;
    protected string $protocol;

    public function __construct(string $domain, string $path, string $id=null, string $protocol='http')
    {
        $this->domain = $domain;
        $this->path = $path;
        if ($id)
            $this->id = '/' . $id;
        else
            $this->id = '';
        $this->protocol = $protocol;
    }

    private function getURI (): string {
        return $this->protocol . "://" . $this->domain . $this->path . $this->id;
    }

    public function getResponse ($method='GET'): ResponseInterface {
        $client = new Client();
        try {
            return $client->request($method, $this->getURI());
        } catch (GuzzleException $e) {
            Log::error($e);
        }
    }
}
