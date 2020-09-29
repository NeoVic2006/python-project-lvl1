#!c:\python_work_for_hexlet\python-project-lvl1\.venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'neovic2006-brain-games','console_scripts','brain-games'
__requires__ = 'neovic2006-brain-games'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('neovic2006-brain-games', 'console_scripts', 'brain-games')()
    )
