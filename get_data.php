<?php
// MySQL configuration
$host = '127.0.0.1';
$user = 'root';
$password = '1234';
$database = 'SolarPanel';

// Create a connection to the database
$conn = new mysqli($host, $user, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve data from the database
$sql = "SELECT * FROM energy_data ORDER BY timestamp DESC LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    ?>
    <h1>Energy Data</h1>
    <p>Input Voltage: <?php echo $row['input_voltage']; ?> V</p>
    <p>Vout: <?php echo $row['vout']; ?> V</p>
    <p>Current: <?php echo $row['current']; ?> A</p>
    <p>Instantaneous Power: <?php echo $row['power']; ?> W</p>
    <p>Total Energy: <?php echo $row['total_energy']; ?> Wh</p>
    <p>Total Price: Rp. <?php echo $row['total_price']; ?></p>
    <p>Elapsed Time: <?php echo $row['elapsed_time_hours'] . ' hours, ' . $row['elapsed_time_minutes'] . ' minutes, ' . $row['elapsed_time_seconds'] . ' seconds'; ?></p>
    <?php
} else {
    echo "No data available.";
}

// Close the connection
$conn->close();
?>
