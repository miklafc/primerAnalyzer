import csv
import functions
import pandas as pd

seqStr = open("rawsequence.txt", "r")
seqStart = seqStr.read()
seq = seqStart.strip()
seq = seq.replace("\n", "")

primerLeftStr = open("leftPrimer.txt", "r")
primerLeftStart = primerLeftStr.read()
primerLeft = primerLeftStart.strip()
leftReversed = primerLeft[::-1]

primerRightStr = open("rightPrimer.txt", "r")
primerRightStart = primerRightStr.read()
primerRight = primerRightStart.strip()
rightReversed = primerRight[::-1]

fieldNames = ["Gene Name", "Primer Name", "Forward Seq box position", "Reverse Seq box position", "Forward Sequence",
              "Forward Seq length", "Reverse Sequence", "Reverse Seq length", "Chromosome", "Starting Position",
              "Ending Position",
              "Length", "TM of forward primer", "TM of reverse primer", "DNA Sequence"]

trimmedSeq = functions.GeneSwap(
    functions.ReverseSeq(functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                                            functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                                                 seq),
                                            seq)))

while True:
    selection = input("Do you want to add the primers you have designed to the database? [y/n] ").upper()
    if selection == 'Y':
        positionF = input("Enter the position of the Forward primer in the box: ")
        positionR = input("Enter the position of the Reverse primer in the box: ")
        geneName = input("Copy the name of the gene: ")
        primerName = input("Copy the name of the primer: ")
        chromosome = input("Copy the chromosome number: ")
        startingPos = input("Copy the starting position: ")
        endingPos = input("Copy the ending position: ")
        length = len(trimmedSeq)
        meltingTempF = functions.calculatingMeltingTemp(primerLeft)
        meltingTempR = functions.calculatingMeltingTemp(primerRight)
        primerRightLength = len(primerRight)
        primerLeftLength = len(primerLeft)

        with open("primerDatabase.csv", "a", newline='') as file:
            writer = csv.writer(file)
            # writer.writerow(fieldNames)
            writer.writerow(
                [geneName, primerName, positionF, positionR, primerLeft, primerLeftLength, primerRight, primerRightLength,
                 chromosome, startingPos, endingPos, length, meltingTempF, meltingTempR, trimmedSeq])
        file.close()

        csvFile = pd.read_csv("primerDatabase.csv")
        sorted_file = csvFile.sort_values(by=['Gene Name'], ascending=True)
        sorted_file.to_csv('primerDatabase_sorted.csv', index=False)
        break
    else:
        break
