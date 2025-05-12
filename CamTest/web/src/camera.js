async function listCameras() {
    const devices = await navigator.mediaDevices.enumerateDevices();
    return devices.filter(device => device.kind === 'videoinput');
}

async function testCamera(deviceId) {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: { deviceId: { exact: deviceId } }
        });
        const track = stream.getVideoTracks()[0];
        const capabilities = track.getCapabilities();

        // Stop the stream
        track.stop();

        return {
            status: 'Success',
            resolution: `${capabilities.width.max}x${capabilities.height.max}`,
            frameRate: capabilities.frameRate.max
        };
    } catch (err) {
        return { status: `Failed: ${err.message}` };
    }
}

module.exports = { listCameras, testCamera };