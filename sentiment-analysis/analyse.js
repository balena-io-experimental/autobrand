const fs = require('fs');
const vader = require('vader-sentiment');
const sdk = require('@balena/transformer-sdk');

var Sentiment = require('sentiment');
var sentiment = new Sentiment();

sdk.transform(text2sentiment);

async function text2sentiment(manifest) {
  var intensity = vader.SentimentIntensityAnalyzer.polarity_scores(manifest.input.contract.data.content);
  var result = sentiment.analyze(manifest.input.contract.data.content);
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