const camera = require('./camera');

async function init() {
    try {
        const cameras = await camera.listCameras();
        console.log('Available cameras:', cameras);

        // Test first camera
        if (cameras.length > 0) {
            const metadata = await camera.testCamera(cameras[0].deviceId);
            console.log('Camera metadata:', metadata);
            // Display in UI (update DOM)
            document.getElementById('results').innerText = JSON.stringify(metadata, null, 2);
        }
    } catch (err) {
        console.error('Error:', err);
    }
}

init();