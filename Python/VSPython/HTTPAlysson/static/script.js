function initializeFileInput() {
    const fileInput = document.getElementById("file-input");
    const fileLabel = document.getElementById("file-label");

    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            fileLabel.textContent = fileInput.files[0].name;
        } else {
            fileLabel.textContent = "Selecione ou arraste um arquivo";
        }
    });
}
