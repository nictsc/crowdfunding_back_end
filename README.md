# crowdfunding_back_end

Nicole Chan

## Planning
### Concept / Name
Crowds of Catan is a crowdfunding platform the Catanians (Catan Community) can pitch their Catan-inspired game campaigns and receive community backing. Players become investors; pledging support for creative expansions, custom maps and/or innovative rule variations. Want an extra robber run amok on resources? This project plans to bring those out of the box ambitions of the Catanians to life.

### Intended Audience / User Stories
- Catan players
    - Authenticated users.
    - They have the ability to create, update and delete their fundraisers.
    - Their main goal is to create fundraisers to support their in-game ambitions and view their resource goals.
- Catan game developers 
    - Authenticated users.
    - They have the ability to create, update and delete their fundraisers.
    - Their main goal is to create fundraisers to support their creative expansions, custom maps or rule variations and view their resource goals.
- Catan supporters 
    - Authenticated users. 
    - They have the ability to create pledges.
    - Their main goal is to support fundraisers by pledging their resources.
- Catan visitors are 
    - Unauthenticated users.
    - They have the ability to view fundraisers and pledges.
    - Their main goal is to view the fundraisers as a whole and in detail.

### Front End Pages/Functionality
Home Page
- Functionality
    - View all fundraisers in tile formats
    - Navigate to Login Page via link
    - Navigate to respective fundraiser details page by clicking on tile
- Front End Elements
    - Fundraiser tiles
    - Fundraiser photos
    - Fundraiser truncated description (60-100 characters)
    - Link to Login Page

Login Page
- Functionality
    - Login with account credentials
- Front End Elements
    - Username field
    - Password field
    - Login button
    - Error message for wrong credentials entered

Fundraiser Details Page
- Functionality
    - View pledges, fundraiser photo, fundraiser short description and fundraiser status bar showing resources raised and ideal resources goal
    - Create pledges
- Front End Elements
    - Fundraiser title
    - Fundraiser photo
    - Fundraiser short description
    - Funraiser status bar showing amount raised and target goal
    - Side section on making pledges 
        - Name field (Mandatory)
        - Amount field (Mandatory)
        - Description field (Optional)
        - Create pledge button
        - Status message indicating saved pledge is successful

Fundraiser Admin Page
- Prerequisite 
    - Succuessful authenticiation
- Functionality
    - Create new fundraiser
    - Update existing fundraiser on title, photo and/or description by clicking on respective tiles and update button
    - Delete existing fundraiser and subsequent pledges by clicking on respective tiles and delete button
- Front End Elements
    - Fundraiser tiles showing fundraiser titles and photos
    - Create button
    - Update button
    - Delete button
    - Save changes button
    - Fundraiser title field
    - Fundraiser photo upload
    - Fundraiser description field
    - Fundraiser Target Amount field

Account Admin Page
- Prequisite
    - Succuessful authenticiation
- Functionality
    - Update first name
    - Update last name
    - Update email address
    - Update password
- Front End Elements
    - First name field (Optional)
    - Last name field (Optional)
    - Email field (Optional)
    - Password field (Optional)
    - Save changes button
    - Status message indicating saved changes is successful

### API Spec

| URL                          | HTTP Method | Purpose              | Request Body                                   | Success Response Code | Authentication/Authorisation |
|------------------------------|-------------|----------------------|------------------------------------------------|-----------------------|------------------------------|
| /signup                      | POST        | Create an account    | first name, last name, email, password         | 201 Created           | none                         |
| /login                       | POST        | Authenticate User    | email, password                                | 200 OK                | none                         |
| /users                       | PATCH       | Update an account    | first name, last name, email, password         | 204 No Content        | authenticated user           |
| /fundraisers                 | GET         | View all fundraisers | title, description, target goal, amount raised | 200 OK                | none                         |
| /fundraisers/{id}            | GET         | View a fundraiser    | title, description, target goal, amount raised | 200 OK                | none                         |
| /fundraisers                 | POST        | Create a fundraiser  | title, description, target goal                | 201 Created           | authenticated user           |
| /fundraisers/{id}            | PATCH       | Update a fundraiser  | title, description, target goal                | 204 No Content        | authenticated user           |
| /fundraisers/{id}            | DELETE      | Delete a fundraiser  |                                                | 204 No Content        | authenticated user           |
| /fundraisers/{id}/pledge     | POST        | Create a pledge      | first name, last name, amount                  | 201 Created           | authenticated user           |

### Database Schema
![Database Schemas](./media/database_schemas.png)