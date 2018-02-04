# <h1>GroupTask1(Python-flask)</h1>

#  <h2>Stripe Subscription Payment</h2>

# <h3>Installation Guide</h3>
    1.Python 2.6 or higher is usually required for installation for Flask on windows.
    The following command installs Virtual Environment on windows:
      1. pip install virtualenv.
    2.The virtual Environment will get installed in the path C:/pythonX/scripts path.Here X is the version name of Python.
    3.Once installed, new virtual environment is created in a  following folder as mentioned below.
        mkdir newproj
        cd newproj
        virtualenv venv
    4.On Windows, following can be used:
        1.venv\scripts\activate
                  (OR)
       On Linux/OS X, use the following:
        1.sudo apt-get install virtualenv
    5. We are now ready to install Flask in this environment.To install flask following command can be used:
        1. pip install Flask
    6.To configure flask code in cross origin request,follow the command specified below:
          1.pip install -U flask-cors
        
  # <h3>Run Python Flask Files</h3>
      1.Running on windows Command Prompt:
            1.Open Command Prompt and go to the directory where the file is located Eg:E:\python.
            2.Type: python filename.py and Press Enter key:
                  1. If you get the error stating that "python is not recognized as internal or external command"
                  then do the following:
                      1.1 Go to properties of This Pc--->Go to Advanced System Settings--->Go to Environmental variables--->
                      Select Path where you want to add the path  and Edit-->Type then type the semicolon ";" at the end
                      and copy the path of the python application and give ok. 
                      Eg:C:\Users\sandya\AppData\Local\Programs\Python\Python36.
                   2.Incase,if you didn't get any error then the command prompt will display the following lines: 
                      2.1  Restarting with stat 
                           Debugger is active! 
                           Debugger PIN: 264-240-688 
                           Running on http://127.0.0.1:5000/ (Press CTRL+C to quit).
           3.Then go to the local host "http://127.0.0.1:5000/" in your browser.To see the output add the extensions specified in the code.
           4.To Run app.py in windows command prompt follow the steps,
               4.1 For Inputing the SECRET_API_KEY and PUBLISHABLE_API_KEY(necessary for performing subscription):
                      4.1.1.set SECRET_API__KEY="your secret API KEY"(should not give within the double quotes),
                      4.1.2.set PUBLISHABLE_API_KEY="your publishable API KEY"(should not give within the double quotes)
               4.2. After entering API keys Run app.py command is:
                      4.2.1.python app.py
               4.3. Then go to the server http://127.0.0.1:5000/ and specify the path:
                      1.@app.route('/')---->http://127.0.0.1:5000/ (gives the customer list as json data).
                      2.@app.route('/cusid')--->http://127.0.0.1:5000/customerid (lists only th customer id as json data).
                      3.@app.route('/plan')---->http://127.0.0.1:5000/plan (lists the subscription plan).
                      4.@app.route('/subscribe')--->http://127.0.0.1:5000/subscribe(takes the customer id from customer list and makes the subscription for each customer).
                     5.@app.route('/listsub')---->http://127.0.0.1:5000/listsub(It will list the subscription list for each customer)
                     6.@app.route('/subscribe')---->http://127.0.0.1:5000/subscribe(It will create the subscription  for each customer with only one plan)
                     7.@app.route('/multiple_subscription')---->http://127.0.0.1:5000/multiple_subscription(It will create the multiple subscription  for each customer with different plan per subscription)
                     8.@app.route('/multiple_plans')---->http://127.0.0.1:5000/multiple_plan(It will create the one subscription  for each customer with multiple plan)

                        

