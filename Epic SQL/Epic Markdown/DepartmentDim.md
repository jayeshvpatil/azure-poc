## Table: DepartmentDim
### Table Description
The department dimension contains information about locations in a facility. Each row represents a bed, room, room group, care area, submitter, department, location, service area, facility profile, or business segment.For Epic data, data is imported at each level of granularity, with records at each level of granularity containing information about the levels above it.
### Table Columns
* __DepartmentKey__: integer. Surrogate key used to uniquely identify the record. 
* __Name__: string. Name of the location in the facility. 
* __BedEpicId__: string. Epic ID of the bed. This column identifies Grand Central bed (BED) records.. 
* __BedName__: string. Name of the bed. 
* __IsBed__: integer. 1/0 column that indicates whether this is a bed. This column returns 1 if this is a bed and 0 if this is not a bed.. 
* __BedInCensus__: integer. 1/0 column that indicates whether the bed should be included in census reporting. This column returns 1 if the bed should be included in census reporting and 0 if the bed shouldn't be included in census reporting.. 
* __RoomEpicId__: string. Epic ID of the room. This column identifies Grand Central room (ROM) records.. 
* __RoomName__: string. Name of the room. 
* __IsRoom__: integer. 1/0 column that indicates whether this is a room. This column returns 1 if this is a room and 0 if this is not a room.. 
* __RoomGroupEpicId__: string. Epic ID of the room group. This column identifies location (EAF) records.. 
* __RoomGroupName__: string. Name of the group of rooms to which the room belongs. For Epic data, this column is only populated for operating rooms.. 
* __IsRoomGroup__: integer. 1/0 column that indicates whether this is a room group. This column returns 1 if this is a room group and 0 if this is not a room group.. 
* __CareAreaEpicId__: string. Epic ID of the care area. This column identifies care area (LED) records.. 
* __CareAreaName__: string. Name of the care area. 
* __IsCareArea__: integer. 1/0 column that indicates whether this is a care area. This column returns 1 if this is a care area and 0 if this is not a care area.. 
* __SubmitterEpicId__: number. Epic ID of the submitter. This column identifies submitter (SMT) records.. 
* __EmrParticipantLevel__: string. Level of patient integration with the Electronic Medical Record. For Epic data, this column is only populated for submitters and can contain Participating, Non-Participating, or Participating without patient creation.. 
* __IsSubmitter__: integer. 1/0 column that indicates whether this is a submitter. This column returns 1 if this is a submitter and 0 if this is not a submitter.. 
* __DepartmentEpicId__: string. Epic ID of the department. This column identifies department (DEP) records.. 
* __DepartmentName__: string. Name of the department or submitter. 
* __DepartmentExternalName__: string. External name of the department or submitter, often used in patient correspondence. 
* __DepartmentAbbreviation__: string. Abbreviated department name. 
* __DepartmentCenter__: string. Center to which the department belongs. 
* __DepartmentSpecialtyEpicId__: string. Epic ID of the specialty practiced in the department. 
* __DepartmentSpecialty__: string. Specialty practiced in the department. 
* __DepartmentSpecialtyAbbreviation__: string. Abbreviation for the specialty practiced in the department. 
* __DepartmentType__: string. Primary type of the department. 
* __DepartmentServiceGrouper__: string. Service reporting grouper of the department. 
* __DepartmentLevelOfCareGrouper__: string. Level of care reporting grouper of the department. 
* __IsDepartment__: integer. 1/0 column that indicates whether this is a department. This column returns 1 if this is a department and 0 if this is not a department.. 
* __RestrictedDepartment__: integer. 1/0 column that indicates whether the department is a restricted department. This column returns 1 if the department is a restricted department and 0 if the department isn't a restricted department.. 
* __OtherAreaName__: string. Name of the area outside the facility structure. For Epic data, this includes Patient Location Facility (PLF) records with a type of 7-Other.. 
* __LocationEpicId__: string. Epic ID of the location. This column identifies facility profile (EAF) records with a type of 2-Location.. 
* __LocationName__: string. Name of the location. 
* __LocationAbbreviation__: string. Abbreviated name of the location. 
* __LocationCcnEpicId__: number. Epic ID of the Centers for Medicare and Medicaid Services certification number (CCN) for the location. 
* __LocationCcn__: string. Centers for Medicare and Medicaid Services certification number (CCN) for the location. 
* __IsLocation__: integer. 1/0 column that indicates whether this is a location. This column returns 1 if this is a location and 0 if this is not a location.. 
* __IsFacilityProfile__: integer. 1/0 column that indicates whether this is a facility profile. This column returns 1 if this is a facility profile and 0 if this is not a facility profile.. 
* __ParentLocationEpicId__: string. Epic ID of the parent location. This column identifies facility profile (EAF) records with a type of 2-Location.. 
* __ParentLocationName__: string. Name of the parent location. 
* __RegionEpicId__: string. Epic ID of the region. This column identifies facility profile (EAF) records with a type of 12-Region.. 
* __RegionName__: string. The name of the region. 
* __ServiceAreaEpicId__: string. Epic ID of the service area, facility profile, or business segment. This column identifies facility profile (EAF) records with a type of 1-Facility Profile, 4-Service Area, or 11-Business Segment.. 
* __ServiceAreaName__: string. Name of the service area, facility profile, or business segment. 
* __IsBusinessSegment__: integer. 1/0 column that indicates whether this is a business segment. This column returns 1 if this is a business segment and 0 if this is not a business segment.. 
* __IsServiceArea__: integer. 1/0 column that indicates whether this is a service area or facility profile. This column returns 1 if this is a service area or facility profile and 0 if not.. 
* __IsServiceAreaOrBusinessSegment__: integer. 1/0 column that indicates whether this is a service area, facility profile, or business segment. This column returns 1 if this is a service area, facility profile, or business segment and 0 if not.. 
* __Type__: string. Type of submitter. For Epic data, this column is only populated for submitters and can contain Health Agency, Research, or other values.. 
* __Address__: string. Associated street address.. 
* __City__: string. Associated city. 
* __County__: string. Associated county. 
* __StateOrProvince__: string. Associated state or province. 
* __StateOrProvinceAbbreviation__: string. Abbreviated name of the associated state or province. 
* __Country__: string. Associated country. 
* __PostalCode__: string. Associated postal code. 
* __HomeCareCCN__: string. This column stores the CCN associated with the home health or hospice agency associated with this department.. 
* ___CreationInstant__: date/time. The date and time the record was created. 
* ___LastUpdatedInstant__: date/time. The date and time the record was last updated. 
* ___IsInferred__: integer. 1/0 column that indicates whether the record is inferred. 
* ___IsDeleted__: integer. 1/0 column that indicates whether the record is deleted. 
* ___IsDeletedByMerge__: integer. 1/0 column that indicates whether the record was deleted by a merge or unmerge. 
* ___PrimaryPackageToImpactRecord__: string. The name of the primary package to impact the record. 
* ___MostRecentPackageToImpactRecord__: string. The name of the most recent package to impact the record. 
* ___NumberOfSources__: integer. The number of sources contributing to the record. 
* ___HasSourceClarity__: integer. 1/0 column that indicates whether the record is influenced by the Clarity source. 
* ___DeletedFromSourceClarity__: integer. 1/0 column that indicates whether the record is deleted from the Clarity source. 
* __LocId_X__: number. The unique ID number assigned to the location record.. 
* __LocName_X__: string. The name of the revenue location.. 
* __GLPrefix_X__: string. The code that billing system’s General Ledger report uses to identify transactions belonging to a revenue location.. 
* __FaxNum_X__: string. Stores the fax number for the department.. 