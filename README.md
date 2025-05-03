# AmateurRadioPrograms
These are helper programs for amateur radio, for the terminal shell.


- hamRadioPrefix.py and hamRadioPrefix_offline.py take as input the prefix of an amateur radio call sign and displays country information for it, like country name,	continent,	itu and	cq zones, in the terminal shell.
The offline version downloads the needed csv table at first use, such that it then can be used for mobile operation without internet access.
With internet access and a browser, for more detailed call lookup, see also: https://hamcall.net/call

- hamRadioPrefix_Form.ipynb is the Colab notebook version of hamRadioPrefix.py. Click on the "open in Colab" button in it.
- <a href=\"https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/hamRadioPrefix_Form.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>

- solarfluxdisp.py displays the current Observed Flux Density from www.spaceweather.gc.ca

- qth_locator_distance_city.py takes as input the own QTH locator and a received QTH locator, and displays the distance in Kilometer, and the nearest big city larger 100k inhabitants and larger 1M inhabitants, for georgraphic context. It uses the csv file 'large_cities.csv'.

These programs where made with the help of ChatGPT and then refined.

Many greetings,
  Gerald, DL5BBN
  
 
