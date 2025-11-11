Overview :

The Bulk Send Randomizer is a python script that allows you to send bulk emails to a list of recipients using randomized SMTP server, subject , message , links, names. 

Features :

	Increase Email Spam Bypass
    - The script uses randomized SMTP server, subject, message, name, link for sending emails to increase the chances of bypassing spam filters.
    Flexible Sending Speed
    - The script allows you to select the sending speed mode - either slow (with a delay between sending emails) or fast (using multiple threads).
    Personalized Email Campaigns
    - The script allows you to use tags in the subject and message to personalize the emails for each recipient.

    * If you require additional features or customization for this script, please do not hesitate to contact us. Our team is available to assist you in finding the best solution for your specific needs. Whether you need help with installation, configuration or further development, we are here to help. 

install :

	Install the required libraries

	pip install -r requirements.txt

Usage :
	
    1 - Update the files with the appropriate information :

    	- emails.txt: a list of email addresses
		- smtps.txt: a list of SMTP servers to send the emails through, in the format host|port|user|passwd
		- subjects.txt: a list of subject lines for the emails
		- froms.txt: a list of sender email addresses names
		- links.txt: a list of links to include in the emails
		-/templates/*: a list of html template to be send 

    2 - You can customize the Tags in the subject and message to personalize the emails for each recipient.
    3 - Run the script by executing the command python3 bulk_send_randomizer.py
    4 -The script will prompt you to select the sending speed mode and enter the necessary details (such as delay time or number of threads).
    
    Then the script will start sending emails .


Note :

    Use this script at your own risk.
    Sending unsolicited emails is illegal in some countries, make sure to comply with the laws of your country before using this script.
    The script is for educational and testing purposes only, use it responsibly.
