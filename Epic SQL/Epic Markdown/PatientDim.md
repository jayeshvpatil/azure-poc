## Table: PatientDim
### Table Description
The patient dimension contains information about patients. Each row represents a patient record for a date range.This table contains both current and historical information. For current records, IsCurrent has a value of 1. Historical records contain information that is valid for the date range specified by the StartDate and EndDate columns.
### Table Columns
* __PatientKey__: integer. Surrogate key used to uniquely identify the record. 
* __DurableKey__: integer. Durable key used to identify the record. 
* __ProblemComboKey__: integer, snapshot on data change. All active problems for the patient. This column will be changed in the future to have no change tracking (Type 1).. Links to DiagnosisBridge table.
* __ProblemComboIdTypeId__: integer, snapshot on data change. Source ID type to identify all active problems for the patient. 
* __ProblemNumericId__: number, snapshot on data change. The NumericId corresponding to the DiagnosisBridge lookup. If this column is populated, then ProblemComboId will not be populated. Cannot and should not be populated by packages.. 
* __ProblemComboId__: string, snapshot on data change. The Id corresponding to the DiagnosisBridge lookup. 
* __PrimaryCareProviderKey__: integer, snapshot on data change. Primary care provider for the patient. This column will be changed in the future to have no change tracking (Type 1).. Links to ProviderDim table.
* __PrimaryCareProviderDurableKey__: integer, snapshot on data change. Primary care provider for the patient. This column will be changed in the future to have no change tracking (Type 1).. Links to ProviderDim table.
* __PrimaryCareProviderSourceDataDurableKey__: integer, snapshot on data change. Primary care provider for the patient. This column will be changed in the future to have no change tracking (Type 1).. Links to ProviderDimSourceData table.
* __PatientRaceComboKey__: integer. All patient races for the patient. Links to PatientRaceBridge table.
* __PatientRaceComboIdTypeId__: integer. The IdTypeId corresponding to the PatientRaceBridge lookup. 
* __PatientRaceNumericId__: number. The NumericId corresponding to the PatientRaceBridge lookup. If this column is populated, then PatientRaceComboId will not be populated. Cannot and should not be populated by packages.. 
* __PatientRaceComboId__: string. The Id corresponding to the PatientRaceBridge lookup. 
* __PreliminaryCauseOfDeathDiagnosisKey__: integer. Preliminary cause of death for the patient. Links to DiagnosisDim table.
* __ConfirmationStatusComboKey__: integer. All confirmation statuses for the patient. Links to PatientConfirmationStatusBridge table.
* __ConfirmationStatusComboIdTypeId__: integer. The IdType ID corresponding to the PatientConfirmationStatusBridge lookup. 
* __ConfirmationStatusNumericId__: number. The NumericId corresponding to the PatientConfirmationStatusBridge lookup. If this column is populated, then ConfirmationStatusComboId will not be populated. Cannot and should not be populated by packages.. 
* __ConfirmationStatusComboId__: string. The Id corresponding to the PatientConfirmationStatusBridge lookup. 
* __AddressKey__: integer, snapshot on data change. Address for the patient's residence. Links to AddressDim table.
* __PatientEpicId__: string. Epic ID of the patient. This column identifies patient (EPT) records.. 
* __Name__: string. Full name of the patient. 
* __PreferredName__: string. Preferred name of the patient. 
* __FirstName__: string. First name of the patient. 
* __MiddleName__: string. Middle name of the patient. 
* __LastName__: string. Last name of the patient. 
* __Ssn__: string. Social Security number (SSN) for the patient. 
* __EnterpriseId__: string. Enterprise ID for the patient. 
* __PrimaryMrn__: string, snapshot on data change. Primary medical record number (MRN) for the patient. This column will be changed in the future to have no change tracking (Type 1).. 
* __Sex__: string. Sex of the patient. For Epic data, this is the legal sex of the patient as defined by a government body.. 
* __SexAssignedAtBirth__: string. Sex assigned at birth as determined by a medical or birthing professional. 
* __GenderIdentity__: string. Gender identity of the patient. 
* __PreferredLanguage__: string. Preferred language of the patient. 
* __Ethnicity__: string. Primary ethnicity of the patient. 
* __OmbEthnicity__: string. Ethnicity of the patient based on the standards of the Office of Management and Budget (OMB). 
* __FirstRace__: string. First race associated with the patient. 
* __SecondRace__: string. Second race associated with the patient. 
* __ThirdRace__: string. Third race associated with the patient. 
* __FourthRace__: string. Fourth race associated with the patient. 
* __FifthRace__: string. Fifth race associated with the patient. 
* __OmbRace__: string. Race of the patient based on the standards of the Office of Management and Budget (OMB). 
* __MultiRacial__: integer. 1/0 column that indicates whether the patient has more than one race. This column returns 1 if the patient has more than one race and 0 if the patient only has one race. For Epic data, the value may be incorrect if your organization documents both ethnicity and race in the same item.. 
* __AgeInYears__: integer. Patient's current age. The value is calculated based on the BirthDate and DeathDate columns.. 
* __BirthDate__: date. Birth date of the patient. 
* __DeathDate__: date. Death date of the patient. 
* __DeathInstant__: date/time. Date and time of the patient's death. 
* __DeathLocation__: string. Location of the patient's death. 
* __Status__: string. Status of the patient. For Epic data, this column can contain Alive, Deceased, or other values.. 
* __Address__: string, snapshot on data change. Street address for the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __City__: string, snapshot on data change. City of the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __County__: string, snapshot on data change. County of the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __StateOrProvince__: string, snapshot on data change. State or province of the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __StateOrProvinceAbbreviation__: string, snapshot on data change. Abbreviated name of the state or province of the patient's residence. This column will be changed in the future to have no change tracking (Type 1).. 
* __Country__: string, snapshot on data change. Country of the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __PostalCodeKey__: integer. Postal code of the patient's residence. Links to PostalCodeDim table.
* __PostalCode__: string, snapshot on data change. Postal code for the patient's residence. This column will be changed in the future to have no change tracking (Type 1). Use AddressHistoryFact for historical address information.. 
* __CensusTractKey__: integer. 2010 Census tract of the patient's residence. Links to CensusTractDim table.
* __CensusTractFipsCode__: string. Census tract of the patient's residence. 
* __Latitude__: number, snapshot on data change. This column should no longer be used and will be removed in a future version. It has been replaced by AddressDim.Latitude of the patient's residence.. 
* __Longitude__: number, snapshot on data change. This column should no longer be used and will be removed in a future version. It has been replaced by AddressDim.Longitude of the patient's residence.. 
* __HomePhoneNumber__: string. Home phone number for the patient. 
* __WorkPhoneNumber__: string. Work phone number for the patient. 
* __EmailAddress__: string. Email address of the patient. 
* __SexualOrientation__: string. Sexual orientation of the patient. For Epic data, this column will store a value indicating "other" if multiple values are entered for sexual orientation.. 
* __MaritalStatus__: string, snapshot on data change. Marital status of the patient. This column will be changed in the future to have no change tracking (Type 1).. 
* __Religion__: string. Religion for the patient. 
* __CountryOfOrigin__: string. The country in which a patient was born. 
* __IndigenousStatus__: string. Indicates whether a patient is considered indigenous. 
* __SmokingStatus__: string, snapshot on data change. Smoking status of the patient. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimaryFinancialClass__: string, snapshot on data change. This column should no longer be used and will be removed in a future version. As a replacement, use CoverageDim.CoverageFinancialClass. This column will be changed in the future to have no change tracking (Type 1).. 
* __HighestLevelOfEducation__: string. Highest level of education completed by the patient. 
* __ResearchContactPreference__: string. The patient's explicit response to whether they want to be contacted about research studies. 
* __MyChartStatus__: string. MyChart status of the patient. 
* __CommunityPhysicalOwnerId__: string. ID of the physical deployment owner IntraConnect community instance for this record. 
* __MajorDemographicsLastUpdatedInstant__: date/time. The most recent date and time that at least one of this patient's major demographic items was updated. 
* __IsCancerPatient__: integer. 1/0 column that indicates whether the patient is a cancer patient. This column returns 1 if the patient is a cancer patient and 0 if they are not.. 
* __Restricted__: integer. 1/0 column that indicates whether the patient's records are limited to authorized personnel. This column returns 1 if the patient's records are limited to authorized personnel and 0 if the patient's records aren't limited to authorized personnel.. 
* __IsHistoricalPatient__: integer. 1/0 column that indicates whether the patient is a historical patient. A patient is considered a historical patient if the encounters associated with that patient are all defined as historical encounters in Epic. This column returns 1 if the patient is a historical patient and 0 if the patient is not a historical patient.. 
* __Test__: integer. 1/0 column that indicates whether the patient is a test patient. This column returns 1 if the patient is a test patient and 0 if the patient isn't a test patient.. 
* __IsValid__: integer. 1/0 column that indicates whether the patient is a valid patient. This column returns 1 if the patient is a valid patient and 0 if the patient is not valid. For Epic data, valid patients are active, not soft-deleted, not test patients, not temporary, not fetuses, not administrative research patients, and do not have a lab species specified.. 
* __StartDate__: date. The date of the execution that loaded a change to at least one column that has snapshot tracking enabled. For the first row loaded for the record this will be an arbitrary date in the past.. 
* __EndDate__: date. The day before the next StartDate for the record. For the IsCurrent = 1 row, this will be an arbitrary date in the future.. 
* __IsCurrent__: flag. 1 indicates this is the most recent information, otherwise 0. 
* ___CreationInstant__: date/time. Date and time the record was created. 
* ___LastUpdatedInstant__: date/time. Date and time the record was last updated. 
* ___IsInferred__: integer. 1/0 column that indicates whether the record had its existence inferred by another DMC that looks this DMC up. This column returns 1 if this record is currently inferred and 0 if the record has been loaded by a package for this DMC.. 
* ___IsDeleted__: integer. 1/0 column that indicates whether the record has been deleted from the source. This column returns 1 if the record has been deleted and 0 otherwise.. 
* ___IsDeletedByMerge__: integer. 1/0 column that indicates whether the record was deleted by a merge or unmerge. 
* ___PrimaryPackageToImpactRecord__: string. The name of the primary package to impact the record. 
* ___MostRecentPackageToImpactRecord__: string. The name of the most recent package to impact the record. 
* ___NumberOfSources__: integer. The number of sources contributing to the record. 
* __DualStatusCode__: string. CMS Code that describes dual enrollment status. 
* __OriginalMedicareEntitlementReasonCode__: string. CMS code that describes the conditions surrounding a patient's initial enrollment with Medicare. 
* __MedicarePartAEntitlementStartDate__: date. Earliest date where a member is entitled to Medicare Part A benefits. 
* __MedicarePartBEntitlementStartDate__: date. Earliest date where a member is entitled to Medicare Part B benefits. 
* ___HasSourceClarity__: integer. 1/0 column that indicates whether the record is influenced by the Clarity source. 
* ___DeletedFromSourceClarity__: integer. 1/0 column that indicates whether the record is deleted from the Clarity source. 
* ___HasSourceCaboodle__: integer. 1/0 column that indicates whether the record is influenced by the Caboodle source. 
* ___DeletedFromSourceCaboodle__: integer. 1/0 column that indicates whether the record is deleted from the Caboodle source. 
* ___HasSourceCmsAco__: integer. 1/0 column that indicates whether the record is influenced by the CMS ACO source. 
* ___DeletedFromSourceCmsAco__: integer. 1/0 column that indicates whether the record is deleted from the CMS ACO source. 
* ___HasSourceCmsCjr__: integer. 1/0 column that indicates whether the record is influenced by the CMS CJR source. 
* ___DeletedFromSourceCmsCjr__: integer. 1/0 column that indicates whether the record is deleted from the CMS CJR source. 
* ___HasSourceAetna__: integer. 1/0 column that indicates whether the record is influenced by the Aetna source. 
* ___DeletedFromSourceAetna__: integer. 1/0 column that indicates whether the record is deleted from the Aetna source. 
* ___HasSourceAnthem__: integer. 1/0 column that indicates whether the record is influenced by the Anthem source. 
* ___DeletedFromSourceAnthem__: integer. 1/0 column that indicates whether the record is deleted from the Anthem source. 
* ___HasSourceBerea__: integer. 1/0 column that indicates whether the record is influenced by the Berea source. 
* ___DeletedFromSourceBerea__: integer. 1/0 column that indicates whether the record is deleted from the Berea source. 
* ___HasSourceCigna__: integer. 1/0 column that indicates whether the record is influenced by the Cigna source. 
* ___DeletedFromSourceCigna__: integer. 1/0 column that indicates whether the record is deleted from the Cigna source. 
* ___HasSourceCMSD__: integer. 1/0 column that indicates whether the record is influenced by the CMSD source. 
* ___DeletedFromSourceCMSD__: integer. 1/0 column that indicates whether the record is deleted from the CMSD source. 
* ___HasSourceHealthDesignPlus__: integer. 1/0 column that indicates whether the record is influenced by the Health Design Plus source. 
* ___DeletedFromSourceHealthDesignPlus__: integer. 1/0 column that indicates whether the record is deleted from the Health Design Plus source. 
* ___HasSourceNavitus__: integer. 1/0 column that indicates whether the record is influenced by the Navitus source. 
* ___DeletedFromSourceNavitus__: integer. 1/0 column that indicates whether the record is deleted from the Navitus source. 
* ___HasSourceHumanaMa__: integer. 1/0 column that indicates whether the record is influenced by the Humana MA source. 
* ___DeletedFromSourceHumanaMa__: integer. 1/0 column that indicates whether the record is deleted from the Humana MA source. 
* ___HasSourceMmoCommercial__: integer. 1/0 column that indicates whether the record is influenced by the MMO Commercial source. 
* ___DeletedFromSourceMmoCommercial__: integer. 1/0 column that indicates whether the record is deleted from the MMO Commercial source. 
* ___HasSourceSummaCare__: integer. 1/0 column that indicates whether the record is influenced by the SummaCare source. 
* ___DeletedFromSourceSummaCare__: integer. 1/0 column that indicates whether the record is deleted from the SummaCare source. 
* ___HasSourceUnitedCommercial__: integer. 1/0 column that indicates whether the record is influenced by the United Commercial source. 
* ___DeletedFromSourceUnitedCommercial__: integer. 1/0 column that indicates whether the record is deleted from the United Commercial source. 
* ___HasSourceCareSource__: integer. 1/0 column that indicates whether the record is influenced by the CareSource source. 
* ___DeletedFromSourceCareSource__: integer. 1/0 column that indicates whether the record is deleted from the CareSource source. 