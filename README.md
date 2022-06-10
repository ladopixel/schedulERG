<h2>schedulERG</h2>

<img src="https://camo.githubusercontent.com/ec19f4f188a819aea16eab8fb5d11c3916eda23f447e34ec2e03a57a321d7f38/68747470733a2f2f6572676f706c6174666f726d2e6f72672f696d672f6c6f676f747970655f77686974652e737667" alt="Logotipo ErgoPlatform">

<p>Simple application written in python to interact with the <a href="https://ergoplatform.org">Ergo blockchain</a> from the terminal.
<br>Undoubtedly, the <a href="https://github.com/mgpai22/ergpy">ergpy repository</a> has been fundamental for the creation of tERGminal.</p>

<p>From schedulERG you can create and query tokens on the Ergo blockchain by encrypting and decrypting the description with a password.</p>

<hr>

<h2>Quick Start</h2>
<code>If you are going to work with a computer other than Raspberry Pi, jump directly to Install dependencies</code>

<h3>Raspberry Pi</h3>
<h4>Prepare installation Raspberry Pi</h4>

~~~
sudo apt update && sudo apt upgrade -y
sudo apt install git pip openjdk-8-jre -y
~~~

<h4>Pi Zero</h4>

We need to explicity call Java 8 otherwise you will receive a "Server VM is only supported on ARMv7+ VFP" error. To correct this run the following ([credit](https://raspberrypi.stackexchange.com/questions/104203/unable-to-run-java-on-raspberry-pi-zero-vm-is-only-supported-on-armv7-vfp)): 

~~~
sudo update-alternatives --config java
# Then select Java 8's menu number
~~~

<h3>Install dependencies</h3>

~~~
pip install JPype1 ergpy
~~~

<h3>Clone repo</h3>

~~~
git clone https://github.com/ladopixel/schedulERG.git
~~~

<h3>Launch schedulERG</h3>

~~~
cd schedulERG
python schedulERG.py
~~~

<hr>

<h3>Option 1 - Add contact</h3>
<p>With this option, we mint a token with the encrypted description.</p>
<img src="https://ergotokens.org/schedulERG-Add.png" atl="Add tokens in schedulERG">

<h3>Option 2 - Info contact</h3>
<p>To consult all the tokens of a wallet to decipher the description of the one we are interested in.</p>
<img src="https://ergotokens.org/schedulERG-Info.png" atl="Add tokens in schedulERG">
