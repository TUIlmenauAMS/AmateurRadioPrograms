# AI for Amateur Radio Programs

This repository contains amateur radio helper programs made with the help of AI.
The following context and background came out of discussions with my amateur radio club, DK0TU. 

AI in amateur radio has the advantage that programs can be made in a fraction of the time previously necessary, and that new software projects are possible with it, for instance in a new programming language. This is a lot of fun, when you get a feeling of what works and what not :-). There are also some pitfalls, which can be avoided using the approaches described below.

Media is trying to please its expected audience or information bubble, or provoke to get attention, which does not necessarily align with the audience's interests. The same is true for AI, it tries to please its user, which is not necessarily in its interest. Hence critical thinking is required, and for the latter, AI literacy on how to use AI collaboratively, as a “Copilot”. Hence, a good knowledge of the programming language generated is still helpful.

This repository features helper programs for amateur radio, as Python programs for the terminal shell, and as browser apps. The aim is also to excite you to do your own experiments using AI as a tool to generate software, for your own experience and judgement, since this is the software development tool of the future, for instance with Cursor, Interpreter, or Codex. For this reason I also added information (like the used AI) to make it more or less reproducible, and as references. For this reason I also included the used (initial) prompt in the beginning of the programs as comments. For best practice and as a workflow, see also the document ["AI-Assisted Workflow for Writing Software.pdf"](https://github.com/TUIlmenauAMS/AmateurRadioPrograms/blob/main/AI-Assisted%20Workflow%20for%20Writing%20Software.pdf). Basically it is like Test Driven Development (TDD).

Large Language Models, as Natural Language Processing (NLP), can also be used as “Natural Language Programming”, like an "Utra High Level Programming Language", which generates, for instance, Python code. The Python interpreter can generate C code. The C compiler generates assembler code, and the assembler generates machine code. When setting their “temperature” parameter of the LLM to zero, as the AI programming tools seem to do by default, their output becomes deterministic, like a compiler. And like with any other programming language, the main work is usually debugging. A major advantage of NLP is that it gives new ideas.

In the same way can program compilers and interpreters (like for C and Python) be seen as language processing, just a very strictly formal language, which became more and mor complex as they are developed from early languages like Basic, to increasing sphisticated ones like Pascal, C, and Python as a Very High Level Language. It is only a logical step to the next level, the "Ultra High Level Language" as natural language processing. 


Good references for **AI Coding Tools** are also:

[https://spectrum.ieee.org/best-ai-coding-tools](https://spectrum.ieee.org/best-ai-coding-tools)

[DFKI: Generative_AI_in_Software_Engineering_Transforming_the_Software_Development_Process_2025](https://www.dfki.de/fileadmin/user_upload/DFKI/Medien/News/2025/Wissenschaftliche_Exzellenz/Generative_AI_in_Software_Engineering_Transforming_the_Software_Development_Process_2025.pdf) 

This also addresses the technical experimental character of amateur radio :-).

Here are interesting publications on the **copyrights issue**: 

["Protecting Your Code: Copyright and Other Best Practices"](https://www.bakerdonelson.com/think-while-you-are-using-ai-coding)

[“LiCoEval: Evaluating LLMs on License Compliance in Code Generation”](https://arxiv.org/html/2406.10952)

This last paper looks interesting, because it has a quantification, and a section on best practices for open-source communities (which now mostly use AI as well). I don’t think a 1% license compliance risk is that high. I guess that percentage is higher for hand-generated code, because people often resort to copy/paste from Stack Exchange or similar sources. In general, the most important factor for quality is thorough testing. What matters is that a program passes tests, not how it was made. I often find AI-generated code much more readable than typical hand-written code, which is also good for testing.

Is open source as AI training fair use?:

["A New Look at Fair Use: Anthropic, Meta, and Copyright in AI Training"](https://www.reedsmith.com/articles/a-new-look-fair-use-anthropic-meta-copyright-ai-training/):

The courts ruled “Anthropic and Meta decisions both suggest fair use…should factor into market harm analysis”. This confirms the current interpretation of fair use, but introduces "marked harm", meaning the marked of the original rights holders should not be harmed by it.

I myself am writing open source programs since many years. Its basic rule is "use it and contribute to it in return". I would be very happy if my code is used for training Large Language Models. Their new possibilities are a tremendous return for me!


I found this Google paper about **power consumption of LLM's** interesting:
["Measuring the environmental impact of delivering AI at Google Scale"](https://arxiv.org/abs/2508.15734v1). 
It says “..median Gemini Apps text prompt uses less energy than .. 0.24 Wh.” With a MacBook with a power consumption of approx. 5W, this equates to approx. 3 minutes of runtime. This is roughly comparable to a compiler run. 
Fun fact: Compare this with a human answering: A human has an average power consumption of about 80W (https://en.wikipedia.org/wiki/Human_power). This means that 0.24Wh corresponds to about 0.18s of work. Hence, if a human needs more than this fraction of a second to answer, the LLM is more energy efficient.

Also keep in mind, if this power comes from non-fossile, renewable sources (like a green electricity plan), it agress with climate protection in any case. I think AI can also be used to increase efficiencies to reduce the use of fossile fuels, and hence can help the goal of climate protection.

**Here are the programs,**

- `hamRadioPrefix.py` and `hamRadioPrefix_offline.py` take as input the prefix of an amateur radio call sign and displays country information for it, like country name,	continent,	itu and	cq zones, in the terminal shell.
The offline version downloads the needed csv table at first use, such that it then can be used for mobile operation without internet access.
With internet access and a browser, for more detailed call lookup, see also: https://hamcall.net/call

- `hamRadioPrefix_Form.ipynb` is the Colab notebook version of hamRadioPrefix.py. Click on the "open in Colab" button in it, or here:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/hamRadioPrefix_Form.ipynb)

- `solarfluxdisp.py displays` the current Observed Flux Density from www.spaceweather.gc.ca

- `qth_locator_distance_city.py` takes as input the own QTH locator and a received QTH locator, and displays the distance in Kilometer, and the nearest big city larger 100k inhabitants and larger 1M inhabitants, for georgraphic context. It uses the csv file 'large_cities.csv'.
- You can also run it in this browser app, which runs purely in your browser, hence also offline after opening it:
[qth_locator_distance_city.html](https://htmlpreview.github.io/?https://github.com/TUIlmenauAMS/AmateurRadioPrograms/blob/main/qth_locator_distance_city.html)

- `solarflux_qth_distance_city.ipynb` is a Colab notebook which runs the previous 2 programs in a Colab virtual machine. This might be useful if there is no local Python installation, like on a smartphone. To run it, you can click on this button: <br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TUIlmenauAMS/AmateurRadioPrograms/blob/main/solarflux_qth_distance_city.ipynb)

- The `predictiveDenoiser.html` is an alternative to many build in Noise Reduction functions. It reduces the attenuation of high frequencies, which is a noticeable disadvantage of many radios build noise reduction.  First, allow a few seconds for adaptation to the (speech) signal, at approx. mu=0.05, then switch to freeze adaptation to get the imporved audio. Repeat if necessary. Experiment with the different settings. You can download the predictiveDenoiser.html file and serve it locally with 'python3 -m http.server 8080', and then open your browser with 'localhost:8080', or just click on this link to serve it in github.io:
[predictiveDenoiser.html](https://htmlpreview.github.io/?https://github.com/TUIlmenauAMS/AmateurRadioPrograms/blob/main/predictiveDenoiser.html)

- `speech_to_text_offline.py` is a program for local realtime speech recognition without an internet connection. It could be used to control programs, like WSJT-X, in portable operation, or used as a very low bit-rate speech coder, where the recognized text is transmitted using a digimode like PSK31 or JT8Call.

These Python programs where made with the help of ChatGPT and then refined. The Browser apps and the speech_to_text_offline.py Python program where made with the help of Grok.com.

Many greetings,73,

  Gerald, DL5BBN
  
 
