# Autobrand - giving all good ideas a good identity.
A GitHub Repository branding tool, automatically generating a name and logo from your Repo's README file.
 
## Description
Good ideas need good names, it helps them become tangible and physical, even if they're digital products. We know naming products is hard, really hard - so we take all the friction away to leaving you to focus on your next earth shattering idea.
 
Based on Brand First Development, Autobrand uses transformers to take the README from your products GitHub Repository and turn it into a brand, complete with name, colors, icon and logo.
 
---
 
## How it works
 
Autobrand is built upon a chain five transformers, each tackling a different step in turning your README into a brand:
 
### Sentiment analysis
 
The first step in taking text and creating a brand is to analyze it. We start by taking the top section of your README file, everything up to and including the first ## paragraph, and running it through two sentiment analysers. This gives an output of a list of both positive and negative key words, and a sentiment score ranging from -1 (negative) to +1 (Positive).
 
More details can be found [here](link to transformers README).
 
### Name generator

Next,  we again take the top section of your README file and strip out the stop words such as “the”, “an”, “a”, “of”, “or”, etc. and massage this through a GPT-2 AI model specifically tuned to generate project names.  The result of this process is a selection or singular name suggestion for your project.
 
More details can be found [here](link to transformers README).
 
 
### Color generator
 
Taking the previously outputted sentiment score this generator assigns it a color on the HSL color spectrum. Whilst not an exact science, the most negative scores will sit on the red section of the spectrum and the most positive will tend towards Orange and Yellow, the more neutral will occupy the Green and Blue hues. Along with creating a primary color for you brand, the generator will use color theory to choose a complimentary secondary color.
 
More details can be found [here](link to transformers README).
 
 
### Icon generator
 
Description here.
 
More details can be found [here](link to transformers README).
 
### Logo builder (In development)
 
The final stage of our chain of transformers creates a logo from the name and icon generated in the previous steps. As well as this it also compiles all the previous outputs into a single folder of brand assets.
 
More details can be found [here](link to transformers README).
 
---
 
## What this isn't
 
This isn't a replacement for an in depth brand design process (yet!), but what it seeks to do is give an idea a brand at the earliest possible opportunity with the least amount of friction, this almost fully automates the process of Brand First Development.
 
---
 
## More about Brand First Development
 
We believe that the best time to evaluate your idea is at the beginning, kind of obvious when you say it out loud really, but we also believe that this can be helped tremendously by creating a brand.
 
By creating a brand for your idea as one of the earliest stages of development something magic happens. What started out as a series of abstract notes written in a notepad, or text file, or even the classic back-of-napkin turns into a living breathing thing. It becomes a tangible, almost physical entity - one you can take a step back from and admire, and more importantly evaluate.
 
You now ask questions of it, what is your purpose? how do you see the world? what do you sound like?...
 
Even better, you can ask questions on behalf of your users. Would they find you useful, would you appeal to them? If yes, then great you're on the right track! If not, you may have discovered some fundamental challenges your idea faces, or perhaps just a change of positioning to your user.
 
We'll be writing more about Brand First Development in the future, but for now if you have any questions please get in touch.
