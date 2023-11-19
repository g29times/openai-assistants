// app.js

$(document).ready(function() {
    // Add event listeners for arrow key presses to handle user moves
    $(document).keydown(function(e) {
        if (e.key === 'ArrowUp' || e.key === 'ArrowDown' || e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            e.preventDefault();  // Prevent default scrolling behavior for arrow keys
            const direction = e.key.replace('Arrow', '').toLowerCase();
            // Send an AJAX request to the backend to handle the move
            $.ajax({
                type: 'GET',
                url: `/move/${direction}`,
                success: function(data) {
                    // Update the game grid with the data received from the backend
                    updateGameGrid(data);
                }
            });
        }
    });

    // Function to update the game grid based on the data received from the backend
    function updateGameGrid(data) {
        // Update the frontend game grid based on the data received
        // TODO: Implement the logic to update the grid based on the received data
    }
});