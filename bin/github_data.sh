# commit to csv_data
#!/usr/bin/env bash

URL=https://github.com/thanhnhu/vietlott.git
FOLDER=vietlott
DATA_FOLDER=data
USER="thanhnhu"
EMAIl="thanhnhudn@gmail.com"

# generate data file
echo "pwd $(pwd)"

export PYTHONPATH="src"
export LOGURU_LEVEL="INFO"

# Random delay (1s to 5 minutes) to avoid detect as bot
RANDOM_DELAY=$(( RANDOM % 301 + 1 ))
sleep $RANDOM_DELAY

python src/vietlott/cli/crawl.py power_655
python src/vietlott/cli/missing.py power_655
python src/vietlott/cli/crawl.py power_645
python src/vietlott/cli/missing.py power_645
#python src/vietlott/cli/crawl.py keno
#python src/vietlott/cli/missing.py keno

python src/render_readme.py

#if [[ ! -d "$FOLDER" ]] ; then
#  git clone $URL $FOLDER
#fi

#cp -r $DATA_FOLDER $FOLDER/

#cd $FOLDER
#git pull

# commit and push
git config user.name "\'$USER\'"
git config user.email "\'$EMAIl\'"
git status
git add $DATA_FOLDER
git add readme.md
git commit -m "update data @ `date +%Y-%m-%d\ %H:%M:%S`"
git push
