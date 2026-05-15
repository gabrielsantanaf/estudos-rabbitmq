import pika

connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="admin",
        password="admin123"
    )
)
channel = pika.BlockingConnection(connection_parameters).channel()

channel.basic_publish(
    exchange="data_exchenge",
    routing_key="",
    body="Alguma coisa",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)