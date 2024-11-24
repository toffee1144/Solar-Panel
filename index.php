<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Energy Data Dashboard</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script> <!-- jQuery library -->
</head>
<body>

<div id="energyData">
    <!-- Displayed data will be loaded here dynamically -->
</div>

<script>
    // Function to update energy data using AJAX
    function updateEnergyData() {
        $.ajax({
            url: 'get_data.php', // PHP script to fetch data from MySQL
            type: 'GET',
            dataType: 'html',
            success: function(data) {
                $('#energyData').html(data);
            },
            complete: function() {
                // Schedule the next update after 5 seconds
                setTimeout(updateEnergyData, 500);
            }
        });
    }

    // Initial call to start the updates
    updateEnergyData();
</script>

</body>
</html>
