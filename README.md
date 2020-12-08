# AutomateOlympicCoding
I made a **Test Case Parser** and it can parse test cases for your problem in just one keystroke.

**Update** : **Contest Parser** was also added

Download the github repo from here : [AutomateOlympicCoding](https://github.com/epsilon573/AutomateOlympicCoding).

#### Video Walkthrough
- [Youtube](https://www.youtube.com/watch?v=gg1cwWMnLhc)

### How to Setup :

Video Walkthrough just explains parsing test cases for a single problem. Contest Parser was added later.

- Install all the required dependencies.
- Clone the github repo
- Place the build file in Packages->User
- Place automate.py and contest.py in the same folder as your main cpp solution file
- In the latest version you don't need to rename anything, it will generate test cases with the same name as your working file

#### Parsing single problem :

- Open your cpp solution file ( must be in the same directory as automate and contest.py )
- Open the problem page on Chrome ( only works on chrome ) 
- Open sublime text and build using automate build system ( Ctrl + Shift + B)
- This plugin will create a test file with the same name as your solution file 
- Now just run your solution using FastOlympicCoding

#### Parsing a complete contest :

- Create a template.cpp file ( must be in the same directory as automate and contest.py ) .
- This file will be copied to all solution files when parsing the contest
- Open any cpp file in the same directory ( preferably template.cpp  )
- Open the contest page on Chrome ( only works on chrome ) 
- Open sublime text and build using automate-contest build system ( Ctrl + Shift + B)
- This plugin will create a directory with the contest ID and it will contain cpp files for all problems with template copied into them and corresponding test files will be parsed with them.
- Just open them and start solving.
- Now just run your solution using FastOlympicCoding

### Dependencies :

- Install Python3.
- pip install bs4
- pip install pywinauto 

You can support me on my Youtube Channel here : [GGxEpsilon](https://www.youtube.com/c/GGxEpsilon)

Support for more platforms like CodeChef and Atcoder will be added soon.

Thanks for reading and feedback will be appreciated.
