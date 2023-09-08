# primerAnalyzerV2
Simple pipeline written in shell script which uses simple python scripts with the combination of already existing tool primer3, which helps user select correct primer sequences while doing the Sanger DNA sequencing.


## Installing primerAnalyzerV2
```
sudo apt update

pip install progress

git clone https://github.com/miklafc/primerAnalyzer.git

cd primerAnalyzer/

chmod +x primerAnalyzerV2.sh
```

## Installing primer3

See [primer3](https://github.com/primer3-org/primer3) for instuctions on how to install primer3.

**Note:** It's important that both primerAnalyzer and primer3 directories are in the same location (for example both of them are in the home directory in my case).


## Altering the shell script

After you have successfully installed both tools you are going to have to alter the shell script. See bellow.

Open the shell script with a text editor and change the path to the primer3file to where it actually is located on your machine.

![Screenshot](https://raw.githubusercontent.com/miklafc/primerAnalyzer/main/Screenshot%20from%202023-09-08%2014-16-47.png)

After you have changed the location of the primer3file you are good to go.

## Running the pipeline

```
./primerAnalyzerV2.sh
```

## How to use the tool

Open the *primerAnalyzer_manual.pdf* to follow the example how primers are designed.


**Note:** *When opening the output.html* use Firefox browser to get the correct visual.

