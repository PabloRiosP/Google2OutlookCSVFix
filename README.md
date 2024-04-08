# Google2OutlookCSVFix
Google2OutlookCSVFix automates contact export from Google to Outlook, removing unnecessary fields. Developed with Pandas, it simplifies CSV importation into Outlook.

## Usage
1. Create 2 folders in same directory where executable is: `input` and `output`.
2. Put your Google Contact's exported CSV files for Microsoft Outlook.
3. Run the software. You can use the `src/fix.py` file when you have already created a virtual environment with `requirements.txt` installed (`pip install -r requirements.txt`). If you are in Windows you can run the exe file without any requirements other than the `input` (with your CSV files) and `output` folders.
4. The output CSV is generated and is in the `output` folder.
5. Import your contacts in your Microsoft Outlook as contacts by setting customized fields.

The fields that are kept are specified in `src/fix.py`. Modify this if you want to keep other fields. You must generate the EXE file with pyinstaller if you want to run the modified script as EXE in Windows, but you can run the modified py file if you have already created virtual environment with requirements installed.

## Notes
Sorry about my bad English :) and thank you for the feedback.

This was a quick solution I created to address a specific issue with importing contacts for an enterprise migrating to Outlook. That's why it is simple and doesn't create the default `input` and `output` folders, for example.

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](./LICENSE) file for details.
