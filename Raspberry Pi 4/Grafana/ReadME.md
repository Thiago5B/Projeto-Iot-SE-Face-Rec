<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Setting up a Dashboard in Grafana with MariaDB</h1>
  <ol>
    <li><strong>Login to Grafana:</strong> Open your web browser and navigate to your Grafana instance.</li>
    <li><strong>Enter Database Credentials:</strong> Before adding a new panel or dashboard, navigate to "Settings" > "Data Sources". Select your MariaDB data source, and enter the database credentials (username, password, host, etc.) in the appropriate fields.</li>
          <br><img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/graf_2.jpg">
        <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/graf_3.jpg">
    <br>
    <li><strong>Create a new Dashboard:</strong> Click on the "add" icon on the left sidebar and select "Dashboard".</li>
    <li><strong>Add a Panel:</strong> Click on "Add new panel" to start adding panels to your dashboard.</li>
    <li><strong>Choose Visualization:</strong> Select the visualization type you want to use for your first panel (e.g., Graph, Singlestat, Table, etc.).</li>
    <li><strong>Configure Data Source:</strong> In the panel settings, under the "Query" tab, select your data source. Since you've already configured MariaDB as a data source, it should appear in the list.</li>
    <li><strong>Write SQL Query:</strong> Write your SQL query to retrieve data from the MariaDB database. You can directly enter your SQL query in the query editor provided by Grafana.</li>
    <li><strong>Save the Dashboard:</strong> Once you've configured your first panel with the desired visualization and data source, click on "Save dashboard" to save your changes.</li>
    <li><strong>Add More Panels:</strong> Repeat steps 4 to 7 to add more panels to your dashboard as needed.</li>
    <li><strong>Customize Dashboard:</strong> You can customize your dashboard further by adding additional panels, adjusting panel settings, applying filters, etc.</li>
    <li><strong>Monitor and Analyze Data:</strong> Your Grafana dashboard is now ready to monitor and analyze data from your MariaDB database.</li>
  </ol>
</body>
</html>
