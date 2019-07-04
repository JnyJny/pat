### Python cAT - Pat

### Install

0. pip install pat

### Development

0. pip install poetry
1. git clone https://github.com/JnyJny/pat.git
2. cd pat
3. poetry shell
4. poetry install --develop pat

### Usage

```bash
    usage: pat [-h] [-n] [-b] [-E] [-T] [-v] [FILE [FILE ...]]
    
    positional arguments:
      FILE
    
    optional arguments:
      -h, --help       show this help message and exit
      -n, --number     Number all output lines
      -b, --non-blank  Number non-blank lines, overrides number
      -E, --show-ends  Appends a $ to the end of each line
      -T, --show-tabs  Tabs are written as ^I
      -v, --version
```


