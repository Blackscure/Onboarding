# Onboarding

## Swagger Link
http://localhost:8000/swagger/

Table Name: Customer

Field Name	Data Type	Constraints
id (Primary Key)	Integer	Auto-generated
name	CharField	Max length: 100
phone	CharField	Max length: 15
email	EmailField	
date_of_birth	DateField	
nationality	CharField	Max length: 100
business_name	CharField	Max length: 100
business_categories	CharField	Max length: 100, Choices: BUSINESS_CATEGORIES
business_registration_date	DateField	
county	CharField	Max length: 100, Choices: LOCATION_COUNTY_CHOICES
sub_county	CharField	Max length: 100, Choices: LOCATION_SUB_COUNTY_CHOICES
ward	CharField	Max length: 100, Choices: LOCATION_WARD_CHOICES
building_name	CharField	Max length: 100
floor	CharField	Max length: 100


## This table represents the Customer model you provided, with each field corresponding to a column in the database. The table's primary key is id, which is auto-generated.

Constraints:

business_categories is limited to choices defined in BUSINESS_CATEGORIES.
county, sub_county, and ward have choices based on their respective predefined sets.
