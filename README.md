<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
</head>
<body>
<header>
  <h1>RaspberryPi Face Recognition Door Control</h1>
</header>
<main>
  <section>
    <article>
    <h1>Architecture</h1>
      <h2>General Overview</h2>
      <p>The picture below shows a flowchart of this project's architecture and its elements, such as a camera, a Raspberry Pi 4 and a TV Box</p>
      <figure>
          <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/Fluxogram.png">
        </figure>
      <h2>Understanding the architecture by its elements</h2> 
      <h3>Camera</h3>
       <p>The camera is responsible for all the <Strong>data capturing</Strong>, staying on for as long as we want it. Although it sounds like a waste of energy keeping it on all day, since it is only 12V, powered by a USB cable, in reality the consumption is almost irrelevant.</p>
       <p>In this case the chosen camera was a <strong>Logitech C92S</strong>, but it could be any other one with a good image quality and a USB connection.</p>
      <h3>TV Box</h3>
      <p>A TV Box is a device used mainly to broadcast TV channels on a chosen device, but it in reality is can be used in a lot of other ways, because it's hardware is a <strong>microcontroller</strong> just like an <strong>ESP32, Arduino and the Raspberry itself</strong>, just simpler.</p>
      <p>While it can be used like a normal microcontroller, it is usually not as fast and have less processing capacity, but it does a great job as a server host or database, and that is why it was chosen as a remote file storage, for being sometimes cheaper and also more safe, since we can have it physically</p>
       <h3>Raspberry Pi 4</h3>
      <p>The Raspberry is responsible for everything that involves processing and communication on this system</p>
      <h4>Processing</h4>
      <p>By keeping the camera on all the time, the Raspberry has access to the data almost in real time and can detect faces using the <strong>face-detection</strong> library on the python script, and once it detects it, the <strong>face-recognition</strong> library uses the model examples, stored on the TV Box, to detect a known face and open the gate</p>
      <h4>Communication and control</h4>
      <p>Using the <strong>OpenCV (Open Computer Vision)</strong> library, it is quite easy to have your image processed by a python script, but once it is received, the script establishes a <strong>TCP/IP Communication Protocol</strong> to access the model database by the Router connection, via Wi-fi.</p>
      <p>The simplest part of the project is actually opening the gate, since once a face is detected, all the code does is activate a relay that sends a current and opens it</p>
      <h1>Motivation</h1>
       <p>To contextualize the project, it must be said that the authors are part of a students residence, that not only has a large number of residents, but also a high turnover of people.
      This kind of living, quite common in some cities, is sometimes the cheaper and most accessible for some college students, but it also comes with some disadvantages.</p>
    <p>One of those is that a big part of the house items are shared, such as refrigerator, shelves and home appliances, but also things from the house infrastructure, like the keys and garage remote control.</p>
    <p>Using the keys, although it looks like a simple and efficient choice, will eventually lead to some problems, because some of the man sharing the house will eventually lose their keys (it has happened more than expected), but using face recognition is an option that is also secure, if not more than the keys and with less chance of leading to problems on the long run for us, since the only ones allowed are registered on the faces database.</p>
      <h1>Objectives</h1>
      <p>The main objective of this project is to solve a problem that is currently happening in our lives while applying the knowledge acquired during the graduation in a real project, outside of the university</p>
    </article>
  </section>
</main>
</body>
</html>
