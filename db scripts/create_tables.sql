CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE cuentas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE movimientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cuenta INT,
    nombre VARCHAR(255),
    tipo ENUM('ingreso', 'egreso'),
    importe DECIMAL(10, 2),
    fecha DATETIME,
    FOREIGN KEY (id_cuenta) REFERENCES cuentas(id)
);

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255)
);

CREATE TABLE cliente_categoria (
    cliente_id INT,
    categoria_id INT,
    PRIMARY KEY (cliente_id, categoria_id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
