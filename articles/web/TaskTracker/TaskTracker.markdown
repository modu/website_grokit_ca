
# Task Tracker: A Motivator To Do Useful Tasks Everyday

This small program (should) be a reminder and motivator to do a few tasks _at least x times a week_.

## How It Works

Go to where the .py files were unzipped, then enter:

    python enter_task.pye
    
You will get the following printed to the console:
    
    Top times:
    Global grand total: 0.0

    Done today:
    Total times today:
      {}
    Today grand total:  0.0
    --------------------------------------------------------------------------------

    listStatTaskBoard: usefultask
    Statistics for task 'usefultask' during the last 30 days:
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    Score: 0.0
    listStatTaskBoard: usefultask2
    Statistics for task 'usefultask2' during the last 30 days:
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    Score: 0.0
    Name?

The enter the name of the task you just did, the amount of time it took and any comment for record-keeping. This will build a database (TaskDoneList_DB.xml) of the tasks you have done. The last section after the separation (---) lists the current task **you should currently be focusing on doing everyday**. You well get a score attributed depending on how consistently you have been doing your tasks in the last 30 days (a 'X' means not done, and 'O' means done).

**Note that the time is kept in a decimal format. This means that 0.25 = 15 min, 1.0 = 1 hour, 1.75 = 1 hour 45 minutes.**

## Example of Use

First, modify the 'enter_task.pye' in order to reflect the tasks you might want to track. The initial file will look someting like that:

    import task_tracker

    import time

    if __name__ == '__main__':
      task_tracker.listTasks()
      
      task_tracker.listStatTaskBoard('usefultask')
      task_tracker.listStatTaskBoard('usefultask2')
      
      task_tracker.enterTask()
      print("All done, keep up the good work! :)")
      time.sleep(1)

Customize the __task_tracker.listStatTaskBoard('taskname') lines. Here is my personal file to give you an idea:

    import task_tracker

    import time

    if __name__ == '__main__':
      task_tracker.listTasks()
      
      task_tracker.listStatTaskBoard('jap')
      task_tracker.listStatTaskBoard('exer')
      task_tracker.listStatTaskBoard('book')
      
      task_tracker.enterTask()
      print("All done, keep up the good work! :)")
      time.sleep(1)

You can see that I am currently focusing on: {jap, exer, book}. This means that I have to exercise everyday, do my [Japanese kanji exercises](http://www.readthekanji.com) and spend time reading a book on my _to read stack_. Once I execute the program with:
      
    python enter_task.pye

I get the following:

    Top times:
      biomed:      29.53
      jap:         18.68
      nback:        6.28
      prog:         6.05
      finance:       4.0
    Global grand total: 76.19

    Done today:
    Name: exer
      time: 0.25
      at: 2010-12-30 14:56
      comment(s): short jog montmo

    Name: book
      time: 1.0
      at: 2010-12-30 15:38
      comment(s): GTD chapt 3. read + notes

    Name: jap
      time: 0.5
      at: 2010-12-30 16:04
      comment(s):

    Total times today:
      {'book': 1.0, 'exer': 0.25, 'jap': 0.5}
    Today grand total:  1.75
    ------------------------------------------------------------------

    listStatTaskBoard: jap
    Statistics for task 'jap' during the last 30 days:
        OXOOXXXXXXXXXXXXXXXXXXXXXXXXX
    Score: 0.103448275862
    listStatTaskBoard: exer
    Statistics for task 'exer' during the last 30 days:
        OOOXXXXXXXXXXXXXXXXXXXXXXXXXX
    Score: 0.103448275862
    listStatTaskBoard: book
    Statistics for task 'book' during the last 30 days:
        OXOXXXXXXXXXXXXXXXXXXXXXXXXXX
    Score: 0.0689655172414    

I am ashamed to admit that I recently fell off the wagon (was too busy with school last semester) since I only get 'good marks' (__O__s) in the last 3 days. Overtime I aim for 71% or japanese (every workday), 43% for exercise (3 times a week) and  57% for book reading (4 times a week).

## Database Format

The program keeps track of your tasks in a simple .xml file in the program's directory. Here is a subset of my database file.

      #TaskDoneList_DB.xml
      #[....] lots of more stuff before
	    <TaskDone>
		    <Name>
			    exer
		    </Name>
		    <CreationTime>
			    2010-12-30 14:56
		    </CreationTime>
		    <TimeSpent>
			    0.25
		    </TimeSpent>
		    <Comments>
			    short jog montmo
		    </Comments>
	    </TaskDone>
	    <TaskDone>
		    <Name>
			    book
		    </Name>
		    <CreationTime>
			    2010-12-30 15:38
		    </CreationTime>
		    <TimeSpent>
			    1.0
		    </TimeSpent>
		    <Comments>
			    GTD chapt 3. read + notes
		    </Comments>
	    </TaskDone>
	    <TaskDone>
		    <Name>
			    jap
		    </Name>
		    <CreationTime>
			    2010-12-30 16:04
		    </CreationTime>
		    <TimeSpent>
			    0.5
		    </TimeSpent>
		    <Comments/>
	    </TaskDone>
    </TaskDoneList>

## End Note

Have fun and be productive!
    
## Download, Install and Source Code

Download and unpack [the zip file](../../static/task_track.zip) to a folder. Run 'enter_task.pye' with python 2.7 or 3.1.

