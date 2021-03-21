# Kanban Board 
A Kanban board is a simple form of task management. Every task that you add can be in one of three states:
- To Do
- Doing
- Done

## User Stories
The following functionalities are completed:

- [x] User can create a new item in the "To do" state.
- [x] User can delete an item when it is done.
- [x] User can move any item from any state ("To do", "Doing", or "Done") to any other state.


#### App Walkthrough GIF
Here's a walkthrough of implemented user stories:
<img src='http://g.recordit.co/UOm6wNzYkC.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />
          
## Requirements
`$ brew install python3`

## How to run the app

```
$ pip3 install virtualenv
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ export FLASK_APP=app.py
$ flask run
```

If you use Windows, to activate virtual environment:

`$ venv\Scripts\activate`

## Unit tests
To run unit tests:

```$ python3 -m venv venv_unit
$ source venv_unit/bin/activate
$ pip3 install -r requirements.txt
$ export DATABASE_URL='sqlite:///tasks.db'
$ python3 tests.py```
