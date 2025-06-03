document.addEventListener('DOMContentLoaded', () => {

    // Hello message 
    fetch('http://localhost:5000/api/hello')
    .then(res => res.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(() => {
        document.getElementById('message').innerText = "Error loading message.";
    });

    // Log button 
    const logButton = document.getElementById('logButton');

    if (logButton) {
        logButton.addEventListener('click', () => {
            const logMessage = {message: 'User clicked the log button'};

            fetch('http://localhost:5000/api/log-button', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(logMessage)
            })
            .then(res => res.json())
            .then(data => console.log("Log successful",  data))
            .catch(err => console.error("Log failed", err))
        })
    }
    })


fetch('http://localhost:5000/api/health')
    .then(res => res.json())
    .then(data => console.log("Backend status", data.status))
    .catch(err => console.error("Health check failed", err))

