# whole🌈
Script that uploads an image of every RGB color to <strike>Instagram</strike> Twitter. Configured to upload a new color every five minutes, slowly working its way through all 16,777,216 24bit RGB colors. It should finish sometime in the 2170s. We will never see the whole rainbow.

[See latest version in action over at @wholerainbow][wholerainbow], or, for an even more colorful social media experience, [check out Blot're](https://blot.re).

**update Feb 8, 2016** - Confirmed: Instagram hates rainbows. The script mysteriously stops and starts working, with the uploads succeeding but the images being insta deleted. Switched over the Twitter instead since their public API is not so intentionally crippled. You can find the original Instagram logic in the [Instagram branch](https://github.com/mattbierner/The-Whole-Rainbow/tree/instagram).

**update Feb 7, 2016** - Continuing with [@thewholerainbow2][wholerainbow2] since first rainbow mysteriously ended after reaching `0x000038`. Can also track using [#whole🌈](https://www.instagram.com/explore/tags/whole🌈/).

# Running
If you notice that the @thewholerainbow has stopped uploading, feel free to use these scripts to continue its mission. The uploads are also tagged with `#xHEXCOLOR #wholerainbow` so you can track what has been uploaded so far instead of starting from scratch.

The main logic is `main.py`. When run, the script uploads a single color and then updates some persisted data and exits.

First, make sure you have all the require dependencies:

```bash
$ pip install requests
$ pip install TwitterAPI
```

Then [register an application with Twitter](http://dev.twitter.com). To give the script permission to post, set the following environment variables

```bash
$ export RAINBOW_TWITTER_CONSUMER_KEY="your consumer key"
$ export RAINBOW_TWITTER_CONSUMER_SECRET="your consumer secret"
$ export RAINBOW_TWITTER_ACCESS_TOKEN_KEY="your token key"
$ export RAINBOW_TWITTER_ACCESS_TOKEN_SECRET="your token secret"
```

Then just run the script, `$ python main.py`. You can also pass all the arguments on the command line instead of using environment variables: `$ python main.py "consumer_key" "consumer_secret" "token_key" "token_secret"`

The current (to be uploaded) color is saved to `color.data` as an hex color.

Run the script using cron to upload all the rainbow. Here's the config to run once every five minutes:

```
*/5 * * * * /usr/bin/python thewholerainbow/main.py "consumer_key" "consumer_secret" "token_key" "token_secret"
```


[wholerainbow]: https://twitter.com/wholerainbow
