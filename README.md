Integration of Robot Framework with Travis CI and Sauce Labs
============================================================

Overview: This document describes integration of the Travis CI build system with a Robot Framework test suite running on AWS (Amazon Web Services) and then integration of the test suite on AWS with SauceLabs.

AWS system
----------

* To access the AWS system, run the following command from a command prompt.

~~~ sh
  $ mstsc
~~~

	`Login credentials to AWS System:
	IPAddress:    54.255.189.247
	User name: Administrator
	Password: <please see team member>`

* From a “Local system” (such as your desktop system), and using any browser, login to Travis-CI:

	`Travis CI Credentials:
	URL: https://travis-ci.com
	UserID: travismys
	Password: <please see team member>
	Select the repository  MySatori/mysatori-qa`

* From the Local system, and using any browser, login to SauceLabs:

	`SauceLabs Credentials:
	URL: https://saucelabs.com 
	UserId: jody3t
	Password: <please see team member>`
	
* Come back to the AWS system

The intention is that a build done by Travis CI will trigger execution of the test suite on the AWS system.This triggering of test execution is planned for builds of the “Development” thread.Builds of the “QA” thread can be scheduled by the Microsoft Task Scheduler and do not have to be triggered by Travis CI.

Communications between the Travis CI system and the AWS system is done using ZeroRPC.

The project is placed at `C:\Wizard_Latest` location on the AWS system.

We want to set up the AWS system so that it is waiting for Travis CI to trigger a test run.  From a command prompt, navigate to the `C:\Wizard_Latest` folder and run `server.py` as shown below.

~~~ sh
  $ python server.py
~~~

If you get an error, the port may already be in use.If the port is in use from an earlier running of server.py, then from the task manager kill `python.exe` and rerun the `server.py` command.

Now the port is listening.The test system is waiting for Travis CI to trigger a test run.Let’s go back to the Travis CI site.

* In  Travis-CI

Select `Current` Tab and click on `Restart Build` 

Click on the `Build History` tab. Select the greatest number link so you can view the build process.

* The build process is started.  Python, ZeroRPC, and related required software are installed.

Click on the `Current` tab to view the build steps.

Installation of Python and ZeroRPC is in progress initially and takes about 2-3 minutes.
At this time, the recommendation is to ignore build errors.  Wait until the command `python client.py` is seen.


* Once the command “python client.py” is displayed, move to the AWS test system. You can observe execution of the tests.  If the default configuration is used, the tests are run using a browser on the AWS system.  SauceLabs is not in use at this step.

* On completion close the command prompt.

Up to now we have seen how to trigger test execution from Travis CI to AWS. Now let’s trigger a test run from Travis-CI to AWS, where the tests are executed using a platform on SauceLabs.

* On the AWS system, navigate to the project folder and edit the ExecuteTestScript.bat file.

* Save the edited bat file and close the editor.

* Repeat steps 4 to 6 above.  This starts the build and triggers the test run again.

* This time, once the command “python client.py” is displayed, move to the SauceLabs screen. 

* You can observe the test suite execution.

* For more details, click on the View Full Screen Link.


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
