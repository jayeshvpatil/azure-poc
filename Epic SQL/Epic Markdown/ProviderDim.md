## Table: ProviderDim
### Table Description
The provider dimension contains information about providers. Each row represents a provider for a date range.This table contains both current and historical information. For current records, IsCurrent has a value of 1. Historical records contain information that is valid for the date range specified by the StartDate and EndDate columns.
### Table Columns
* __ProviderKey__: integer. Surrogate key used to uniquely identify the record. 
* __DurableKey__: integer. Durable key used to identify the record. 
* __EmployeeDurableKey__: integer. The employee associated with this provider. Links to EmployeeDim table.
* __ProviderEpicId__: string. Epic ID of the provider. This column identifies provider (SER) records.. 
* __EmployeeEpicId__: string. Epic ID of the employee. This column identifies user (EMP) records.. 
* __Name__: string. Name of the provider. 
* __Upin__: string. Unique Physician Identification Number (UPIN) for the provider. 
* __Npi__: string. National Provider Identifier (NPI) for the provider. 
* __DeaNumber__: string. The Drug Enforcement Administration (DEA) number for the provider. 
* __MedicareIdNumber__: string. Medicare ID number for the provider. 
* __MedicaidIdNumber__: string. Medicaid ID number for the provider. 
* __Sex__: string. Sex of the provider. 
* __PrimaryDepartmentEpicId__: string, snapshot on data change. Epic ID of the primary department with which the provider is associated. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimaryDepartment__: string, snapshot on data change. Name of the primary department with which the provider is associated. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimaryLocation__: string, snapshot on data change. Name of the location associated with the primary department with which the provider is associated. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimaryServiceArea__: string, snapshot on data change. Name of the service area associated with the primary department with which the provider is associated. This column will be changed in the future to have no change tracking (Type 1).. 
* __Type__: string, snapshot on data change. Type of the provider. This column will be changed in the future to have no change tracking (Type 1).. 
* __ClinicianTitle__: string, snapshot on data change. Clinician title for the provider. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimarySpecialty__: string, snapshot on data change. Primary specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __PrimarySpecialtyTaxonomyCode__: string, snapshot on data change. Taxonomy code for the provider's primary specialty. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimarySpecialtyTaxonomyName__: string, snapshot on data change. Name of the taxonomy code for the provider's primary specialty. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimarySpecialtyCmsCode__: string, snapshot on data change. Centers for Medicare & Medicaid Services (CMS) code for the provider's primary specialty. This column will be changed in the future to have no change tracking (Type 1).. 
* __PrimarySpecialtyCmsName__: string, snapshot on data change. Name of the Centers for Medicare & Medicaid Services (CMS) code for the provider's primary specialty. This column will be changed in the future to have no change tracking (Type 1).. 
* __SecondSpecialty__: string, snapshot on data change. Second specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __ThirdSpecialty__: string, snapshot on data change. Third specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __FourthSpecialty__: string, snapshot on data change. Fourth specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __FifthSpecialty__: string, snapshot on data change. Fifth specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __SixthSpecialty__: string, snapshot on data change. Sixth specialty of the provider. This column will be changed in the future to have no change tracking (Type 1). Use ProviderSpecialtyHistoryDim for historical specialty information.. 
* __OfficePhoneNumber__: string. Office phone number for the provider. 
* __Email__: string. Email address for the provider. 
* __OfficeAddress__: string, snapshot on data change. Street address for the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficeCity__: string, snapshot on data change. City of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficeCounty__: string, snapshot on data change. County of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficeStateOrProvince__: string, snapshot on data change. State or province of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficeStateOrProvinceAbbreviation__: string, snapshot on data change. Abbreviated state or province of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficeCountry__: string, snapshot on data change. Country of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __OfficePostalCode__: string, snapshot on data change. Postal code of the provider's office. This column will be changed in the future to have no change tracking (Type 1).. 
* __EntityType__: string. Type of entity the provider is. Acceptable values are "Individual", "Group", or "Organization".. 
* __AnesthesiaProviderGroup__: string, snapshot on data change. Anesthesia provider group to which the provider belongs, if applicable. This column will be changed in the future to have no change tracking (Type 1).. 
* __Resident__: integer, snapshot on data change. 1/0 column that indicates whether the provider is a resident. This column returns 1 if the provider is a resident and 0 if the provider isn't a resident. This column will be changed in the future to have no change tracking (Type 1).. 
* __Generic__: integer. 1/0 column that indicates whether the provider is marked as generic. This column returns 1 if the provider was marked as generic and 0 if the provider wasn't marked as generic.. 
* __IsMedicationAuthorizingProvider__: integer. 1/0 column that indicates whether the provider can authorize medications. This column returns 1 if the provider can authorize medications and 0 if the provider can't authorize medications.. 
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
* ___HasSourceClarity__: integer. 1/0 column that indicates whether the record is influenced by the Clarity source. 
* ___DeletedFromSourceClarity__: integer. 1/0 column that indicates whether the record is deleted from the Clarity source. 
* ___HasSourceCaboodle__: integer. 1/0 column that indicates whether the record is influenced by the Caboodle source. 
* ___DeletedFromSourceCaboodle__: integer. 1/0 column that indicates whether the record is deleted from the Caboodle source. 
* ___HasSourceNPPES__: integer. 1/0 column that indicates whether the record is influenced by the NPPES source. 
* ___DeletedFromSourceNPPES__: integer. 1/0 column that indicates whether the record is deleted from the NPPES source. 
* ___HasSourceCMS__: integer. 1/0 column that indicates whether the record is influenced by the CMS source. 
* ___DeletedFromSourceCMS__: integer. 1/0 column that indicates whether the record is deleted from the CMS source. 
* __ExternalName_X__: string. The external name of the provider record. 
* __OfficeFaxNumber_X__: string. The office fax number for the provider..