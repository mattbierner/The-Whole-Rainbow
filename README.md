# whole🌈
Script that uploads an image of every RGB color to Instagram. Configured to upload a new color every five minutes, slowly working its way through all 16,777,216 24bit RGB colors. It should finish sometime in the 2170s. We will never see the whole rainbow.

[See it in action over at @thewholerainbow][wholerainbow], or, for an even more colorful social media experience, [check out Blot're](https://blot.re).

**update Feb 7, 2016** - Continuing with [@thewholerainbow2][wholerainbow2] since first rainbow mysteriously stopped working after reaching `0x000038`. Can also track using [#whole🌈](https://www.instagram.com/explore/tags/whole🌈/).

#### Why don't the colors in the uploaded images exactly match the targeted hex values?
Instagram takes jpeg images and performs some post processing that may alter the precise color values.

#### Will Instagram have a problem with this?
I hope not. Their public API lacks the ability to upload images (WTF), so this script makes use of an unofficial API to automate the upload process. The script is designed to run very slowly, and the uploaded images are extremely tiny, so it does not consume many resources at all.

This is a fun little project that shouldn't bother anyone and improves the community. Just in case however, I recommend using a burner account if you plan on using the scripts found in this repo. If @thewholerainbow suddenly stops working, most likely someone at Instagram just hates rainbows.

# Running
If you notice that the @thewholerainbow has stopped uploading, feel free to use these scripts to continue its mission. The uploads are also tagged with `#whole🌈`, `#HEX_COLOR` so you can track what has been uploaded so far instead of starting from scratch.

The main logic is `main.py`. When run, the script uploads a single color and then updates some persisted data and exits.

First, make sure you have all the require dependencies:

```bash
$ pip install requests
```

And make sure to set the following environment variables to give the script permission to upload to an Instagram account:

```bash
$ export INSTAGRAM_USER_ID="your user name"
$ export INSTAGRAM_USER_PASSWORD="your password"
```

Then just run the script, `$ python main.py`. The current (to be uploaded) color is saved to `color.data` as an hex color.

Run the script using cron to upload all the rainbow. Here's the config to run once every five minutes:

```
*/5 * * * * /usr/bin/python thewholerainbow/main.py "USER_NAME" "PASSWORD"
```

# Credits
Python Instagram uploader copied from https://github.com/lukecyca/python-instagram-upload


[wholerainbow]: https://www.instagram.com/thewholerainbow/
[wholerainbow2]: https://www.instagram.com/thewholerainbow2
