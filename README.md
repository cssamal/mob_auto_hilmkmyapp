# mob_auto_hilmkmyapp
Mobile application automation

### Setup:
1. Install NodeJS server and check both Node and NPM

2. Install Java and Android Studio

3. Install Appium via NPM

4. Install Python(> 3.11) and Appium Python Client

5. Download Appium Inspector

### Prerequisities before running tests:
1. Copy apk file to automation root folder.
2. Create virtual environment
`python3 -m venv myenv`
3. Activate virtual environment
In windows run:
`\myenv\Scripts\activate.bat`
In Mac:
`source myenv/bin/activate `
3. Install dependent modules
`pip install -r requirement.txt`

### Run tests
`pytest tests/ -v`
