document.addEventListener('DOMContentLoaded', function() {
    var getFileButton = document.getElementById('getFile');
    var fileInput = document.querySelector('input[type="file"]');
    var submitButton = document.getElementById('submitBtn');
    var fileNameDisplay = document.getElementById('fileName');

    getFileButton.addEventListener('click', function() {
        fileInput.click(); // Trigger the file input
    });

    fileInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            document.getElementById("getFile").style.display = "none"
            fileNameDisplay.textContent = this.files[0].name; // Display the file name
            submitButton.classList.remove('hidden'); // Show the 'Submit' button
        }
    });

    submitButton.addEventListener('click', function() {
        // Implement the action to take upon file submission
        // Likely you will want to submit the form here
        // Note: The form will automatically be submitted because this button is of type 'submit'
    });
});
