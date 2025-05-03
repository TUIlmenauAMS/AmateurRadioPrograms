# AmateurRadioPrograms
These are helper programs for amateur radio, for the terminal shell.


- hamRadioPrefix.py and hamRadioPrefix_offline.py take as input the prefix of an amateur radio call sign and displays country information for it, like country name,	continent,	itu and	cq zones, in the terminal shell.
The offline version downloads the needed csv table at first use, such that it then can be used for mobile operation without internet access.
With internet access and a browser, for more detailed call lookup, see also: https://hamcall.net/call

- hamRadioPrefix_Form.ipynb is the Colab notebook version of hamRadioPrefix.py. Click on the "open in Colab" button in it, or here:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/hamRadioPrefix_Form.ipynb)

- solarfluxdisp.py displays the current Observed Flux Density from www.spaceweather.gc.ca

- qth_locator_distance_city.py takes as input the own QTH locator and a received QTH locator, and displays the distance in Kilometer, and the nearest big city larger 100k inhabitants and larger 1M inhabitants, for georgraphic context. It uses the csv file 'large_cities.csv'.
- solarflux_qth_distance_city.ipynb is a Colab notebook which runs the previous 2 programs in a Colab virtual machine. This might be useful if there is no local Python installation, like on a smartphone. To run it, you can click on this button:
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/solarflux_qth_distance_city.ipynb)

These programs where made with the help of ChatGPT and then refined.

Many greetings,
  Gerald, DL5BBN
  
 
