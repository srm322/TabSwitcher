# TabSwitcher
###### For Grey Oakcs CC
######
### Project By:
#### Sam Markovich
###### ___________________________________________________________________________________

Program to switch between 2 tabs in fullscreen using chrome drivers and selinium

Currently being used for information board.

# 

chrome location: chrome binary and driver in chrome folder.
- it stupid large tho, so it never coming near Git again.
-  website: https://googlechromelabs.github.io/chrome-for-testing/#stable

#


Steps for getting working from fresh
1. clone from repo
2. download chrome and chromedriver from link above
3. make folder in parent directory called chrome and put both unzipped downloads in there
4. in terminal type 
```js
conda env create -f env.yml
python switch.py
```

```
pyinstaller --onefile --add-binary "/usr/bin/chrome:/chrome-linux64" --add-binary "/usr/bin/chrome:/chromedriver-linux64" bin-switch.py