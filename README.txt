Casa Panto Church of Gainz Lifting App

Purpose:  Ongoing project to develop a workout app based on the lifting program I follow

Ideally I'd like to turn it into a mobile app, and the goal is to have it be user friendly,
and have all data stored on the device.  I'd eventually like to allow users to export their
data to a JSON or similar file so they can re-load it if they change devices.

Glidepath -
    - Working backend model on text readout
    - Develop simple GUI
    - Develop into web hosted application able to be accessed from web server
    - Develop into mobile app

Update 0.0.2
    Beginning to work on front end in Django
    Look into containerizing application (Kubernetes)
        - At minimum start tracking dependencies and create install script

Update 0.0.1-3
    Created functionality to import and save data from a JSON file
        -Included exception handling for no json present in directory

    Fixed bug with updating all maxes under settings


Update 0.0.1-2
    Fixed bug where sets failed to update when changeing phases

    Fixed bug in showMe() to force int input

Update 0.0.1-1
    Added functionality to change between phases of the program

    Need to implement exception handling for invalid inputs

    Need to develop functionality to save data between sessions so you don't need to re-enter
    your maxes every time you launch.


Release 0.0.1
    Limited functionality backend model.  If you run model.py in your terminal, it will ask 
    for your max weights in the major lifts, and calculate based on phase I of the program.

    Need to develop functionality to save data between sessions so you don't need to re-enter
    your maxes every time you launch.

    Need to develop functionality to change between phases of the program.