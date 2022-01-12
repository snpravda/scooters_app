package com.example.mapwithmarker

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import com.github.kittinunf.fuel.coroutines.awaitStringResponse
import com.github.kittinunf.fuel.httpGet
import kotlinx.coroutines.runBlocking
import org.json.JSONObject

class ScooterDetail : AppCompatActivity() {

    companion object {
        const val SCOOTER_ID = "id"
    }

    private lateinit var title : TextView
    private lateinit var scooterInfo : TextView
    private lateinit var rentButton  : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_scooter_detail)

        title = findViewById(R.id.title)
        scooterInfo = findViewById(R.id.scooterInfo)
        rentButton = findViewById(R.id.rentButton)

        this.getScooterDetail()

        rentButton.setOnClickListener {
            Toast.makeText(this, "You don't have enough money on your balance", Toast.LENGTH_LONG)
        }
    }

    fun getScooterDetail() {
        val scooterId = intent.getIntExtra(SCOOTER_ID, 0)
        title.setText("Scooter ${scooterId}")
        runBlocking {
//            val (request, response, result) = "${server}/todos/${scooterId}".httpGet().awaitStringResponse()
//            var scooter = JSONObject(result)
            var scooter = JSONObject("{\"id\": 1,\"latitude\": 10.9336,\"longitude\": 20.5323,\"battery_percentage\": 78,\"price_per_hour\": \"10.0\",\"provider_name\": \"Bolt\"}")
            scooterInfo.setText("Info:\nBattery percentage: ${scooter.get("battery_percentage")}% \nPrice per hour : ${scooter.get("price_per_hour")}$  \nProvider : ${scooter.get("provider_name")} ")
        }

    }
}