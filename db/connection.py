def connect_to_db():
    import psycopg2
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="flowcast",
        user="postgres",
        password="1234"
    )
