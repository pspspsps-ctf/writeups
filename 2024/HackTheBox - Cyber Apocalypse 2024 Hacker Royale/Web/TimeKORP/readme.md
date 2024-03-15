# TimeKORP

> Difficulty: Very Easy
>
> TBD

Solution: 

We are given with the source files to re-create the challenge locally. We can also spawn our Docker instance, which is `http://94.237.57.155:59233/`

![image](1.png)

Pressing either `What's the time?` or `What's the date?` will only change the URL parameter `format` to a hardcoded format

![image](2.png)

Looking at the `TimeController.php`, we can see it converts our parameter value based on the model, `TimeModel`

![image](3.png)

Based on `TimeModel.php` we can do a command injection attack since it passes the value to `exec()`

Looking at the Dockerfile, our target file, `flag`, it stored at `/flag`

![image](4.png)

So we can simply do `' ; cat '/flag` to escape the `date` command and to retrieve the contents of the `flag` file

![image](5.png)

Noice!

Flag: `HTB{t1m3_f0r_th3_ult1m4t3_pwn4g3}`
