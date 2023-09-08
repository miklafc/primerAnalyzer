import time
import requests

seqFile = open("rawsequence.txt", "r+")
seqFile.truncate(0)
seqFile = open("rawsequence.txt", "w")
newList = []

def highlightDNAwithNuc(rawDna, lenNuc):
    """Function that highlights the DNA, so it's ready to be analyzed."""
    rawDna = rawDna.upper()
    int(lenNuc)
    tempSeqOne = rawDna[:250] + "_"
    tempSeqTwo = ""
    for nuc in range(250, 250 + int(lenNuc)):
        tempSeqTwo += rawDna[nuc]
    tempSeqThree = "_" + rawDna[250 + int(lenNuc):]
    listOne = []
    listOne += [tempSeqOne]
    listOne += [tempSeqTwo]
    listOne += [tempSeqThree]
    finalSeq = ''.join(listOne)
    return finalSeq


def dnaCheckUp(rawdna):
    """Function that checks whether the sequence actually exists."""
    rawdna.upper()
    if 'N' in rawdna:
        return 1
    else:
        return 0


program_run = True

while program_run:
    selection = input("Press ENTER to continue or q to exit the program! ")
    time.sleep(0.2)
    if str.lower(selection) == 'q':
        print("\nExiting the program...")
        exit()
    else:
        print()
        print("------------------------------------IMPORTANT!--------------------------------------------")
        print("First part of the analysis is obtaining the DNA of choice!")
        time.sleep(0.2)
        print("You will be asked to provide the tool with the chromosome number and the location on the\n"
              "chromosome where the variant is located as well as the length of the region where it occurs!")
        input("Go to https://franklin.genoox.com/clinical-db/home to get the location of the variant of\n"
              "interest on the chromosome. Press ENTER to continue!")
        while True:
            try:
                listOfLegal = ["1", "2", "3", "4", "5", "6",
                               "7", "8", "9", "10", "11", "12",
                               "13", "14", "15", "16", "17", "18",
                               "19", "20", "21", "22",
                               "X", "Y", "MT", "M"]
                chromosome = input("Enter the number of chromosome where the variant is located: ").upper()
                if chromosome in listOfLegal:
                    newList += [chromosome]
                    break
                else:
                    print("(x) Invalid input! " + chromosome)
                    time.sleep(0.2)
                    continue
            except ValueError:
                continue
        while True:
            try:
                location = int(input("Enter the location on the chromosome, where the variant is located: "))
                if location > 250:
                    newList += [location]
                    break
                else:
                    print("(x) The number of the location entered is too small!")
                    time.sleep(0.2)
                    continue
            except ValueError:
                print("(!) Please enter an integer!")
                continue
        while True:
            try:
                lengthOfNucleo = int(input("Enter the length of the region where the variant occurs: "))
                if lengthOfNucleo == 0:
                    print("(x) The length cannot be 0!")
                    continue
                else:
                    newList += [lengthOfNucleo]
                    break
            except ValueError:
                print("(!) Please enter an integer!")
                continue
        chromosome = newList[0]
        location = newList[1]
        lengthOfNucleo = newList[2]
        starting_location = location - 251
        ending_location = location + 250
        response = requests.get(
            "https://api.genome.ucsc.edu/getData/sequence?genome=hg19;chrom=chr{};start={};end={}".format(chromosome,
                                                                                                          starting_location,
                                                                                                          ending_location))
        raw_dna = response.json()["dna"]
        raw_dna.upper()
        if dnaCheckUp(raw_dna) != 0:
            print("\n(x) Wrong input regarding the chromosome or location! \nChromosome: chr" + str(
                chromosome) + " \nLocation: " + str(location))
            input("\nPress ENTER to start over! ")
            continue
        else:
            print(highlightDNAwithNuc(raw_dna, lengthOfNucleo), file=seqFile)
            seqFile.close()
            break
