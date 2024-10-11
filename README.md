## Описание
Сервис для решения задачи по нахождению pow. Подходит как для lesta, так и для wargaming. <br>
По умолчанию, поднимается по адресу http://127.0.0.1:5000/solve

## Запуск
docker-compose up -d

## Пример
```php
use GuzzleHttp\Client;

const SOLVER_URL = 'http://127.0.0.1:5000/solve';

function getNonce($pow): int
{
    $client = new Client();
    $response = $client->post(self::SOLVER_URL, [
        'headers' => [
            'Content-Type' => 'application/json',
            'Accept' => 'application/json',
        ],
        'json' => [
            'algorithm' => [
                'extension' => '',
                'name' => 'hashcash',
                'resourse' => 'wgni',
                'version' => 1,
            ],
            'complexity' => 3,
            'random_string' => $pow['random_string'],
            'timestamp' => $pow['timestamp'],
            'type' => 'pow',
        ]
    ]);

    if ($response->getStatusCode() !== 200) {
        throw new Exception($response->getReasonPhrase());
    }

    $body = $response->getBody()->getContents();
    $result = json_decode($body, true);

    return $result['nonce'];
}
```

