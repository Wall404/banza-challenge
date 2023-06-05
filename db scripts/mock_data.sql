-- Inserción de datos ficticios en la tabla "clientes"
INSERT INTO clientes (nombre) VALUES
    ('Cliente 1'),
    ('Cliente 2'),
    ('Cliente 3');

-- Inserción de datos ficticios en la tabla "cuentas"
INSERT INTO cuentas (nombre, cliente_id) VALUES
    ('Cuenta 1', 1),
    ('Cuenta 2', 1),
    ('Cuenta 3', 2),
    ('Cuenta 4', 3);

-- Inserción de datos ficticios en la tabla "movimientos"
INSERT INTO movimientos (id_cuenta, nombre, tipo, importe, fecha) VALUES
    (1, 'Movimiento 1', 'ingreso', 100.00, '2023-06-01 10:00:00'),
    (1, 'Movimiento 2', 'egreso', 50.00, '2023-06-02 15:30:00'),
    (2, 'Movimiento 3', 'ingreso', 200.00, '2023-06-03 09:45:00'),
    (2, 'Movimiento 4', 'egreso', 75.00, '2023-06-04 14:15:00');

-- Inserción de datos ficticios en la tabla "categorias"
INSERT INTO categorias (nombre) VALUES
    ('Categoria 1'),
    ('Categoria 2'),
    ('Categoria 3');

-- Inserción de datos ficticios en la tabla intermedia "cliente_categoria"
INSERT INTO cliente_categoria (cliente_id, categoria_id) VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 1),
    (3, 3);

-- Fin del script SQL
