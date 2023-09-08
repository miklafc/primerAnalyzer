#!/bin/bash
echo "******************************************************************************************"
echo "*                   _                     ___               _ _                          *"
echo "*         _ __  _ _(_)_ __ ___   ___ _ _ /   \  _ __   __ _| (_)_____ ____ _ _           *"
echo "*        | '_ \| ' | | '_ - _ \ / _ \ ' |  _  \| '_ \ / _' | | |_   //  _ \ ' |          *"
echo "*        | |_) |  /| | | | | | |  __/  /  /_\  | | | | (_| | | |/  /_|  __/  /           *"
echo "*        | .__/|_| |_|_| |_| |_|\___|_|__/   \_|_| |_|\__,_|_|_|_____|\___|_|            *"
echo "*        |_|                                                                             *"
echo "******************************************************************************************"
echo "------------------------------------------------------------------------------------------"
echo "-----------------------------primerAnalyzer-v2.0------------------------------------------"
echo "------------------------------------------------------------------------------------------"
echo "=========================================================================================="
echo "    This is a simple python script tool for checking whether the primers are correctly    "
echo "                     designed for your DNA sequence of choice.                            "
echo "=========================================================================================="
date
cd primerAnalyzer
python3 obtainingDNA.py
if [ -s rawsequence.txt ]; then
echo ""
echo "(✓) DNA sequence saved to the rawsequence.txt file."
echo ""
else
exit 1
fi
read -p "First step of the analysis done! Press ENTER to continue!"
truncate -s 0 analysisFile.txt
while ! [ -s analysisFile.txt ]; do
python3 pickingPrimers.py
if [ -s primer3file ]; then
echo ""
echo "(✓) Data saved to primer3file."
echo ""
else
exit 1
fi
read -p "Second step of the analysis done! Press ENTER to continue!"
cd -
cd primer3/src
#change the path to the primer3file to where it is located on your machine
./primer3_core /home/primerAnalyzer/primer3file
cd -
cd primerAnalyzer
read -p "Third step of the analysis done! Press ENTER to continue!"
python3 primerChecking.py
if [ -s leftPrimer.txt ] && [ -s rightPrimer.txt ]; then
echo ""
echo "(✓) Both primers saved to their respective files."
echo ""
else
exit 1
fi
read -p "Fourth step of the analysis done! Press ENTER to continue!"
python3 analyzing.py
if [ -s analysisFile.txt ]; then
sleep 0.2
echo ""
echo "Opening the UCSC In-Silico PCR site..."
sleep 0.1
echo ""
echo "Left primer (FORWARD): "
cat leftPrimer.txt
echo ""
echo "Right primer (REVERSE): "
cat rightPrimer.txt
echo ""
sleep 2
firefox https://genome.ucsc.edu/cgi-bin/hgPcr
python3 visualOutput.py
date
break
else
echo ""
echo "Selected primers are not the best fit for your DNA sequence of choice!"
read -p "Press ENTER to pick new set of primers!"
echo ""
continue
fi
done
