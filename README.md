# AmateurRadioPrograms
These are helper programs for amateur radio, for the terminal shell.


- hamRadioPrefix.py and hamRadioPrefix_offline.py take as input the prefix of an amateur radio call sign and displays country information for it, like country name,	continent,	itu and	cq zones, in the terminal shell.
The offline version downloads the needed csv table at first use, such that it then can be used for mobile operation without internet access.
With internet access and a browser, for more detailed call lookup, see also: https://hamcall.net/call

- hamRadioPrefix_Form.ipynb is the Colab notebook version of hamRadioPrefix.py. Click on the "open in Colab" button in it, or here:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/hamRadioPrefix_Form.ipynb)

- solarfluxdisp.py displays the current Observed Flux Density from www.spaceweather.gc.ca

- qth_locator_distance_city.py takes as input the own QTH locator and a received QTH locator, and displays the distance in Kilometer, and the nearest big city larger 100k inhabitants and larger 1M inhabitants, for georgraphic context. It uses the csv file 'large_cities.csv'.
- You can also run it in this browser app, which runs purely in your browser, hence also offline after opening it:
[qth_locator_distance_city.html](https://htmlpreview.github.io/?https://github.com/TUIlmenauAMS/AmateurRadioPrograms/blob/main/qth_locator_distance_city.html)

- solarflux_qth_distance_city.ipynb is a Colab notebook which runs the previous 2 programs in a Colab virtual machine. This might be useful if there is no local Python installation, like on a smartphone. To run it, you can click on this button: <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/solarflux_qth_distance_city.ipynb)

- The predictiveDenoiser.html is an alternative to many build in Noise Reduction functions. It reduces the attenuation of high frequencies, which is a noticeable disadvantage of many radios build noise reduction.  First, allow a few seconds for adaptation to the (speech) signal, at approx. mu=0.05, then switch to freeze adaptation to get the imporved audio. Repeat if necessary. Experiment with the different settings. You can download the predictiveDenoiser.html file and serve it locally with 'python3 -m http.server 8080', and then open your browser with 'localhost:8080', or just click on this link to serve it in github.io:
[predictiveDenoiser.html](https://htmlpreview.github.io/?https://github.com/TUIlmenauAMS/AmateurRadioPrograms/blob/main/predictiveDenoiser.html)

These Python programs where made with the help of ChatGPT and then refined. The Browser apps where made with Grok.com.

Many greetings,
  Gerald, DL5BBN
  
 
