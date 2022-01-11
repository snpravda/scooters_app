package com.example.mapwithmarker

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.mapwithmarker.R

class MainActivity : AppCompatActivity() {
    private lateinit var getScooterButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        getScooterButton = findViewById(R.id.get_scooters_btn)

        getScooterButton.setOnClickListener {
            this.getScooters()
        }
    }

    private fun getScooters () {
        startActivity(Intent(this, MapsMarkerActivity::class.java))
    }
}