import math;
import datetime;
import time;

# Normally I wouldn't comment this much if at all, but a requirement was to comment.
# If someone can read code, 85% of these comments are useless - aka this is over commented

evnt = input("Enter the name of the event: ");
day = input("Enter the day of your event, e.g. 1-31: ");
month = input("Enter the month of your event, e.g. 1-12: ");
year = input("Please enter the year of your event, e.g. 2022-2100: ");
# Requirement of no checking - We're to assume valid inputs.
# Easily enough fixed if we wanted to go through the process


# Setting up the date and current time values
timeDate = datetime.datetime(int(year), int(month), int(day)); # wow python, datetime.datetime... that's just.. just wow
currTime = datetime.datetime.now();


# Annnd converting those values to seconds since the epochalypse - And also getting the time difference
dateSeconds = time.mktime(timeDate.timetuple());
currSeconds = time.mktime(currTime.timetuple());
timeDifference = int(dateSeconds) - int(currSeconds); # We're not dealing with milliseconds, so converting these to ints is fine


# Converting the seconds to minutes, hours days and years
# Seconds
seconds = timeDifference % 60; 			# Seconds left over, should be no decimal remainder

# Minutes
minutesRAW = timeDifference / 60; 		# 60 Seconds in a minute
minutes = math.floor(minutesRAW % 60);

# Hours
hoursRAW = minutesRAW / 60; 			# 60 Minutes in an hour
hours = math.floor(hoursRAW % 24);

# Days
daysRAW = hoursRAW / 24; 				# 24 Hours in a day
days = math.floor(daysRAW % 365);

# Years
years = math.floor(daysRAW / 365); 		# We're not converting any higher, so this is just straight up years


# We gonna do some array magic here:
# We will not add any item to the array if its value is 0 (eg `15 days, 0 hours, 23 minutes` should simply display as `15 days, 23 minutes`)
# Then at the end, we'll join all the items in the array together as a singular string.
timeArray = [];
timeData = [[years, "year"], [days, "day"], [hours, "hour"], [minutes, "minute"], [seconds, "second"]];

def checkTimeInterval (num, word):
	"""
	Checks if time specific number is greater than 0,
	if so adds the item to an array.
	"""
	# Checking if the number should be added to an array;
	# If it should be, whether or not the 'word' should have an s on the end - eg: 1 hours vs 1 hour,  3 hours vs 3 hour
	# Since 0 values will not viewed, we don't have to worry about "0 seconds" vs "0 second"
	if(num > 0):
		if(num > 1): word += "s";
		timeArray.append(f"{num} {word}");


# Load the array
for t in timeData:
	checkTimeInterval(t[0], t[1]);


# If timeArray is greater than or equal to 2, grab the last 2 items and put an " and " between them
# Also removing said last 2 items from the array while we're at it
if(len(timeArray) >= 2):
	andSeperator = " and "
	andItem = andSeperator.join(timeArray[-2:]);

	del timeArray[-2:];
	timeArray.append(andItem);


# Join all the wibbly-wobbly timey-wimey stuff together
seperator = ", ";
timeString = seperator.join(timeArray);
date = f"{day}/{month}/{year}";
timeUntil = f"{evnt} is on {date} ({timeString} later)"; # Later should gramatically be changed to "away"


# Galifrey stands! I uh.. I mean we're done.
print(timeUntil);
