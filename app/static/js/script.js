document.getElementById('getFile').addEventListener('click', function() {
    document.getElementById('fileInput').click(); // Trigger the file input
});

document.getElementById('fileInput').addEventListener('change', function() {
    if (this.files.length > 0) {
        const fileNameDisplay = document.getElementById('fileName');
        fileNameDisplay.textContent = this.files[0].name; // Display the file name
        fileNameDisplay.classList.add('file-name'); // Add class for styling (optional)
        this.classList.add('hidden'); // Hide the file input
        document.getElementById('submitBtn').classList.remove('hidden'); // Show the 'Submit' button
    }
});

document.getElementById('submitBtn').addEventListener('click', function() {
    // Implement the action to take upon file submission
    // Likely you will want to submit the form here
});