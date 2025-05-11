package com.example.camtest

import android.Manifest
import android.content.pm.PackageManager
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import android.hardware.camera2.CameraManager

class MainActivity : AppCompatActivity() {
    private val CAMERA_PERMISSION_CODE = 100

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val resultText = findViewById<TextView>(R.id.result_text)

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
            != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,
                arrayOf(Manifest.permission.CAMERA), CAMERA_PERMISSION_CODE)
        } else {
            testCamera(resultText)
        }
    }

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == CAMERA_PERMISSION_CODE && grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            testCamera(findViewById(R.id.result_text))
        } else {
            findViewById<TextView>(R.id.result_text).text = "Camera permission denied"
        }
    }

    private fun testCamera(resultText: TextView) {
        val cameraManager = getSystemService(CAMERA_SERVICE) as CameraManager
        val cameraIds = cameraManager.cameraIdList
        val result = StringBuilder("Available cameras:\n")
        for (id in cameraIds) {
            val characteristics = cameraManager.getCameraCharacteristics(id)
            val resolution = characteristics.get(android.hardware.camera2.CameraCharacteristics.SENSOR_INFO_PIXEL_ARRAY_SIZE)
            result.append("Camera $id: Resolution $resolution\n")
        }
        resultText.text = result.toString()
    }
}