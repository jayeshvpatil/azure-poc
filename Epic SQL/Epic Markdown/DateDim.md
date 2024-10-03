## Table: DateDim
### Table Description
The date dimension contains information about dates. Each row represents a date.The dimension supports dates from January 1, 0001 to December 30, 9999.
### Table Columns
* __DateKey__: integer. Surrogate key used to uniquely identify the record. The value is the combination of the four-digit year from 0001 to 9999, the two-digit month from 01 to 12, and the two-digit day from 01 to 31.. 
* __DateValue__: date. Value in date format. 
* __DisplayString__: string. Display string for the date formatted by the configuration settings. 
* __EpicDte__: integer. Number of days since December 31, 1840 for the date. This column will be NULL for dates earlier than December 31, 1840 and dates later than September 27, 2173.. 
* __EpicDat__: integer. Epic contact date sequence number for the date. The value is 121,531 minus the number of days since December 31, 1840. This column will be NULL for dates earlier than December 31, 1840 and dates later than September 27, 2173.. 
* __EpicInstantAtMidnight__: integer. The point in time for midnight of the date.The value is the number of seconds since midnight on December 31, 1840. This column will be NULL for dates earlier than December 31, 1840.. 
* __DayOfWeek__: string. Name of the day of the week. 
* __DayOfWeekAbbreviation__: string. Abbreviated name of the day of the week. 
* __IndexDayOfWeek__: integer. Number of the day of the week for the date from 1 to 7. The first day of the week is set in the configuration settings. 
* __DayOfMonth__: integer. Number of the day of the month for the date from 1 to 31. 
* __OccurrenceInMonth__: integer. Number of times the day of the week has occurred in the month for the date from 1 to 5. 
* __DayOfYear__: integer. Number of the day of the year for the date from 1 to 366. 
* __Weekend__: integer. 1/0 column that indicates whether the date is on a weekend. This column returns 1 if the date is on a weekend and 0 if the date is on a weekday.. 
* __IsWeekendIncludingFriday__: integer. 1/0 column that indicates whether the date is on a weekend. This column returns 1 if the date is on a weekend and 0 if the date is on a weekday. Here, weekend is defined as Friday, Saturday, and Sunday.. 
* __IsHoliday__: integer. 1/0 column that indicates whether the date is a recognized holiday. This column returns 1 if the date is a holiday and 0 if the date isn't a holiday. This column is based entirely on DATE_DIMENSION.HOLIDAY_YN in Clarity.. 
* __IsDayBeforeHoliday__: integer. 1/0 column that indicates whether the date is the day before a recognized holiday. This column returns 1 if the date is the day before a holiday and 0 if the date isn't a day before a holiday.. 
* __IsDayAfterHoliday__: integer. 1/0 column that indicates whether the date is the day after a recognized holiday. This column returns 1 if the date is the day after a holiday and 0 if the date isn't a day after a holiday.. 
* __LastFridayDate__: date. Date of the Friday prior to the date. If the date is a Friday, this column holds that date value. This column will be NULL for dates earlier than January 5, 1753.. 
* __TomorrowDate__: date. The day following the date. 
* __WeekNumber__: integer. Number of the week since the beginning of the year for the date from 1 to 54. 
* __IsoWeekNumber__: integer. Number of the week since the beginning of the year for the date as defined by the International Organization for Standardization (ISO). 
* __WeekYear__: string. String containing the concatenation of the two-digit week number, a space, and the four-digit year. 
* __IsoWeekYear__: string. String containing the concatenation of the two-digit week number, a space, and the four-digit year as defined by the International Organization for Standardization (ISO). 
* __WeekStartDate__: date. Date of the first day of the week for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __WeekEndDate__: date. Date of the last day of the week for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __MonthName__: string. Name of the month for the date. 
* __MonthNameAbbreviation__: string. Abbreviated name of the month for the date. 
* __MonthNumber__: integer. Number of the month of the year for the date from 1 to 12. 
* __MonthYear__: string. String containing the concatenation of the two-digit month, a space, and the four-digit year. 
* __FormattedMonthYear__: string. String containing the concatenation of the month name, a space, and the four-digit year. 
* __MonthStartDate__: date. Date of the first day of the month for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __MonthEndDate__: date. Date of the last day of the month for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __FiscalMonth__: integer. Fiscal month of the year for the date from 1 to 12. This column will be NULL for fiscal dates that are earlier than January 1, 1753 or later than December 31, 9999.. 
* __QuarterNumber__: integer. Number of the quarter for the date from 1 to 4. 
* __FormattedQuarterNumber__: string. String containing the concatenation of "Q" and the number of the quarter for the date. 
* __QuarterYear__: string. String containing the concatenation of the one-digit quarter, a space, and the four-digit year. 
* __FormattedQuarterYear__: string. String containing the concatenation of the two-digit quarter (Q + quarter number), a space, and the four-digit year. 
* __QuarterStartDate__: date. Date of the first day of the quarter for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __QuarterEndDate__: date. Date of the last day of the quarter for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __FiscalQuarter__: integer. Fiscal quarter of the year for the date from 1 to 4. This column will be NULL for fiscal dates that are earlier than January 1, 1753 or later than December 31, 9999.. 
* __Year__: integer. Year for the date from 0001 to 9999. 
* __YearWeek__: string. String containing the concatenation of the four-digit year, a space, and the two-digit week number. 
* __IsoYearWeek__: string. String containing the concatenation of the four-digit year, a space, and the two-digit week number as defined by the International Organization for Standardization (ISO). 
* __YearMonth__: string. String containing the concatenation of the four-digit year and the two-digit month. 
* __YearFormattedMonth__: string. String containing the concatenation of the four-digit year, a space, and the month name. 
* __YearQuarter__: string. String containing the concatenation of the four-digit year, a space, and the one-digit quarter. 
* __YearFormattedQuarter__: string. String containing the concatenation of the four-digit year, a space, and the two-digit quarter (Q + quarter number). 
* __YearStartDate__: date. Date of the first day of the year for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __YearEndDate__: date. Date of the last day of the year for the date. This column will be NULL for dates earlier than January 1, 1753.. 
* __PreviousYearDate__: date. Date one year prior to the date. This column will be NULL for dates earlier than January 1, 1754.. 
* __NextYearDate__: date. Date one year after the date. 
* __FiscalYear__: integer. Fiscal year for the date from 1753 to 9999. This column will be NULL for fiscal dates that are earlier than January 1, 1753 or later than December 31, 9999.. 