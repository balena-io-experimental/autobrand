const fs = require('fs');
const vader = require('vader-sentiment');
const sdk = require('@balena/transformer-sdk');

var Sentiment = require('sentiment');
var sentiment = new Sentiment();

sdk.transform(text2sentiment);

async function text2sentiment(manifest) {

  // assume repo readme is at /input/input.md
  const data = fs.readFileSync(manifest.input.artifactPath, 'utf8');
  var intensity = vader.SentimentIntensityAnalyzer.polarity_scores(data);
  var result = sentiment.analyze(data);
  console.dir('Sentiment: ' + intensity.compound);

  return [{ contract: {
    type: 'sentiment',
    data: {
      sentiment: intensity.compound,
      positivewords: result.positive,
      negativewords: result.negative
    }
  }, artifactPath: '/output' }]

}