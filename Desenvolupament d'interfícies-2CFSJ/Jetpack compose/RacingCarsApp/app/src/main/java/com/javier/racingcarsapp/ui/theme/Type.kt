package com.javier.racingcarsapp.ui.theme

import android.R.attr.fontWeight
import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import com.javier.racingcarsapp.R


val Electrolize = FontFamily(
    Font(R.font.electrolize_regular)
)

val OpenSans = FontFamily(
    Font(R.font.opensans_regular),
    Font(R.font.opensans_bold)
)



// Set of Material typography styles to start with
val Typography = Typography(
    displayLarge = TextStyle(
        fontFamily = Electrolize, fontWeight = FontWeight.Normal, fontSize = 30.sp
    ),

    displayMedium = TextStyle(
        fontFamily = OpenSans, fontWeight = FontWeight.Bold, fontSize = 15.sp
    ),

    labelSmall = TextStyle(
        fontFamily = OpenSans, fontWeight = FontWeight.Bold, fontSize = 14.sp
    ),

    bodyLarge = TextStyle(
        fontFamily = OpenSans, fontWeight = FontWeight.Normal, fontSize = 14.sp
    )
)
