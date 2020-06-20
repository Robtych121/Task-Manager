# Task Manager Project
This project came about after experiencing alot of issues with Microsoft To-Do. I decided to see if I could make a working web app using Django/Python to make a replacement.

This app allows people to log into an secure area, create lists and share them with other users that are registered and assign permissions (like certain people can edit the list but others cant).

You can view a copy of this project by clicking here: [Click Here](https://rd-task-manager.herokuapp.com/)


## UX Interface
The app has been designed to be used on all devices using the Bootstrap framework.

## Features
The current list of features are as follows:
1. Whole app is completely locked down
2. Only admins can create new users
3. Create new lists and share them with others
4. Create tasks against lists
5. Can view personal dynamic lists like assigned to me, due today, overdue tasks
6. Able to create grouped task lists


### Future plans
1. Alerts when a task is completed to the list owner.

## Technology Used
The following technologies were used as part of this project:
### Front End
1. HTML5 - This was used to structure the website
2. CSS3 - This was used to provide styling to the website
3. Bootstrap - This was used to help keep the forms in the same format/style and also to help with making it mobile ready
4. Fontawesome - This was used to create the icons in the footer
5. jQuery/JavaScript - Custom JS scripts were used in a few places to help with the functionality of the website

### Back End
1. PostreSQL - This was used as my main data store for all the information.
2. SQLite3 - This is used as my local data store while testing the application locally on my machine
3. Python 3 With Django - This was used for the backend logic and routing of the pages, this also is what entered the information into PostreSQL
4. AWS S3 - This was used as asset storage since I am using file uploads and needed a place that wouldn't be cleaned daily.