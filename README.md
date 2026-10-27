# Task_Tracker
Menu-based Python Task Tracker that stores tasks in a JSON file and can reload the saved tasks when run again.


# Mini Task Tracker

A menu-based Python task tracker that stores tasks in `tasks.json`. Tasks are
loaded when the program starts and saved whenever one is added, completed, or
deleted.

## Features

- Add tasks with a non-empty title; new tasks start as Pending.
- View a numbered list of tasks with Pending or Done status.
- Mark a task as complete or delete it by its number.
- Save and reload tasks in a JSON file.
- Handle a missing task file, blank titles, invalid menu choices, and invalid
  task numbers.

## Requirements

Python 3. No third-party packages are needed.

## Run

From the folder containing `mini_task_tracker.py`, run:

```bash
python mini_task_tracker.py
```

The program creates `tasks.json` in the current working directory the first
time a task is saved. On later runs, it loads the saved tasks automatically.

