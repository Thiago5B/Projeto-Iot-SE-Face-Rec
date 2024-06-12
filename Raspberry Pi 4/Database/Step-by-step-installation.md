<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<header>
  <h1>Step-by-step Installation</h1>
  <p>Here you can find instructions on how our database was created and use it to create your own. In order to use the MariaDB on our headless linux application, it was necessary to run some codes, that you can find below commented and described</p>
</header>
<main>
  <section>
    <article>
      <h2>MariaDB</h2>
      <p><strong>It is important to note that the MariaDB isn't the database, it is a compiler for mySQL, just like DevC++ is a compiler for C/C++</strong></p>
      <p>First, it is necessary to update the package list and then install the MariaDB</p>
        <pre>
          <code>
            sudo apt update #updates the package list
            sudo apt install mariadb-server #install the MariaDB server
          </code>
        </pre>
      <p>Then, configure the inicial security, following the instructions</p>
        <pre>
          <code>
            sudo mysql_secure_installation
          </code>
        </pre>
     <p>Then, access the MariaDB as root and create the desired tables and databases</p>
        <pre>
          <code>
            sudo mysql -u root -p
            <br>
            CREATE DATABASE acesso_casa;
            USE acesso_casa;
            CREATE TABLE registros (
              id INT AUTO_INCREMENT PRIMARY KEY,
              data_hora DATETIME NOT NULL,
              imagem_path VARCHAR(255) NOT NULL
            );
          </code>
        </pre>
    </article>
  </section>
</main>
</body>
</html>
