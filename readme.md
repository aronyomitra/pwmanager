# Password Manager in Python

This is a CLI password manager and autologin app written in python

### Dependencies
- pynput   
(https://pypi.org/project/pynput/)
- pyperclip   
(https://pypi.org/project/pyperclip/)  
*Both modules can be installed easily using "pip install"*

### Usage Instructions
First thing, run the setup script using:  
<code>python setup.py</code> on the command line.

Then the main program can be started using:  
<code>python main.py</code>  

After starting main.py
1. Enter global passkey to access app
(passkey can be set inside source file main.py)  
>Default passkey="pass"  
**Note: It is recommended to change the default passkey**
2. Enter name of account ('fb', 'gmail', etc)
3. Click on the first login field in web browser within 3 seconds (timing can be changed in login.py)
4. You should be logged in. Enjoy!

### Adding accounts
You can add your own accounts by adding/editing lines in the file 'data.txt' inside the data folder, in the following format:  
>account:credential1,credential2,credential3.....  

In most cases there are only two credentials: username/email and password
>eg:  
gmail:username,password  
fb:email,password  
hotmail:johndoe,john1987  
**NOTE: The above format must be followed exactly. Make sure there are no spaces between the values**

When you add a new account, the program will follow the default procedure while logging in:  
1. Wait 3 seconds  
2. Enter first credential (username)
3. Press TAB ('\t')
4. Enter second credential (password)
5. Press ENTER ('\r')

If there are more than two credentials or the default login order is not suitable (*for example, maybe the password needs to be entered on a different page after entering username*) you need to edit login.py and add a custom login method (inside an elif comparison)  

The credentials will be available in a list called credList.

>eg:<pre><code>elif acc == 'twitter':
  time.sleep(5)
  keyboard.type(credList[0] + '\r');
  time.sleep(7)
  keyboard.type(credList[1] + '\r')</code></pre>

### Code Explanation
The pynput library provides functions to simulate keyboard input.  
<code>keyboard.type("Text")</code>  
Also, actions like ENTER and TAB can be simulated by using the special characters:  
- Carriage return: <code>'\r'</code>
- Horizontal Tab: <code>'\t'</code>


  Thus credentials can be entered automatically in this way, ***provided the user has already placed the cursor at the first input field.***


Hence, instead of typing straightaway, some time should be given to the user, with the function <code>time.sleep(n)</code>  
where n is the number of seconds

The function <code>pyperclip.copy("text")</code> can be used to copy text to the clipboard. This would allow users to copy text to clipboard. After that he can simply press CTRL+V to paste it to an input field
