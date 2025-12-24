function copyToken() {
    const tokenText = document.getElementById("jwt-token").innerText;
    navigator.clipboard.writeText(tokenText)
        .then(() => alert("JWT copied to clipboard"))
        .catch(() => alert("Failed to copy JWT"));
}
