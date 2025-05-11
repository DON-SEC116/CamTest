import UIKit
import AVFoundation

class ViewController: UIViewController {
    @IBOutlet weak var resultLabel: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()
        checkCameraPermission()
    }

    func checkCameraPermission() {
        switch AVCaptureDevice.authorizationStatus(for: .video) {
        case .authorized:
            testCamera()
        case .notDetermined:
            AVCaptureDevice.requestAccess(for: .video) { granted in
                DispatchQueue.main.async {
                    if granted {
                        self.testCamera()
                    } else {
                        self.resultLabel.text = "Camera permission denied"
                    }
                }
            }
        default:
            resultLabel.text = "Camera permission denied"
        }
    }

    func testCamera() {
        let devices = AVCaptureDevice.devices(for: .video)
        var result = "Available cameras:\n"
        for device in devices {
            result += "Camera: \(device.localizedName)\n"
        }
        resultLabel.text = result
    }
}