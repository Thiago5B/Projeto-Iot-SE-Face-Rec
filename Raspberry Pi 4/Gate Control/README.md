<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>
<header>
  <h1>Gate control</h1>
  <p>Since the gate is already locked by a eletronic device, the control itself is quite easy, the real difficulty is choosing automatically who can enter and who can't.</p>
</header>
<main>
  <section>
    <article>
      <h2>Hardware</h2>
      <p>The list below describes the items involved and their use</p> 
      <li><strong>Camera</strong>: The camera model chosen in this project is a Logitech C92S, because it can record video in HD, altought the image seen by the microcontroller is limited to 480p, 
        so it consumes less processing.</li>
      <li><strong>Microcontroller</strong>: The Raspberry Pi 4 was chosen because it can run a individual OS, making the image capturing and processing easier.<br>
      The project was developed on the 4GB version of the board and using the Debian Linux adapted for Rasp, called Raspbian, as an OS.</li>
      <li><strong>Switch</strong>: The switch used to control the eletronic gate lock was a simples Relay module, JOC-3FF-S-Z.</li>
      <li><strong>Eletronic Lock</strong>: The locked used was the one already installed on our house, C-90 HDL</li>
      <br>
      <p>The picture below shows a simples diagram of the circuit connections</p>
      <figure>
        <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/circuitorelay.png"></img>
      </figure>
      <h2>Software</h2> 
      <p>The raspberry uses three main codes to effectively realize the face recognition and gate control. Each one is briefly described and commented below.</p>
        <h3>Face registering</h3>
        <p>This code is used to register new faces on the database and consequently allowing the people to unlock the gate. The way is works is: It starts the camera with a face detection function and, once is detects a unknown face, clicking the Enter button will save the picture and the persons name (chosen by the user) to the database, by converting the image to bytes and sending it as strings to the TV Box.</p>
       <p>You can check the code <strong><a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Gate%20Control/Cadastro.py">here</a></strong></p>
      <h3>Gatekeeper</h3>
      <p>This code is responsible for openning the gate if a known face is detected by the camera. The camera is started with a face detection function and once it detects, the database is compared and if a match is find, the raspberry opens the gate by activating the relay and stores the timestamp of the entry on the database.</p>
       <p>You can check the code <strong><a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Gate%20Control/Poorteiro.py">here</a></strong></p>
       <h3>Image Extractor</h3>
      <p>This code extracts the last recorded face from the database, allowing the user to confirm if the taken picture satisfies their needs. It connects to the database with the login and password and if a connection is estabilished, checks for the database. If the database is find, the picture is extracted in bytes format to then be reconverted into a picture.</p>
       <p>You can check the code <strong><a href="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/Raspberry%20Pi%204/Gate%20Control/Extrai_img.py">here</a></strong></p>
      </article>
  </section>
</main>
</body>
</html>
