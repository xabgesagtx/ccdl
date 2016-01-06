# ccdl #

This is a python adapter to easily download content from Comedy Central via YoutubeDL

URL for show is first command line parameter.
The show will be:
* downloaded
* merged
* renamed
* copied to a folder defined in the scripts

# Installtion

Checkout the project.

In the directory do
```bash
python3 setup.py install
```

# Configuration

Configuration is done in $HOME/.ccdl-config 

Config file looks like this:

```json
{
  "shows": [
     {
        "name": "thedailyshow",
        "copy_to": "~/The Daily Show/",
        "regex": "the-daily-show"
     },
     {
        "name": "thenightlyshow",
        "copy_to": "~/The Nightly Show/",
        "regex": "the-nightly-show"
     }
   ],
   "fallback_dir": "~/temp/"
}
```


In shows you configure how a show is detected and where the merged file should be copied.

In fallback_dir you define the directory where all other files should be copied


# Prerequisites

* avconv
* python3
* setuptools
