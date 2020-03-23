'''
Task manager script

This script is the procedure that manages my daily tasks. It will look in my
task folder for the most recent day. It will search this document for all 
tasks. Tasks that are marked as 'completed' will be removed and added to the
file for completed tasks. For all other tasks, it will copy these into the
new day's file.

03/02/2020
Jacob Ferraiolo
'''

import os
import time
import logging
import sys

logger = logging.getLogger('daily')
logger.setLevel(logging.DEBUG)


os.chdir('C:/users/e144483/productivity/productivity-tools')


# Grab the most recent daily task
most_recent_daily = sorted(os.listdir('daily'), reverse = True)[0]
most_recent_daily = '20200301.txt'
text = open('daily/'+most_recent_daily, 'r')


# Create today's daily 
datekey_today = time.strftime('%Y%m%d')
if os.path.isfile('daily/' + datekey_today+'.txt'):
    print(datekey_today + '.txt '+ 'already exists')
    logger.info('Process was ended early because file ' + datekey_today 
                + ' already exists')
    sys.exit('Process finished early because the date was already created')
else:
    todays_file = open('daily/'+datekey_today+'.txt', 'w')
    

completed_tasks = open('completed_tasks/completed_tasks.txt', 'a+')

# iterate through the previous daily for tasks that should be added to the new
# file
for line in text.readlines():
    if (line.find('done') or line.find('completed')) == -1:
        todays_file.write(line)
    else:
        new_line = datekey_today + ' ' +line
        completed_tasks.write(new_line)
        

print(datekey_today + '.txt successfully created')
todays_file.close()
completed_tasks.close()