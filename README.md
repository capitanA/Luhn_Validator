CONTENTS OF THIS FILE
---------------------

 * [INTRODUCTION](#Introduction)
 * [REQUIREMENTS](#Requirements)
 * [INSTALLATION](#Installation)
 * [CONFIGURATION](#Configuration)
 * [SUPPORT](#Support)



Introduction
------------

This project aimed to validate alberta PHN numbers. Alberta PHNs consist of 9 digits with no letters. The PHN has a check digit in the 5th position.
A PHN is valid if the check digit calculated by the Modulus 10 algorithm matches the check digit in the PHN. The ModuleTen algorithm used in this project could be used for any other numbers that need to be checked with the module10 algorithm. 
Just provide the position of the check digit in ModuleTen class, and then it will check if that input is valid or not.

  
Requirements
------------
Only requirement is python3 installed in your system. 

Installation
------------
1- Run the project by the following command line:

    python3 run.py "Your Input PHN"

Configuration
-------------

There is no specific configuration needed for this project


Support
-----------

If you are having issues, please let us know.
* Arash Fassihozzaman Langroudi - email: afassihozzam@mun.ca
