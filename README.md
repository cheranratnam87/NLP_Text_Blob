Compile and install Python from scratch

#sudo apt-get update

#sudo apt-get install build-essential gdb lcov libbz2-dev libffi-dev libgdbm-dev liblzma-dev libncurses5-dev libreadline-dev libsqlite3-dev libssl-dev xz-utils tk-dev uuid-dev zlib1g-dev

'wget https://www.python.org/ftp/python/3.12.4/Python-3.12.4.tgz'

'tar zxvf Python-3.12.4.tgz'

'./configure --enable-optimizations'

' make -j4'

'sudo make altinstall'

'/usr/local/bin/python3.12 '

'vim ~/.bashrc'

enter the url from above

alias python="/usr/local/bin/python3.12"

'source ~/.bashrc'

goto bash again then

#source virtual env

'source ~/.venv/bin/activate'

'python -m venv ~/.venv'

'make install'