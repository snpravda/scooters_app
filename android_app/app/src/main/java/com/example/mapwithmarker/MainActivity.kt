package com.example.mapwithmarker

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.auth.api.signin.GoogleSignIn
import com.google.android.gms.auth.api.signin.GoogleSignInOptions
import com.google.firebase.auth.FirebaseAuth
//import kotlinx.android.synthetic.main.activity_main.*

var server = "https://jsonplaceholder.typicode.com/"

class MainActivity : AppCompatActivity() {
    private lateinit var getScooterButton: Button
    private lateinit var sign_out_button: Button

    companion object {
        fun getLaunchIntent(from: Context) = Intent(from, MainActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK)
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setupUI()

        getScooterButton = findViewById(R.id.get_scooters_btn)
        getScooterButton.setOnClickListener {
            this.getScooters()
        }
    }

    private fun setupUI() {
        sign_out_button = findViewById(R.id.sign_out_button)
        sign_out_button.setOnClickListener {
            signOut()
        }
    }

    private fun signOut() {
        FirebaseAuth.getInstance().signOut()
        val gso = GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN)
            .requestIdToken(refresh_token)
            .requestEmail()
            .build()

        val googleSignInClient = GoogleSignIn.getClient(this, gso)
        googleSignInClient.signOut()
        startActivity(SignInActivity.getLaunchIntent(this))
    }

    private fun getScooters () {
        startActivity(Intent(this, MapsMarkerActivity::class.java))
    }
}