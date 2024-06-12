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
            CREATE TABLE cadastro (
              id INT AUTO_INCREMENT PRIMARY KEY,
              data_hora DATETIME NOT NULL,
              imagem LONGBLOB NOT NULL,
              encoding TEXT NOT NULL 
            );
          </code>          
        </pre>
      <p>Create a user and give it the necessary permissions</p>
      <pre>
          <code>
            CREATE USER 'seu_usuario'@'%' IDENTIFIED BY 'sua_senha';
            GRANT ALL PRIVILEGES ON acesso_casa.* TO 'seu_usuario'@'%';
            FLUSH PRIVILEGES;
          </code>
        </pre>
      <p>
        Open the settings file for the MariaDB and then change the bind-address, allowing remote accessing.
      </p>
      <pre>
          <code>
            CREATE USER 'seu_usuario'@'%' IDENTIFIED BY 'sua_senha';
            GRANT ALL PRIVILEGES ON acesso_casa.* TO 'seu_usuario'@'%';
            FLUSH PRIVILEGES;
          </code>
        </pre>
      <pre>
          <code>
              bind-address = 0.0.0.0
          </code>
        </pre> 
      <p>
        Restart the MariaDB
      </p>
      <pre>
          <code>
              sudo systemctl restart mariadb
          </code>
        </pre>
      <p>
        Use <strong>ipconfig</strong> on the TV Box and then establish the connection on the Rasp using the following command
      </p>
      <pre>
          <code>
              sudo apt install mysql-client
              mysql -u seu_usuario -p -h IP_da_TVBox
          </code>
        </pre>
      <h2>Raspberry</h2>
      <p>In order to connect to the TV Box and run the python scripts, it is necessary to first create a virtual environment</p>
      <h3>Virtual Environtment</h3>
      <p>To create the virtual environment, use the following codes, that will store the VE data on the <strong>source</strong></p>
      <pre>
          <code>
              python3 -m venv myenv
              source myenv/bin/activate
          </code>
        </pre>
      <p>
        Then, install the required librarys. The used ones are listed below on the example code. <br>
        After that will be possible to import them on the python scripts
      </p>
      <pre>
          <code>
              pip install mysql-connector-python
              pip install opencv-python
              pip install face-recognition
              pip install face-detection
              pip install os-sys
              pip install datetime
              pip install cmake
              sudo apt install build-essential cmake
              sudo apt install libgtk-3-dev
              sudo apt install libboost-all-dev
              pip install dlib
          </code>
        </pre>
      <h3>Running the status_rasp.py in a loop</h3>
      <p>
        In order to have the Rasp status updated constantlly, it is necessary to change the <a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Database/status_rasp.py">status_rasp.py</a> location to a special Rasp folder, that runs the scripts inside it every defined interval
      </p>
      <p>First, create the <strong>run_script.sh</strong></p>
       <pre>
          <code>
              #!/bin/bash
              # Caminho para o seu ambiente virtual
              VENV_PATH="/home/pi/myenv"
              <br>
              # Ativa o ambiente virtual
              source "$VENV_PATH/bin/activate"
              <br>
              # Executa o script Python
              python3 /home/pi/scripts/seu_script.py
              <br>
              # Desativa o ambiente virtual
              deactivate
          </code>
        </pre>
      <p>Give execution permission to the script</p>
      <pre>
          <code>
              chmod +x /home/pi/scripts/run_script.sh
          </code>
        </pre>
      <p>Edit the crontab</p>
      <pre>
          <code>
              crontab -e
          </code>
        </pre>
      <p>Add the following line to the script</p>
      <pre>
          <code>
              */5 * * * * /home/pi/scripts/run_script.sh
          </code>
        </pre>
      <h3>Grafana</h3>
      <p>To establish the connection between the Grafana and the Microcontroller, it is necessáry to configure it</p>
      <p>First, add the Grafana repository</p>
      <pre>
          <code>
              echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
          </code>
        </pre>
      <p>Install the require packages</p>
      <pre>
          <code>
              wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
          </code>
        </pre>
      <p>Then, add the GPG key from Grafana</p>
      <pre>
          <code>
              sudo apt-get update
              sudo apt-get install grafana
          </code>
        </pre>
      <p>Lastly, start the Grafana service and configure it to run it on initialization</p>
      <pre>
          <code>
              sudo systemctl start grafana-server
              sudo systemctl enable grafana-server
          </code>
        </pre>
      <h2>Grafana</h2>
      <p>Now, to configure the Granafa itself, to estabilish the connection, follow the steps:</p>
      <ol>
        <li>Log into Grafana and go to <strong>Configuration > Data Sources</strong></li>
        <li>Then, click on <strong>Add data source</strong> and select <strong>MySQL</strong></li>
        <li>Configure the connection:
          <ul>
          <li><strong>Host: </strong>IPV4:Port (insert your IPV4 and Port)</li>
          <li><strong>Database: </strong>your_database_name</li>
          <li><strong>User: </strong>your_user</li>
          <li><strong>Password: </strong>your_password</li>
          </ul>
        </li>
        <li>Click on <strong>Save & Test</strong> and check if the connection is working</li>
      </ol>
    </article>
  </section>
</main>
</body>
</html>
