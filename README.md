# Swimming Database

*Command line application connecting with local MS Sql Server. Made for university databases course.*

## User's manual

### Initial configuration

1. Install `python3` and `MS SQL Server`.
2. Download this repository.
3. Run `pip install -r requirements.txt` in main folder to install needed packages.
4. * Run `echo "username, password = '[your MS SQL Server username]', '[your MS SQL Server Password]'" > app/settings.py` with substituted your MS SQL Server credentials.
   * If you can't run above command, just create file in `settings.py` app folder and write there `username, password = '[your MS SQL Server username]', '[your MS SQL Server Password`.
   * **Attention!**
File `app/settings.py` contains your server username and password. Be careful with version controll softwere! Should username and/or password change, you have to repeat this step.

5. Execute `db_create.sql` to database and fill it with examlpe data.
6. Execute `main.py` to start the app.

### App usage

App menu is printed and user should type in selected number and press `Enter`.

## App functionality

User can:

* Insert new data
* Delete records by selected criteria
* Modify records
* Print reports
