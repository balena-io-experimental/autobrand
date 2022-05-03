const fs = require('fs');
const vader = require('vader-sentiment');
var Sentiment = require('sentiment');
var sentiment = new Sentiment();

try {
    // assume repo readme is at /input/input.md
    const data = fs.readFileSync('/input/input.md', 'utf8');
    var intensity = vader.SentimentIntensityAnalyzer.polarity_scores(data);
    var result = sentiment.analyze(data);
    console.dir('Sentiment: ' + intensity.compound);
    try {
      fs.writeFileSync('/output/sentiment.txt', `${intensity.compound}`);
      fs.writeFileSync('/output/positive.txt', `${result.positive}`);
      fs.writeFileSync('/output/negative.txt', `${result.negative}`);
      // file written successfully
    } catch (err) {
      console.error(err);
    }
  } catch (err) {
    console.error(err);
  }