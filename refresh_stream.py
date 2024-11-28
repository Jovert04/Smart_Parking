<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Continuous Live Feed</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: black;
            color: white;
        }
        h1 {
            font-size: 2em;
        }
        #liveFeed {
            max-width: 100%;
            max-height: 90vh;
            border: 5px solid white;
        }
        #loading {
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <h1>Continuous Live Feed</h1>
    <p id="loading">Channel 1</p>
    <!-- Image or Video that refreshes -->
    <img id="liveFeed" src="http://192.168.1.10/capture?_cb=" alt="Live Feed" />
    
    <script>
        // Function to refresh the live feed image
        function refreshPage() {
            const timestamp = new Date().getTime(); // Get current timestamp for cache-busting
            const imageUrl = "http://192.168.1.10/capture?_cb=" + timestamp;
            document.getElementById("liveFeed").src = imageUrl; // Update image source
        }

        // Set the refresh interval to 500 ms (2 updates per second)
        setInterval(refreshPage, 500); // 500 ms = 2 updates per second
    </script>
</body>
</html>