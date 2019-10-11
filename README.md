# M2
Program files and project documentation (both still in development)


Project Group 6 – Erwin, Celia and Yuliia

The Juceer (July, Celia & Erwin) song API is organized around representational state transfer (REST). Our API uses standard HTTP response codes and authentication. Juceer simplifies song data selection by various variables such as song information, genre, artist and ranking. Further on, the basic documentation of the Juceer API is given.

Note: The Juceer API documentation is a “living” document. Version 1.0

Back-end was written on Python using Django. So far only the Bootstrap is used to visualize the required minimum visual elements.

Functionality of the current version:
1. Ability to download a '.csv' dataset format (so far only this format has been developed, since the given database is '.csv') as a set of entries. For proper operation, pre-processing of the dataset is required, as there is noise in the dataset. At present, 8 columns out of 34 are being developed. This desicion is due to the fact that many values are redundant and do not affect the functioning of the application in any way.

2. View a list of all songs in chronological order (that is, the order in which they are downloaded from the dataset). After typing at any entry, you go to the entry details page. There is an opportunity to go to the Google page about this artist.
Also, if the user is authorized as an staff, it is possible to the edit page of the entry or delete it.

3. The navigation bar allows to move from one window to another and search for records (the function is not available in the current version). From this panelis possible to go to pages with sorted entries.

4. Sort all songs by year of release. The function still needs clarification, since in many records the value of this field equals to "0".

5. Sort all the songs by popularity.

6. Sort all the artists alphabetically. Only unique values are shown.

7. Sort all artists by genre.

8. Sort all artists by popularity.

9. The start page on which the registered user receives information about the functionality of the application, and the new user is asked to register in the system. Also information page.

