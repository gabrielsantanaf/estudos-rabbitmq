# Curso RabbitMQ com Python

Projeto de estudo de mensageria com RabbitMQ usando a biblioteca `pika` em Python. Aborda tanto a abordagem procedural (raw) quanto a orientada a objetos.

## Pré-requisitos

- [Docker](https://www.docker.com/) e Docker Compose
- Python 3.8+

## Instalação

```bash
pip install pika
```

## Subindo o RabbitMQ

O RabbitMQ roda via Docker Compose. Execute na raiz do projeto:

```bash
docker compose up -d
```

Aguarde o container ficar saudável e acesse o painel de gerenciamento em:

```
http://localhost:15672
```

> Credenciais: **admin** / **admin123**

## Estrutura dos arquivos

| Arquivo | Descrição |
|---|---|
| `publisher_raw.py` | Publisher procedural (sem classes) |
| `publisher.py` | Publisher orientado a objetos (`RabbitmqPublisher`) |
| `consumer_raw.py` | Consumer procedural (sem classes) |
| `consumer.py` | Consumer orientado a objetos (`RabbitmqConsumer`) |
| `docker-compose.yml` | Configuração do RabbitMQ |

## Configuração no RabbitMQ (passo obrigatório)

Antes de rodar os scripts, crie a exchange e a fila pelo painel:

1. Acesse **Exchanges** > **Add a new exchange**
   - Name: `data_exchenge`
   - Type: `fanout`
   - Durability: `Durable`

2. Acesse **Queues** > **Add a new queue**
   - Name: `data_queue`
   - Durability: `Durable`

3. Acesse a exchange `data_exchenge` > **Bindings** > vincule à fila `data_queue`

## Rodando os exemplos

### Versão procedural (raw)

Em um terminal, inicie o consumer:

```bash
python consumer_raw.py
```

Em outro terminal, dispare o publisher:

```bash
python publisher_raw.py
```

### Versão orientada a objetos

Em um terminal, inicie o consumer:

```bash
python consumer.py
```

Em outro terminal, dispare o publisher:

```bash
python publisher.py
```

O consumer imprimirá no terminal a mensagem recebida assim que o publisher publicar.

## Parando o RabbitMQ

```bash
docker compose down
```

Para remover também os volumes (apaga filas e dados persistidos):

```bash
docker compose down -v
```
