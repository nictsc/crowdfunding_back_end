# crowdfunding_back_end

Nicole Chan

## Planning
### Concept / Name
Crowds of Catan is a crowdfunding platform the Catanians (Catan Community) can pitch their Catan-inspired game campaigns and receive community backing. Players become investors; pledging support for creative expansions, custom maps and/or innovative rule variations. Want an extra robber run amok on resources? This project plans to bring those out of the box ambitions of the Catanians to life.

### Intended Audience / User Stories
- Catan players who want to create fundraisers to support their in-game ambitions and view their resource goals.
- Catan game developers who want to create fundraisers to support their creative expansions, custom maps or rule variations and view their resource goals.
- Catan supporters who want to support fundraisers by pledging their resources.
- Catan visitors who want to view the fundraisers

### Front End Pages/Functionality
Home Page
- View all fundraisers
- Navigate to Login Page
- View individual fundraisers by clicking on their tile

Login Page
- Login with account credentials

Fundraiser Details Page
- View photo, short description and status bar showing resources raised and ideal resources goal
- View pledges

Fundraiser Admin Page
Prerequisite - Succuessful authenticiation
- Create new fundraiser
- Update existing fundraiser on title, photo and/or description
- Delete existing fundraiser and subsequent pledges

Account Admin Page
Prerequisite - Succuessful authenticiation
- Update password
- Update first name, last name and email address

### API Spec

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| /api/signup | POST | Create a account | first name, last name, email, password | 201 Created | none |
| /api/login | POST | Log user | email, password | 200 OK | none |
| /api/users | PATCH | Update an account | first name, last name, email, password | 204 No Content | authenticated user |
| /api/fundraisers | GET | View all fundraisers | ID, title, description, target goal, amount raised | 200 OK | none |
| /api/fundraisers/{id} | GET | View a fundraiser | ID, title, description, target goal, amount raised | 200 OK | none |
| /api/fundraisers | POST | Create a fundraiser | ID, title, description, target goal | 201 Created | authenticated user |
| /api/fundraisers | PATCH | Update a fundraiser | ID, title, description, target goal | 204 No Content | authenticated user |
| /api/fundraisers | Delete | Delete a fundraiser | ID, title, description, target goal | 204 No Content | authenticated user |
| /api/fundraisers/{id}/pledge| POST | Create a pledge | amount, created time/date | 201 Created | authenticated user |

### DB Schema