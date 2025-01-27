package com.javier.racingcarsapp

import android.R.attr.contentDescription
import android.R.attr.onClick
import android.R.attr.text
import android.R.attr.top
import android.graphics.drawable.Icon
import android.graphics.drawable.shapes.Shape
import android.graphics.fonts.Font
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.annotation.DrawableRes
import androidx.annotation.StringRes
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.animateContentSize
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ExpandLess
import androidx.compose.material.icons.filled.ExpandMore
import androidx.compose.material3.Card
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.Icon
import androidx.compose.material3.Typography

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.input.key.Key.Companion.I
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.dimensionResource
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.res.vectorResource
import androidx.compose.ui.tooling.preview.Preview

import com.javier.racingcarsapp.data.RacingCar
import com.javier.racingcarsapp.data.racingCars
import com.javier.racingcarsapp.ui.theme.RacingCarsAppTheme
import com.javier.racingcarsapp.ui.theme.Typography
import com.javier.racingcarsapp.ui.theme.secondaryDark
import com.javier.racingcarsapp.ui.theme.secondaryLight

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            RacingCarsAppTheme {
                RacingCarsApp()
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun RacingCarsApp() {
        Scaffold(
            topBar = {
                RacingCarsTopAppBar()
            }
        ) { innerPadding ->
            LazyColumn(
                modifier = Modifier
                    .fillMaxSize() // Add fillMaxSize() here
                    .padding(innerPadding) // Keep innerPadding
            ) {
                items(racingCars) { car ->
                    CarItem(
                        car = car,
                        modifier = Modifier
                            .padding(dimensionResource(id = R.dimen.padding_small))
                    )
                }
            }
        }
}


@Composable
fun CarItem(
    car: RacingCar,
    modifier: Modifier = Modifier
) {
    var expanded by remember { mutableStateOf(false) }
    // REVISAR val color by animateColorAsState(/*TODO, aquí agregamos el color de fondo correspondiente si está expandido o si no lo está. Si no quieres desarrollar esta parte, elimina el código correspondiente */)
    Card(
        modifier = modifier

    ) {
        Column(
            modifier = Modifier
                .animateContentSize(
                    animationSpec = spring(/*TODO, agregaremos la animación correspondiente de resorte*/)
                )

                //.background(color = color)
        )
        {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(dimensionResource(R.dimen.padding_small))

            ) {
                CarIcon(car.imageTeamId)
                CarInformation(car.team, car.driver, car.year)
                Spacer(modifier = Modifier.weight(1f))
                CarItemButton(
                    expanded = expanded,
                    onClick = {
                        if (expanded == false) {
                            expanded = true
                        } else {
                            expanded = false
                        }
                    }
                )
            }
            if(expanded) {
                CarDescription(
                    car.description,
                    car.engine,
                    modifier = Modifier.padding(end = dimensionResource(R.dimen.padding_medium), top = dimensionResource(R.dimen.padding_small), start = dimensionResource(R.dimen.padding_medium), bottom = dimensionResource(R.dimen.padding_medium))
                )
            }
        }
    }
}


@Composable
private fun CarItemButton(
    expanded: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    IconButton(
        onClick = onClick,
        modifier = modifier
    ){
        Icon(
            imageVector = Icons.Default.ExpandMore,
            contentDescription = stringResource(R.string.expand_button_content_description),
            tint = secondaryLight // REVISAR
        )
    }




}
/**
 * Composable that displays a photo of a racing car.
 *
 * @param carIcon is the resource ID for the image of the car
 * @param modifier modifiers to set to this composable
 */
@Composable
fun CarIcon(
    @DrawableRes carIcon: Int,
    modifier: Modifier = Modifier
) {
    Image(
        modifier = modifier          //Ojo este modifier es en minúscula//
            .size(dimensionResource(R.dimen.image_size))
            .padding(dimensionResource(R.dimen.padding_small))
            .clip(shape = MaterialTheme.shapes.small),

        painter = painterResource(carIcon),     //para cargar el recurso de imagen//
        contentScale = ContentScale.Crop,

        contentDescription = null
    )
}

@Composable
fun CarDescription(
    @StringRes carDescription: Int,
    @StringRes carEngine: Int,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier
    ) {
        Text(
            text = stringResource(R.string.motor),
        )

        Text(
            text = stringResource(carEngine),
            style = Typography.bodyLarge
        )

        Spacer(modifier = Modifier.weight(1f))

        Text(
            text = stringResource(R.string.description),
            style = Typography.labelSmall
        )
        Text(
            text = stringResource(carDescription),
            style = Typography.bodyLarge
        )

    }
}

@Composable
fun CarInformation(
    @StringRes carName: Int,
    @StringRes driver: Int,
    carYear: Int,
    modifier: Modifier = Modifier
) {
    Column(modifier = modifier) {
        Text(
            text = stringResource(carName),
            style = Typography.displayMedium,
            modifier = Modifier.padding(top = dimensionResource(R.dimen.padding_small))
        )

        Row {
            Text(
                text = stringResource(R.string.driver),
                style = Typography.labelSmall,
            )
            Text(
                text = stringResource(driver),
                style = Typography.bodyLarge,
                modifier = Modifier.padding(start = dimensionResource(R.dimen.padding_small))

                )
        }

        Text(
            text = stringResource(R.string.year, carYear),
            style = Typography.bodyLarge
        )
    }
}


@OptIn(ExperimentalMaterial3Api::class)     //Esta anotación es necesaria para usar
// el CenterAlignedTopAppBar. No está en el tutorial de la web//
@Composable
fun RacingCarsTopAppBar(modifier: Modifier = Modifier) {
    CenterAlignedTopAppBar(
        title = {
            Row {
                Icon(
                    painter = painterResource(R.drawable.ic_formula1_logo),
                    contentDescription = stringResource(R.string.description)
                )
                Text(
                    text = stringResource(R.string.app_name),
                )
            }
        },
        modifier = modifier
    )
}


/**
 * Composable that displays what the UI of the app looks like in light theme in the design tab.
 */
@Preview
@Composable
fun RacingCarsPreview() {
    RacingCarsAppTheme(darkTheme = false) {
        RacingCarsApp()
    }
}

@Preview
@Composable
fun RacingCarsDarkThemePreview() {
    RacingCarsAppTheme(darkTheme = true) {
        RacingCarsApp()
    }
}
