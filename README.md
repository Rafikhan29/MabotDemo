Mabot
=====

This document describe the installation of Robot framework , Mabot , GitHub, Travis-Ci, Travis-Ci integration with SauceLabs and Travis-Ci integration with AWS.

The purpose of using Robot Framework is to test automation framework for acceptance testing and acceptance test-driven development (ATDD). It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Using Mabot we can generate reports of manual test execution results in format understood by Robot frameworks report generation component. It allows combining manual and automated test results to one common report. Travis CI, a hosted continuous integration service used to build for open source and private projects hosted at GitHub. AWS is used to execute the test scripts in multiple virtual servers .Using SauceLabs we can run our tests on different platforms, browsers, and devices....

Mabot Installation
------------------

* Prerequisites: Install Python
* Download and install `mabot.exe` file from `robotframework-mabot downloads`location.See [robotframework-mabot] (https://code.google.com/p/robotframework-mabot/downloads/list)
Install `mabot-0.10.win-amd64.exe` for windows 64 bit version OS.
Install `mabot-0.10.win32.exe` for windows 32 bit version OS.

* Create a directory structure for Automation Test Cases and Manual Test cases for any sample Project.  

Designing manual steps
----------------------

* Open `Ride.py` as editor to design manual test case. Enter `ride.py` from command prompt or double click RIDE shortcut placed at desktop.
   
~~~ sh
  $ ride.py
~~~

* Open the project using File>>Open Directory option from Ride. Navigate to the project directory structure to open the project.
* Create a test suite, Select Folder (Manual Testsuites) and right click. From Context menu select "New Suite" option. Enter Suite name and click OK button.
* Select newly created test suite and right click. Select "New test case" option from context menu. Enter test case name and click OK button.
* Use Documentation for Test Case description.
* Tabular format is displayed. Use first column for step details, Second column for Test data and third for Expected results.

Execute manual steps
--------------------

* Open command prompt, enter `mabot` command and click enter.
  
~~~ sh
  $ mabot
~~~

* Mabot UI is displayed. Using "File>Open Dir", open the manual test suite to execute.
* Execute the steps described in manual test steps and update the status accordingly. In Message enter the Actual Results.
* As we observed in the above screen shot, click on each Test Case , Initially 'status' section shows Fail, after successful execution of manual test cases, update the status to `Pass/Fail` ,If Fails suggest the expected result in message box and store the results into user directory location.
* Complete the manual test suite execution. On completion save the results by selecting "File>Save As" option, and enter the execution result file path along with the name with .xml extension.

Combining automation and manual test results
--------------------------------------------
* Save manual test case execution results from Mabot to file system path with .xml file.
* Execute automation test scripts with the option to display the results in xml format. 
`[Project dir]>pybot -o [OutPutDirectoryLocation]\filenamexxx.xml [TestSuiteName].txt`
* Run rebot command to combine Automated and Manual test execution results.
`>rebot --name Combined AutomationOutput_filename.xml manual__output_filename.xml`
