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
        <img src="https://www.duosat.tv/media/catalog/product/cache/23/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/b/t/btv_e10.png" width="400" 
     height="350"></img>
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
