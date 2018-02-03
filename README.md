# GroupTask1
IMAD_TASK3
# imad_task3
group task

My language framework is backend Python-flask

* Python 2.6 or higher is usually required for installation for Flask on windows.
* The following command installs Virtual Environment
                * pip install virtualenv
* It will get installed in the path C:/pythonX/scripts path.Here X is the version name of Python. pip install virtualenv

 * Once installed, new virtual environment is created in a folder.

    * mkdir newproj
    * cd newproj
    * virtualenv venv

* To activate corresponding environment, on Linux/OS X, use the following − On Windows, following can be used −
     
     * venv\scripts\activate

* We are now ready to install Flask in this environment.

    * pip install Flask
#Steps to run python-flask files:


* Step1:Open Command Prompt and go to the directory where the file is located
    Eg:E:\python
    
* Step2:Type: python filename.py and Enter if you get the error stating that python is not recognized as internal or external command 
then
go to properties of 
This Pc--->Go to Advanced System Settings--->Go to Environmental variables--->Select Path and Edit-->Type ";" at the end 
  and 
copy the path of the python application and give ok.
Eg:C:\Users\sandya\AppData\Local\Programs\Python\Python36.

  * Incase,if you didn't get any error then the cmd prompt will display the following lines:
                         * Restarting with stat
                         * Debugger is active!
                         * Debugger PIN: 264-240-688
                         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
                         
                         
* Step3:Then go to the local host "http://127.0.0.1:5000/" in your browser. To see the output add the extensions specified in the code.

 #Step4:TO RUN app.py

1.app.py displays the list of customers,lists the subscription plan which is created manually.

  #Before running app.py follow the procedures which I mentioned
   * To run the app.py in windows command prompt follow the steps,
   
        * we should input the secret API KEY and publishable API KEY.
        * command is :
            1.set SECRET_API__KEY="your secret API KEY"(should not give within the double quotes),
        
            2.set PUBLISHABLE_API_KEY="your publishable API KEY"(should not give within the double quotes)
                     
        * After entering the api key type:python app.py
        
            Then go to the server http://127.0.0.1:5000/ and specify the path:
            
                  1.@app.route('/')---->http://127.0.0.1:5000/ (gives the customer list as json data).
                  2.@app.route('/customerid')--->http://127.0.0.1:5000/customerid (gives only th customer id as json data).
                  3.@app.route('/plan')---->http://127.0.0.1:5000/plan (gives the subscription plan).
                  4.@app.route('/subscribe')--->http://127.0.0.1:5000/subscribe(takes the customer id from customer list and makes the subscription for each customer).
                  
                  5.@app.route('/listsub')---->http://127.0.0.1:5000/listsub(It will list the subscription list for each customer)
                  6.@app.route('/subscribe')---->http://127.0.0.1:5000/subscribe(It will create the subscription  for each customer with only one plan)
                  7.@app.route('/multiple_subscription')---->http://127.0.0.1:5000/multiple_subscription(It will create the multiple subscription  for each customer with different plan per subscription)
                  8.@app.route('/multiple_plans')---->http://127.0.0.1:5000/multiple_plan(It will create the one subscription  for each customer with multiple plan)
        
        
                    * NOTE:I added templates folder which contains HTML files,I used to check whether incoming customers are able to subscribe or not.It works perfectly for all kinds of subscription.   



                    
                    
 
