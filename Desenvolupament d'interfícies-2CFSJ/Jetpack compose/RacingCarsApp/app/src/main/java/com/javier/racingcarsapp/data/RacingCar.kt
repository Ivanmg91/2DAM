package com.javier.racingcarsapp.data

import androidx.annotation.DrawableRes
import androidx.annotation.StringRes
import androidx.compose.ui.input.key.Key.Companion.One
import com.javier.racingcarsapp.R

data class RacingCar(
    @StringRes val team: Int,
    @StringRes val driver: Int,
    @DrawableRes val imageTeamId: Int,
    @StringRes val description: Int,
    @StringRes val engine: Int,
    val year: Int
)

val racingCars = listOf(
    RacingCar(
        R.string.escuderia_ferrari,
        R.string.carlos_sainz,
        R.drawable.escuderia_ferrari_f1,
        R.string.description_ferrari,
        R.string.motor_ferrari,
        2024),
    RacingCar(
        R.string.escuderia_red_bull,
        R.string.max_verstappen,
        R.drawable.escuderia_redbull_f1,
        R.string.description_red_bull,
        R.string.motor_red_bull,
        2024),
    RacingCar(
        R.string.escuderia_mercedes,
        R.string.lewis_hamilton,
        R.drawable.escuderia_mercedes_f1,
        R.string.description_mercedes,
        R.string.motor_mercedes,
        2024),
    RacingCar(
        R.string.escuderia_mclaren,
        R.string.lando_norris,
        R.drawable.escuderia_mclaren_f1,
        R.string.description_mclaren,
        R.string.motor_mclaren,
        2024),
    RacingCar(
        R.string.escuderia_alpine,
        R.string.esteban_ocon,
        R.drawable.escuderia_alpine_f1,
        R.string.description_alpine,
        R.string.motor_alpine,
        2024),
    RacingCar(
        R.string.escuderia_aston_martin,
        R.string.fernando_alonso,
        R.drawable.escuderia_astonmartin_f1,
        R.string.description_aston_martin,
        R.string.motor_aston_martin,
        2024)
)

