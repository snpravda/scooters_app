// Copyright 2020 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package com.example.mapwithmarker

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.github.kittinunf.fuel.coroutines.awaitStringResponse
import com.github.kittinunf.fuel.httpGet
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.Marker
import com.google.android.gms.maps.model.MarkerOptions
import kotlinx.coroutines.runBlocking
import okhttp3.*
import org.json.JSONArray

/**
 * An activity that displays a Google map with a marker (pin) to indicate a particular location.
 */
// [START maps_marker_on_map_ready]
class MapsMarkerActivity : AppCompatActivity(), OnMapReadyCallback {

    private var client = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Retrieve the content view that renders the map.
        setContentView(R.layout.activity_maps)

        // Get the SupportMapFragment and request notification when the map is ready to be used.
        val mapFragment = supportFragmentManager.findFragmentById(R.id.map) as? SupportMapFragment
        mapFragment?.getMapAsync(this)
    }

    override fun onMapReady(googleMap: GoogleMap) {
        runBlocking {
            val (request, response, result) = "${server}/scooters".httpGet().awaitStringResponse()
            val scooters = JSONArray(result)
//            val scooters = JSONArray("[{\"id\": 1,\"latitude\": 10.9336,\"longitude\": 20.5323,\"battery_percentage\": 78,\"price_per_hour\": \"10.0\",\"provider_name\": \"Bolt\"},{\"id\": 2,\"latitude\": 23.1442,\"longitude\": 43.3572,\"battery_percentage\": 65,\"price_per_hour\": \"10.0\",\"provider_name\": \"Bolt\"},{\"id\": 3, \"latitude\": 35.4458, \"longitude\": 28.6104,\"battery_percentage\": 100, \"price_per_hour\": \"9.0\", \"provider_name\": \"Uber\"}]")
            for (i in 0 until scooters.length()) {
                val scooter = scooters.getJSONObject(i)
                val coordinates = LatLng(scooter.get("latitude").toString().toDouble(), scooter.get("id").toString().toDouble())
                googleMap.addMarker(
                    MarkerOptions()
                        .position(coordinates)
                        .title(scooter.get("provider_name").toString())
                        .snippet("${scooter.get("battery_percentage")}\uD83D\uDD0B. ${scooter.get("price_per_hour")} \uD83D\uDCB2")
                )
                googleMap.moveCamera(CameraUpdateFactory.newLatLng(coordinates))
            }
        }

      // [START_EXCLUDE silent]

    }

}

