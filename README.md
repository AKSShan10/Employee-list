# Employee-list
This is a employee list project which build in Django framework. It has full-filled following requirements:
1. Images of employees resized before storing. So that large images do not take a long time to load. You have to use some 3rd party library or client side resize mechanism to achieve this.
2. Name, email, mobile and date of birth column should be sortable.
3. Data came from the database with paging. So if the user is viewing 10 items per page, only 10 items should be fetched from the database even if there are thousands of rows in the database table. 
4. Clicking the edit button under “Actions” will take the user to the edit page.
5. Clicking the delete button under “Actions” will show a confirmation popup asking “Are you sure, you want to delete this?”. There will be “Yes” and “No” buttons in the popup. If the user clicks “Yes” then the item is deleted, otherwise not.
6. In the “Add employee” page, the user will provide, Photo file, first name, last name, email, mobile, and date of birth. 
7. All date fields should use a date picker JavaScript plugin for easy date selection. 
8. Search should work for partial matches in case of name and email.
