# Working hours
This is an application that converts the 12 hours clock into military clock

The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Homepage Problem Set 7 : Working](hhttps://cs50.harvard.edu/python/2022/psets/7/working/)

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/console-Adieu-py.git

# Using git bash
git clone https://github.com/krigjo25/console-Adieu-py.git

# Using Github Cli
gh repo clone console-Adieu-py
```

2. Navigate to the project directory
```sh
cd console-adieu-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py
python app.py 
```

## Example
```sh
python app.py

Hours : <9 AM to 5 PM>

expected output: '09:00 to 17:00'
```
Replace `<9 AM to 5 PM>` with the desired time.

##  Credits

### Responsories
[regex -  Matthew Barnett](https://github.com/mrabarnett/mrab-regex)
[pytest - Holger Krekel ( and many other developers)](https://github.com/pytest-dev/pytest)


##  Testing framework / Datasets
The project uses pytest to perform automated tests
```sh
pytest -k test_app.py       #   Run a detailed test
pytest --html=index.html    #   Run a test with HTML template
```
Data sets which has been used in the project is located in the [Test folder](./tests/)
## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25