# backup-manager
Downloads and saves CSV backup data from our backend database

### Prepare:
- Optionally [create virtual env](https://docs.python.org/3/library/venv.html)
- Clone repo and install required packages  
```
git clone https://github.com/klubidorka/backup-manager
cd backup-manager
pip install -r requirements.txt
```
- Create and fill in config file (see 'config_example.py')
```
touch config.py
```
### How to use:
- Save backup file in the specified directory
```
python3 backup.py -p "path/to/dir"  
```
- OR save backup file in the current directory
```
python3 backup.py
```
