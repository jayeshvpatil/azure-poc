## Table: TimeOfDayDim
### Table Description
The time of day dimension contains information about the time of day. Each row represents a minute in the day.
### Table Columns
* __TimeOfDayKey__: integer. Surrogate key used to uniquely identify the record. The value is the combination of the two digit hour from 00 to 23 and the two digit minute from 00 to 59.. 
* __TimeValue__: time. Value in time format. 
* __DisplayString24Hour__: string. Display string for the time in 24-hour notation. The value is the combination of the two-digit hour from 00 to 23, the string constant ":", and the two-digit minute from 00 to 59.. 
* __DisplayString12Hour__: string. Display string for the time in 12-hour notation. The value is the combination of the two-digit hour from 01 to 12, the string constant ":", the two-digit minute from 00 to 59, and one of the string constants "AM" or "PM".. 
* __HourNumber__: integer. Number of the hour for the time from 0 to 23. 
* __MinuteNumber__: integer. Number of the minute for the time from 0 to 59. 
* __DisplayStringHourStart24Hour__: string. Display string for the first minute of the hour this time is within in 24-hour notation. The value is the combination of the two-digit hour from 00 to 23 and the string constant ":00".. 
* __DisplayStringHourEnd24Hour__: string. Display string for the last minute of the hour this time is within in 24-hour notation. The value is the combination of the two-digit hour from 00 to 23 and the string constant ":59".. 
* __DisplayStringHourRange24Hour__: string. Display string for start and end range of the hour this time is within in 24-hour notation. The value is the combination of the two-digit hour from 00 to 23, the string constant ":00", the string constant " - ", two-digit hour from 00 to 23, and the string constant ":59".. 
* __DisplayStringHourStart12Hour__: string. Display string for the first minute of the hour this time is within in 12-hour notation. The value is the combination of the two-digit hour from 01 to 12, the string constant ":00", and one of the string constants "AM" or "PM".. 
* __DisplayStringHourEnd12Hour__: string. Display string for the first minute of the hour this time is within in 12-hour notation. The value is the combination of the two-digit hour from 01 to 12, the string constant ":59", and one of the string constants "AM" or "PM".. 
* __DisplayStringHourRange12Hour__: string. Display string for start and end range of the hour this time is within in 12-hour notation. The value is the combination of the two-digit hour from 01 to 12, the string constant ":00", one of the string constants "AM" or "PM", the string constant " - ", the two-digit hour from 01 to 12, the string constant ":59", and one of the string constants "AM" or "PM"..