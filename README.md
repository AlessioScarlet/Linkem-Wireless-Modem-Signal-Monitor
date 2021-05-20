# Linkem Wireless Modem Signal Monitor
This python program will monitor and log your wireless linkem modem signal every 5 seconds.
![](https://i.imgur.com/wvnB5Sh.png)
![](https://i.imgur.com/yO1IJdQ.png)
![](https://i.imgur.com/zaxxxp4.png)

# How to install:

You will need to install the [requests](https://pypi.org/project/selenium/ "requests") library, by typing in your console:

`pip install selenium`

### I'M USING FIREFOX AS THE WEBDRIVER! CHROME SUCKS, UNINSTALL IT ASAP.

Then, save the "geckodriver.exe" file in any folder.
Edit the 16th line and paste the executable path. If you downloaded it in the Downloads folder, it should look like this:

`driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\Users\\YOUR_PC_NAME\\Downloads\\geckodriver.exe")`

If you've installed firefox in a different folder than C:\\Program Files\\Mozilla Firefox\\firefox.exe, change the 15th line accordingly too.

Now, check the 27th and 28th lines.

"guest" and "linkem123" are the default username and passwords. 

If you've changed them, just swap them with your username/password. 

If you didn't, you're ready to go.

It will create a logs.txt file, that indicates the signal + the time it was recorded.

If you'd like to see what the statistical average of the signal is, open averagecalc.py. It obviously has to be in the same folder as the logs.txt file.

I've noticed that it logs you off after 10 minutes, so I made it so that it closes and reopens every 540 seconds (9 minutes), just to be sure.
