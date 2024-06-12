<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Raspberry Pi Monitoring Dashboard</h1>
        <img src="https://github.com/Thiago5B/RaspberryPi-FaceRecognition-Door-Control/blob/main/img/graf_1.jpg">
    <!-- Chart 1 = TOP LEFT -->
    <h2>Chart 1: CPU Temperature Over Time</h2>
    <h3>Description</h3>
    <p>
        This chart shows the CPU temperature of the Raspberry Pi over time. It is useful for monitoring how the temperature varies during different periods of the day.
    </p>
    <h3>SQL Query</h3>
    <pre><code>
SELECT
  UNIX_TIMESTAMP(timestamp) as time_sec,
  cpu_temperature as value
FROM
  raspberry_data
WHERE
  device = 'chrispi' AND $__timeFilter(timestamp)
ORDER BY
  timestamp
    </code></pre>
    <h3>Interpretation</h3>
    <ul>
        <li><strong>X-axis (time_sec)</strong>: Represents the time in seconds since the Unix epoch.</li>
        <li><strong>Y-axis (value)</strong>: Represents the CPU temperature in degrees Celsius.</li>
    </ul>
    <!-- Chart 2 = BOTTON LEFT-->
    <h2>Chart 2: CPU Temperature Over Time (Copy)</h2>
    <h3>Description</h3>
    <p>
        This chart is a copy of the first one and shows the CPU temperature of the Raspberry Pi over time again.
    </p>
    <h3>SQL Query</h3>
    <pre><code>
SELECT
  UNIX_TIMESTAMP(timestamp) as time_sec,
  cpu_temperature as value
FROM
  raspberry_data
WHERE
  device = 'chrispi' AND $__timeFilter(timestamp)
ORDER BY
  timestamp
    </code></pre>
    <h3>Interpretation</h3>
    <ul>
        <li><strong>X-axis (time_sec)</strong>: Represents the time in seconds since the Unix epoch.</li>
        <li><strong>Y-axis (value)</strong>: Represents the CPU temperature in degrees Celsius.</li>
    </ul>
    <!-- Chart 3 = TOP RIGHT-->
    <h2>Chart 3: CPU Temperature Over Time (Copy)</h2>
    <h3>Description</h3>
    <p>
        This chart is a copy of the first two and shows the CPU temperature of the Raspberry Pi over time again.
    </p>
    <h3>SQL Query</h3>
    <pre><code>
SELECT
  UNIX_TIMESTAMP(timestamp) as time_sec,
  cpu_temperature as value
FROM
  raspberry_data
WHERE
  device = 'chrispi' AND $__timeFilter(timestamp)
ORDER BY
  timestamp
    </code></pre>
    <h3>Interpretation</h3>
    <ul>
        <li><strong>X-axis (time_sec)</strong>: Represents the time in seconds since the Unix epoch.</li>
        <li><strong>Y-axis (value)</strong>: Represents the CPU temperature in degrees Celsius.</li>
    </ul>
  <!-- Chart 4 = BOTTON RIGHT-->
    <h2>Chart 4: CPU Temperature Over Time (Copy)</h2>
    <h3>Description</h3>
    <p>
        This chart is a copy of the first three and shows the CPU temperature of the Raspberry Pi over time again.
    </p>
    <h3>SQL Query</h3>
    <pre><code>
SELECT
  UNIX_TIMESTAMP(timestamp) as time_sec,
  cpu_temperature as value
FROM
  raspberry_data
WHERE
  device = 'chrispi' AND $__timeFilter(timestamp)
ORDER BY
  timestamp
    </code></pre>
    <h3>Interpretation</h3>
    <ul>
        <li><strong>X-axis (time_sec)</strong>: Represents the time in seconds since the Unix epoch.</li>
        <li><strong>Y-axis (value)</strong>: Represents the CPU temperature in degrees Celsius.</li>
    </ul>
</body>
</html>

