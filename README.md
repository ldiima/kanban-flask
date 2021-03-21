## Kanban
A Kanban board is a simple form of task management. Every task that you add can be in one of three states:
- To Do
- Doing
- Done

This Kanban application:

- [x] Creates a new item in the "To do" state.
- [x] Delete an item when it is done.
- [x] Move any item from any state ("To do", "Doing", or "Done") to any other state.


#### App Walkthrough GIF

<img src="http://g.recordit.co/UOm6wNzYkC.gif><br>
          
## Requirements
`$ brew install python3`

## How to run the app

1. Install virtual environment

`$ pip3 install virtualenv`

2. Create virtual environment

`$ python3 -m venv venv`

3. Activate virtual environment
`$ source venv/bin/activate`

If you use Windows:

`$ venv\Scripts\activate`

4. Install dependencies

`<$ pip3 install -r requirements.txt`

5. Start the server

`$ python3 app.py`

## Unit tests
To run unit tests:
```$ python3 -m venv venv_unit
$ source venv_unit/bin/activate
$ pip3 install -r requirements.txt
$ export DATABASE_URL='sqlite:///tasks.db'
$ python3 tests.py
