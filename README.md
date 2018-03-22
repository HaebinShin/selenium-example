# Selenium Example
This is the example of using Selenium with Chrome. It alse introduce reservation way periodic task using crontab.

This example script clicks button of the DOM element which matching the given "id".

## Usage
### script.conf
Default configuration file used in run.py
- dest: target page url.
- id: HTML tag's id to do something.
- chromedriver_path: chromedriver path.
    - Download from ![https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - Must be check *Supports Chrome Version*.
- profile_path: user data file path (optional)
    - Write *Profile Path* from ![chrome://version](chrome://version).
    - In case of using Chromium, write path before "....../....../Default" written in *Profile Path*.
- browser_bin_path: binary file path (optional)
    - Ubuntu default path: /usr/bin/google-chrome

### run.py
- Example script
    - It clicks button of the DOM element which matching the given "id".

### crontab
- Reserve task by `crontab -e`
- `00 18 * * 1-5 env DISPLAY=:0 /usr/bin/python3 {dir}/run.py >> {dir}/log.txt 2>&1`
    - Meaning that run script at every weekday 6:00 PM.