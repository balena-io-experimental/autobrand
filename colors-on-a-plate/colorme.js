const Color = require('color');
const fs = require('fs');
const sdk = require('@balena/transformer-sdk');

sdk.transform(sentiment2color);

function sentiment2color(manifest) {
    const sentimentscore = manifest.input.contract.data.sentiment;
    console.dir('Input sentiment: ' + sentimentscore.toString());

    // scale the score so we can use it to get the H component of HSL color (0 to 360 degrees)
    // we give more resolution to positive (270 degrees) than negative (90 degrees)
    var degreesH = 0;
    var complementarydegreesH = 0;
    var zeropoint = 330;
    var contrastRatioTarget = 4.5;

    if(sentimentscore >=0) {
        degreesH = zeropoint - (270 * sentimentscore); // positive result
    } else {
        degreesH = zeropoint - (90 * sentimentscore);
        if (degreesH > 360) {
            degreesH = degreesH - 360;
        } 
    }

    // calculate the complementary color (180 deg offset)
    if (degreesH >= 180) {
        complementarydegreesH = degreesH - 180;
    } else {
        complementarydegreesH = degreesH + 180;
    }

    console.log('Calculated H: ' + degreesH.toString());
    console.log('Complementary H: ' + complementarydegreesH.toString());

    const primaryColor = Color('hsl(' + degreesH + ', 100%, 50%)');
    const complementaryColor = Color('hsl(' + complementarydegreesH + ', 100%, 50%)');

    console.log('Contrast: ' + primaryColor.contrast(Color("white")));
    var contrastAdjustedColor = primaryColor;

    while (contrastAdjustedColor.contrast(Color("white")) < contrastRatioTarget) {
        contrastAdjustedColor = contrastAdjustedColor.darken(0.01);
    }

    console.log('Primary: ' + primaryColor.hex());
    console.log('Primary (contrast adjusted): ' + contrastAdjustedColor.hex());
    console.log('Complementary: ' + complementaryColor.hex());

    return [{ contract: {
        type: 'colorset',
        data: {
          primary: primaryColor.hex(),
          complementary: complementaryColor.hex(),
          contrastAdjusted: contrastAdjustedColor.hex(),
          primaryRGB: primaryColor.rgb(),
          complementaryRGB: complementaryColor.rgb(),
          contrastAdjustedRGB: contrastAdjustedColor.rgb(),
          primaryName: primaryColor.keyword(),
          complementaryName: complementaryColor.keyword(),
          contrastAdjustedName: contrastAdjustedColor.keyword()
        }
      }, artifactPath: '/output' }]
}
