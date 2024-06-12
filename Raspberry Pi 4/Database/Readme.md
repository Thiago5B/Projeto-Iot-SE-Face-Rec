<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<header>
  <h1>Database</h1>
  <p>Since the gate is already locked by a eletronic device, the control itself is quite easy, the real difficulty is choosing automatically who can enter and who can't.</p>
</header>
<main>
  <section>
    <article>
      <h2>Hardware</h2>
      <p>In this case, the only hardware is the TV Box. It is used to stream open and subscription-based TV channels available on the internet, but in reality it can do much more, because its hardware is basically a microcontroller, just like ESP32, Arduino and Raspberries. Knowing that, it is possible to install any desired OS, like a Linux for example, and use it in many ways: as a server host, a database or even a smart home hub. The used TV Box model is BTV E10.</p>
      <br>
      <p>The picture below shows a simple diagram of the circuit connections</p>
      <figure>
        <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/tvbox.png" width="300" 
     height="175"></img>
      </figure>
      <h2>Software</h2> 
      <p>The raspberry only one script, but some integrations with other softwares, described below.</p>
        <h3>Raspberry Status</h3>
        <p>This code is used by the Rasp to record, send and store some status, as cpu temperature, processing used and disk used into the TV Box</p>
       <p>You can check the code <strong><a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Database/status_rasp.py">here</a></strong></p>
        <h3>Database</h3>
      <p>To store the user's data, it was necessary to choose a database service to our linux-based TV Box. There were three main options, but they had some differences:</p>
      <ol> 
        <li><strong>MongoDB:</strong> The MongoDB is a x64-based database, and since the TV Box uses a x32 system, it is not compatbile</li> 
        <li><strong>InfluxDB:</strong> Found few references on the internet help with using and installation problems</li> 
        <li><strong>MariaDB:</strong> Has a simple step-by-step installation and easy integration</li>
        <br>
        <p>That's why the MariaDB was chosen as our Database, since it was the best fitting option for US</p>
        <p>You can access the MariaDB site on the picture below</p>
        <figure>
          <a href="https://mariadb.org/"><img src="https://d1.awsstatic.com/logos/partners/MariaDB_Logo.d8a208f0a889a8f0f0551b8391a065ea79c54f3a.png"></a>
        </figure>
      </ol> 
      <p>The MariaDB allows the creation of a mySQL-based database and accessing it remotely by TCP/IP. It also has a user system, allowing specific accounts to access specific databases.
        The Grafana Dashoboard integration also requires the user account to establish a bridge</p>
      <h3>Dashboard</h3> 
      <p>In order to keep a performance monitoring of the system running, our option was to store the data collected from the <strong>status_rasp.py</strong> on the TV Box and, for better visualization, show the values and their timestamp as a line plot on the <strong>Grafana Dashboard</a></strong>. You can access the Grafana home page by clicking on the image below.</p>
      <figure>
          <a href="https://grafana.com/grafana/dashboards/"><img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/grafana-removebg-preview.png"
          width="350" height="350"></a>
        </figure>
      <p>It was choosen because of its simple integration and application, since it is a well-known Dashboard and has some pre-configured integration with many apps, while being free-of-charge</p>
    <h3>Used ports</h3>
      <p>In order to establish TCP/IP connections, it its necessary to use one port for each connection</p>
        <li><strong>Port 3000:</strong> Grafana</li> 
        <li><strong>Port 3306:</strong> MariaDB</li> 
      <h2>How is it done</h2>  
      <p>You can check the step-by-step description of the system, with the required commands 
      <strong><a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Database/Step-by-step-installation.md">here</a></strong></p></p>
    </article>
  </section>
</main>
</body>
</html>
