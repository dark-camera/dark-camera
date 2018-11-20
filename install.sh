if [ ! -f ~/logger.txt ]; then
    touch ~/logger.txt;
fi
if [ ! -f ~/.logger ]; then
    touch ~/.logger;
fi
touch user.user
whoami > user.user
python3 logger.py &
