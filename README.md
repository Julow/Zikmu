# Zikmu

Set metadata to audio files

Take one or more files and options

```shell
./zikmu -g Dubstep *.mp3
```

Need `Mutagen` lib to be installed 

### Options

- `-a album`
	Set album name for all following files

- `-A artist`
	Set artist name for all following files

- `-d date`
	Set date for all following files

- `-g genre`
	Set genre for all following files

Use empty quote to empty remove a tag. ex: `./zikmu -a "" *.mp3`
