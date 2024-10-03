## Table: VisitFact
### Table Description
The visit fact contains information about visits. Each row represents a visit encounter.For Epic data, the fact includes appointment records as well as records with encounter types configured in Chronicles as face-to-face. The full list of encounter types is displayed in Component Configuration.
### Table Columns
* __VisitKey__: integer. Surrogate key used to uniquely identify the record. 
* __EncounterKey__: integer. Encounter associated with the visit. Links to EncounterFact table.
* __PatientKey__: integer. Patient associated with the visit. Links to PatientDim table.
* __PatientDurableKey__: integer. Patient associated with the visit. Links to PatientDim table.
* __PatientSourceDataDurableKey__: integer. Patient associated with the visit. Links to PatientDimSourceData table.
* __AgeKey__: integer. Patient age as of the encounter date. This value is calculated based on EncounterDateKey and the BirthDate column in PatientDim.. Links to DurationDim table.
* __ReferralKey__: integer. First referral associated with the visit. Links to ReferralFact table.
* __ClosedDateKey__: integer. Date when the encounter was closed. Links to DateDim table.
* __AppointmentDateKey__: integer. Date of the appointment. Links to DateDim table.
* __EncounterDateKey__: integer. Encounter date for the visit. Links to DateDim table.
* __AppointmentTimeOfDayKey__: integer. Time of day of the appointment. Links to TimeOfDayDim table.
* __AppointmentCreationDateKey__: integer. Date when the appointment was created. If an appointment was rescheduled, this is the date on which the new (rescheduled) appointment was created, not the creation date of the original appointment.. Links to DateDim table.
* __AppointmentCancellationDateKey__: integer. Date when the appointment was canceled. Links to DateDim table.
* __RescheduledVisitKey__: integer. Non-canceled appointment rescheduled from this visit. Links to VisitFact table.
* __CheckInDateKey__: integer. Date when the patient was checked in. Links to DateDim table.
* __CheckInTimeOfDayKey__: integer. Time of day when the patient was checked in. Links to TimeOfDayDim table.
* __RoomedDateKey__: integer. Date when the patient was roomed. Links to DateDim table.
* __RoomedTimeOfDayKey__: integer. Time of day when the patient was roomed. Links to TimeOfDayDim table.
* __CheckOutDateKey__: integer. Date when the patient was checked out. Links to DateDim table.
* __CheckOutTimeOfDayKey__: integer. Time of day when the patient was checked out. Links to TimeOfDayDim table.
* __DepartmentKey__: integer. Department for the visit. For Epic data, if there are multiple departments for the visit, this is the first department on the list.. Links to DepartmentDim table.
* __PrimaryDiagnosisKey__: integer. Primary encounter diagnosis for the visit. Links to DiagnosisDim table.
* __EncounterDiagnosisComboKey__: integer. All encounter diagnoses for the visit. Links to DiagnosisBridge table.
* __EncounterDiagnosisComboIdTypeId__: integer. The IdTypeId corresponding to the DiagnosisBridge lookup. 
* __EncounterDiagnosisNumericId__: number. The NumericId corresponding to the DiagnosisBridge lookup. If this column is populated, then EncounterDiagnosisComboId will not be populated. Cannot and should not be populated by packages.. 
* __EncounterDiagnosisComboId__: string. The Id corresponding to the DiagnosisBridge lookup. 
* __PrimaryVisitProviderKey__: integer. Primary visit provider for the visit. Links to ProviderDim table.
* __PrimaryVisitProviderDurableKey__: integer. Primary visit provider for the visit. Links to ProviderDim table.
* __PrimaryVisitProviderSourceDataDurableKey__: integer. Primary visit provider for the visit. Links to ProviderDimSourceData table.
* __SecondVisitProviderKey__: integer. Second visit provider for the visit. Links to ProviderDim table.
* __SecondVisitProviderDurableKey__: integer. Second visit provider for the visit. Links to ProviderDim table.
* __SecondVisitProviderSourceDataDurableKey__: integer. Second visit provider for the visit. Links to ProviderDimSourceData table.
* __ThirdVisitProviderKey__: integer. Third visit provider for the visit. Links to ProviderDim table.
* __ThirdVisitProviderDurableKey__: integer. Third visit provider for the visit. Links to ProviderDim table.
* __ThirdVisitProviderSourceDataDurableKey__: integer. Third visit provider for the visit. Links to ProviderDimSourceData table.
* __FourthVisitProviderKey__: integer. Fourth visit provider for the visit. Links to ProviderDim table.
* __FourthVisitProviderDurableKey__: integer. Fourth visit provider for the visit. Links to ProviderDim table.
* __FourthVisitProviderSourceDataDurableKey__: integer. Fourth visit provider for the visit. Links to ProviderDimSourceData table.
* __IsContinuityOfCare__: integer. 1/0 column that indicates whether the patient was seen by their own care team. This column returns 1 if the patient was seen by a provider on their care team and 0 if the patient wasn't.. 
* __PrimaryResourceKey__: integer. Scheduled resource for the visit. Links to ResourceDim table.
* __LevelOfServiceKey__: integer. Primary level of service associated with the visit. Links to ProcedureDim table.
* __LevelOfServiceDurableKey__: integer. Primary level of service associated with the visit. Links to ProcedureDim table.
* __LevelOfServiceAuthorizedByProviderKey__: integer. Provider who authorized the level of service for the visit. Links to ProviderDim table.
* __LevelOfServiceAuthorizedByProviderDurableKey__: integer. Provider who authorized the level of service for the visit. Links to ProviderDim table.
* __LevelOfServiceAuthorizedByProvSourceDataDurableKey__: integer. Provider who authorized the level of service for the visit. Links to ProviderDimSourceData table.
* __EncounterClosedByProviderKey__: integer. Provider who closed the encounter. Links to ProviderDim table.
* __EncounterClosedByProviderDurableKey__: integer. Provider who closed the encounter. Links to ProviderDim table.
* __EncounterClosedByProviderSourceDataDurableKey__: integer. Provider who closed the encounter. Links to ProviderDimSourceData table.
* __GuarantorKey__: integer. Guarantor associated with the visit. Links to GuarantorDim table.
* __GuarantorDurableKey__: integer. Guarantor associated with the visit. Links to GuarantorDim table.
* __CoverageKey__: integer. Coverage for the visit. For Epic data, this column stores the primary coverage on the associated hospital account if it is available. Otherwise it stores the original coverage on the first non-voided professional transaction if it is available. Otherwise it stores the coverage assigned at check-in or appointment entry.. Links to CoverageDim table.
* __EncounterType__: string. Encounter type for the visit. For Epic data, hospital outpatient visits are indicated by a type of Hospital Encounter.. 
* __VisitType__: string. Visit type for the visit. 
* __VisitTypeEpicId__: string. Epic ID of the visit type (PRC) record for the visit. The column is blank for visits associated with Home Health (LCT) records.. 
* __TelehealthMode__: string. Telehealth mode associated with the visit. 
* __FinancialClass__: string. This column should no longer be used and will be removed in a future version. As a replacement, use CoverageDim.PayorFinancialClass.. 
* __AppointmentStatus__: string. Status of the appointment. 
* __SystolicBloodPressure__: integer. Patient systolic blood pressure for the visit. 
* __AppointmentConfirmationStatus__: string. Confirmation status of the appointment. 
* __AuthorizationStatus__: string. The authorization status of the visit, determined by evaluating all the authorizations linked to the visit. 
* __AppointmentLengthInMinutes__: integer. Length of the scheduled appointment in minutes. 
* __AppointmentLeadTimeInDays__: integer. Number of days from the appointment creation date to the appointment date. By default, this is calculated from AppointmentCreationDate and AppointmentInstant.. 
* __SchedulingSource__: string. Source that performed the initial scheduling action on this appointment. 
* __IsNewToFacility__: integer. 1/0 column that indicates whether the patient was new to the facility. This column returns 1 if the patient was new to the facility and 0 if the patient wasn't new to the facility.. 
* __IsNewToServiceArea__: integer. 1/0 column that indicates whether the patient was new to the service area. This column returns 1 if the patient was new to the service area and 0 if the patient wasn't new to the service area.. 
* __IsNewToRevenueLocation__: integer. 1/0 column that indicates whether the patient was new to the revenue location. This column returns 1 if the patient was new to the revenue location and 0 if the patient wasn't new to the revenue location.. 
* __IsNewToDepartment__: integer. 1/0 column that indicates whether the patient was new to the department. This column returns 1 if the patient was new to the department and 0 if the patient wasn't new to the department.. 
* __IsNewToSpecialty__: integer. 1/0 column that indicates whether the patient was new to the specialty. This column returns 1 if the patient was new to the specialty and 0 if the patient wasn't new to the specialty.. 
* __IsNewToProvider__: integer. 1/0 column that indicates whether the patient was new to the provider. This column returns 1 if the patient was new to the provider and 0 if the patient wasn't new to the provider.. 
* __ReasonAppointmentCanceled__: string. Reason for the appointment cancellation, if the appointment was canceled. 
* __CancellationLeadTimeInDays__: integer. Number of days between the date on which the appointment was canceled and the date of the appointment. 
* __CancellationInitiator__: string. Name of the cancel initiator associated with an appointment cancel reason. 
* __NoShowPredictedProbability__: number. The most recent percent likelihood the appointment will result in being a no-show appointment. 
* __EncounterEpicCsn__: number. Epic contact serial number (CSN) of the visit. This column identifies patient (EPT) contacts.. 
* __AppointmentSerialNumber__: number. The appointment serial number for the appointment. This value is unique among appointments that are not canceled, and can be used to group together canceled and rescheduled appointments.. 
* __HospitalAccountEpicId__: number. Epic ID of the hospital account associated with the visit. This column identifies account (HAR) records.. 
* __PrimaryProfessionalAccountEpicId__: number. Epic ID of the primary professional account associated with the visit. This column identifies account (HAR) records.. 
* __MinutesToRoom__: integer. Number of minutes from the check-in time to the roomed time. By default, this is calculated from CheckInInstant and RoomedInstant.. 
* __MinutesInRoom__: integer. Number of minutes from the roomed time to the check-out time. By default, this is calculated from RoomedInstant and VisitEndInstant.. 
* __SecondsWaitingToBeRoomed__: integer. Number of seconds the patient spent waiting after check in before being roomed. 
* __SecondsWithNurse__: integer. Number of seconds the patient spent in the exam room with the nurse. 
* __SecondsWaitingForPhysician__: integer. Number of seconds the patient spent in the exam room waiting for the physician after the nurse left the room. 
* __SecondsWithPhysician__: integer. Number of seconds the patient spent in the exam room with the physician. 
* __SecondsSpentPreCharting__: integer. Number of seconds the physician spent pre-charting prior to the visit. 
* __SecondsSpentPostCharting__: integer. Number of seconds the physician spent charting after the visit. 
* __Height__: string. This column should no longer be used and will be removed in a future version. It has been replaced by HeightInInches.
Patient height for the visit. For Epic data, indicators for feet and/or inches might be included.. 
* __HeightInCentimeters__: number. Patient height in centimeters for the visit. For Epic data, values are only included if the Clarity data is in the format (#' #") and below 9 feet and 12 inches.. 
* __HeightInInches__: number. Patient height in inches for the visit. For Epic data, values are only included if the Clarity data is in the format (#' #") and below 9 feet and 12 inches.. 
* __WeightInOunces__: number. Patient weight in ounces for the visit. 
* __WeightInGrams__: number. Patient weight in grams for the visit. 
* __BodyMassIndex__: number. Patient body mass index for the visit. 
* __BodyMassIndexPercentile__: number. Patient body mass index percentile for the visit. 
* __BodyMassIndexPercentileGrowthChart__: string. Growth chart used for the patient's body mass index percentile calculation. 
* __BodySurfaceArea__: number. Patient body surface area for the visit. 
* __DiastolicBloodPressure__: integer. Patient diastolic blood pressure for the visit. 
* __TemperatureInFahrenheit__: number. Patient temperature in Fahrenheit for the visit. 
* __TemperatureInCelsius__: number. Patient temperature in Celsius for the visit. 
* __PulseRate__: integer. Patient pulse rate for the visit. 
* __RespirationRate__: integer. Patient respiration rate for the visit. 
* __TotalCost__: number. Total cost associated with the visit. 
* __DirectCost__: number. Direct cost associated with the visit. 
* __IndirectCost__: number. Indirect cost associated with the visit. 
* __FixedCost__: number. Fixed cost associated with the visit. 
* __VariableCost__: number. Variable cost associated with the visit. 
* __DirectFixedCost__: number. Direct fixed cost associated with the visit. 
* __DirectVariableCost__: number. Direct variable cost associated with the visit. 
* __IndirectFixedCost__: number. Indirect fixed cost associated with the visit. 
* __IndirectVariableCost__: number. Indirect variable cost associated with the visit. 
* __LaborDirectCost__: number. Direct labor cost associated with the visit. 
* __LaborDirectFixedCost__: number. Direct fixed labor cost associated with the visit. 
* __LaborDirectVariableCost__: number. Direct variable labor cost associated with the visit. 
* __SuppliesCost__: number. Supplies cost associated with the visit. 
* __OtherDirectCost__: number. Direct other cost associated with the visit. 
* __OtherDirectFixedCost__: number. Direct fixed other cost associated with the visit. 
* __OtherDirectVariableCost__: number. Direct variable other cost associated with the visit. 
* __CopayDue__: number. Amount of copay that was due. 
* __CopayCollected__: number. Amount of copay that was collected. 
* __PrepaymentDue__: number. Amount of prepayment that was due. 
* __PrepaymentCollected__: number. Amount of prepayment that was collected. 
* __PortalReasonForVisit__: string. The reason for visit associated with the visit. For Epic data, this column is populated only for visits scheduled online.. 
* __OnlineCheckinStatus__: string. The status of electronic check-in for the visit. 
* __DaysSavedByAutoWaitList__: integer. Number of days between the patient's original appointment time and the patient's actual appointment time when the appointment was scheduled using auto wait list functionality. 
* __SecondsToRespondToAutoWaitListOffer__: integer. When the appointment was scheduled using auto wait list functionality, the number of seconds between the time a new appointment was offered and the time the appointment was accepted. 
* __MinutesOfExcessWaitTime__: integer. Number of minutes above the estimated wait time that the patient spent waiting to be roomed. 
* __MarkedSelfPay__: integer. 1/0 column that indicates whether the visit is marked as Self Pay. This column returns 1 if the visit encounter is marked as Self Pay and 0 if it wasn't.. 
* __MarkedDoNotBillInsurance__: integer. 1/0 column that indicates whether the visit is marked as Do Not Bill Insurance. This column returns 1 if the visit encounter is marked as Do Not Bill Insurance and 0 if it wasn't.. 
* __Closed__: integer. 1/0 column that indicates whether the visit encounter is closed. This column returns 1 if the visit encounter is closed and 0 if the visit encounter is open.. 
* __Complete__: integer. 1/0 column that indicates whether the appointment is complete. This column returns 1 if the appointment is complete and 0 if the appointment isn't complete.. 
* __WalkIn__: integer. 1/0 column that indicates whether the visit encounter is a walk-in. This column returns 1 if the visit encounter is a walk-in and 0 if the visit encounter isn't a walk-in.. 
* __IsFaceToFace__: integer. 1/0 column that indicates whether the encounter is an outpatient face-to-face visit. This column returns 1 if the encounter is an outpatient face-to-face visit and 0 otherwise.. 
* __IsScheduledAppointment__: integer. 1/0 column that indicates whether this is a scheduled appointment. This column returns 1 if this is a scheduled appointment and 0 if this is not a scheduled appointment.. 
* __IsSameDayAppointment__: integer. 1/0 column that indicates whether the appointment was a same-day appointment. This column returns 1 if the appointment was a same-day appointment and 0 if the appointment wasn't a same-day appointment.. 
* __IsSameDayCancel__: integer. 1/0 column that indicates whether the appointment was canceled on the same day it was scheduled to occur. This column returns 1 if the appointment was canceled on the same day and 0 if the appointment wasn't canceled on the same day.. 
* __IsLateCancel__: integer. 1/0 column that indicates whether the appointment was canceled late. This column returns 1 if the appointment was canceled late and 0 if the appointment wasn't canceled late.. 
* __ReferralRequired__: integer. 1/0 column that indicates whether a referral is required for the visit. This column returns 1 if a referral is required and 0 if a referral isn't required.. 
* __TobaccoUseReviewed__: integer. 1/0 column that indicates whether the patient's tobacco use was reviewed during the visit. This column returns 1 if the patient's tobacco use was reviewed and 0 if the patient's tobacco use wasn't reviewed.. 
* __MedicationsReviewed__: integer. 1/0 column that indicates whether the patient's medications were reviewed during the visit. This column returns 1 if the patient's medications were reviewed and 0 if the patient's medications weren't reviewed.. 
* __ProblemListReviewed__: integer. 1/0 column that indicates whether the patient's problem list was reviewed during the visit. This column returns 1 if the patient's problem list was reviewed and 0 if the patient's problem list wasn't reviewed.. 
* __AvsPrinted__: integer. 1/0 column that indicates whether the after visit summary (AVS) was printed for the visit. This column returns 1 if the AVS was printed and 0 if the AVS wasn't printed.. 
* __AllergiesReviewed__: integer. 1/0 column that indicates whether the patient's allergies were reviewed during the visit. This column returns 1 if allergies were reviewed and 0 if allergies weren't reviewed.. 
* __ScheduledOnline__: integer. 1/0 column that indicates whether the visit was scheduled online. This column returns 1 if the visit was scheduled online and 0 if the visit wasn't scheduled online.. 
* __PortalActiveAtScheduling__: integer. 1/0 column that indicates whether the patient's portal account was active at the time the visit was scheduled. This column returns 1 if the patient's portal account was active at the time the visit was scheduled and 0 ifthe patient's portal account wasn't active at the time the visit was scheduled.. 
* __ScheduledFromTicket__: integer. 1/0 column that indicates whether the visit was scheduled from a ticket. This column returns 1 if the visit was scheduled from a ticket and 0 if the visit wasn't scheduled from a ticket.. 
* __OnlineCheckinAvailable__: integer. 1/0 column that indicates whether online check-in was available for the visit. This column returns 1 if online check-in was available and 0 if online check-in wasn't available.. 
* __CheckedInWithKiosk__: integer. 1/0 column that indicates whether the visit was checked in via a kiosk. This column returns 1 if the visit was checked in via a kiosk and 0 if the visit wasn't checked in via a kiosk.. 
* __IsWithPCP__: integer. 1/0 column that indicates whether the primary provider for the visit was the patient's PCP at the time of the visit. The column returns 1 if the primary provider for the visit was the patient's PCP and 0 otherwise.. 
* __SelfArrivalAllowed__: integer. 1/0 column that indicates whether this visit supports self-arrival. This column returns 1 if some type of self-arrival is supported, and 0 if not.. 
* __SelfArrivalType__: string. Indicate what type(s) of self-arrival, if any, this visit support. 
* __Count__: integer. Artificial measure on which calculations can be done. The value is 0 for rows marked as deleted, 1 otherwise.. 
* ___CreationInstant__: date/time. The date and time the record was created. 
* ___LastUpdatedInstant__: date/time. The date and time the record was last updated. 
* ___IsInferred__: integer. 1/0 column that indicates whether the record is inferred. 
* ___IsDeleted__: integer. 1/0 column that indicates whether the record is deleted. 
* ___PrimaryPackageToImpactRecord__: string. The name of the primary package to impact the record. 
* ___MostRecentPackageToImpactRecord__: string. The name of the most recent package to impact the record. 
* ___NumberOfSources__: integer. The number of sources contributing to the record. 
* ___HasSourceClarity__: integer. 1/0 column that indicates whether the record is influenced by the Clarity source. 
* ___DeletedFromSourceClarity__: integer. 1/0 column that indicates whether the record is deleted from the Clarity source. 