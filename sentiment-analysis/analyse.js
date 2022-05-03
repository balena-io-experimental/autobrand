const fs = require('fs');
const vader = require('vader-sentiment');


try {
    // assume repo readme is at /input/input.md
    const data = fs.readFileSync('/input/.md', 'utf8');
    var intensity = vader.SentimentIntensityAnalyzer.polarity_scores(data);
    console.dir('Sentiment: ' + intensity.compound);
    try {
      fs.writeFileSync('/output/sentiment.txt', `${intensity.compound}`);
      // file written successfully
    } catch (err) {
      console.error(err);
    }
  } catch (err) {
    console.error(err);
  }