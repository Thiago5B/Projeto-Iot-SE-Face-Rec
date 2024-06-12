<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grafana Dashboard Description</title>
</head>
<body>
  <h1>Grafana Dashboard Description</h1>
  <p>This Grafana dashboard displays data from two tables: <strong>Controle de Acesso</strong> and <strong>Registro por cadastro</strong>.</p>
  <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/graf_4.jpg">
  <h2>Table: Controle de Acesso</h2>
  <p>The <strong>Controle de Acesso</strong> table contains records of all entries made by users. Each entry includes the following information:</p>
  <ul>
    <li><strong>Acesso em:</strong> Date and time of the entry.</li>
    <li><strong>Usuário:</strong> Name of the user who made the entry.</li>
  </ul>
  <p>This table is used to track all user entries.</p>
  <h2>Table: Registro por cadastro</h2>
  <p>The <strong>Registro por cadastro</strong> table stores the latest entry made by each user. It contains the following columns:</p>
  <ul>
    <li><strong>Usuário:</strong> Name of the user.</li>
    <li><strong>Último acesso:</strong> Date and time of the user's last entry.</li>
  </ul>
  <p>This table is useful for quickly identifying the most recent entry made by each user.</p>
  <h2>SQL Queries for Grafana:</h2>
  <h3>First Query:</h3>
  <pre><code>SELECT name AS "Usuário", DATE_FORMAT(data_hora, '%Y-%m-%d %H:%i:%s') AS "Acesso em"
FROM entradas
ORDER BY data_hora DESC
LIMIT 30;</code></pre>
  <h3>Second Query:</h3>
  <pre><code>SELECT name AS "Usuário", MAX(DATE_FORMAT(data_hora, '%Y-%m-%d %H:%i:%s')) AS "Último Acesso"
FROM entradas
GROUP BY name
ORDER BY "Último Acesso" DESC;</code></pre>
</body>
</html>
