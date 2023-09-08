import functions
import time
from progress.bar import IncrementalBar

seqStr = open("rawsequence.txt", "r")
seqStart = seqStr.read()
seq = seqStart.strip()
seq = seq.replace("\n", "")
reversedSeq = seq[::-1]

primerLeftStr = open("leftPrimer.txt", "r")
primerLeftStart = primerLeftStr.read()
primerLeft = primerLeftStart.strip()
leftReversed = primerLeft[::-1]

primerRightStr = open("rightPrimer.txt", "r")
primerRightStart = primerRightStr.read()
primerRight = primerRightStart.strip()
rightReversed = primerRight[::-1]

f = open("analysisFile.txt", 'r+')
f.truncate(0)
f = open("analysisFile.txt", "a")

newList = []

program_run = True

while program_run:
    input("This is the last step of the primer analysis. Press ENTER to continue!")
    time.sleep(0.2)
    if functions.leftPrimerAlign(primerRight, functions.GeneSwap(functions.ReverseSeq(
            functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                               functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed), seq),
                               seq)))) == 1:
        print("(x) Right primer sequence not found on the DNA sequence! ")
        time.sleep(0.2)
        print("\nExiting the program...")
        break
    else:
        if functions.rightPrimerAlign(functions.GeneSwap(leftReversed), functions.GeneSwap(functions.ReverseSeq(
                functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                                   functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed), seq),
                                   seq)))) == 1:
            print("(x) Left primer sequence not found on the DNA sequence! ")
            time.sleep(0.2)
            print("\nExiting the program...")
            break
        else:
            if functions.CheckIfLeftPrimerOverlapsTheCodon(
                    functions.findStartingPosOfLeftPrimer(primerLeft, seq) + len(
                        primerLeft),
                    functions.nucleotideStartingPosition(seq)) != 0:
                print("\n(x) ERROR (x)\n")
                print(
                    "(x) Your left primer sequence lies too close to the marked nucleotide(s),\n"
                    "please choose a different left primer.\n"
                    "\n(x)The left primer sequence should end at least 50 bp away from the starting\n"
                    "position of the marked nucleotide(s)!\n")
                print("- Ending position of the left primer sequence: " + str(
                    functions.findStartingPosOfLeftPrimer(primerLeft, seq) + len(primerLeft)))
                print("- Starting position of the marked nucleotide(s): " + str(
                    functions.nucleotideStartingPosition(seq)))
                time.sleep(0.2)
                print("\nExiting the program...")
                break
            else:
                if functions.CheckIfRightPrimerOverlapsTheCodon(
                        functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                             seq) - len(
                            functions.GeneSwap(rightReversed)),
                        functions.nucleotideEndingPosition(seq)) != 0:
                    print("\n(x) ERROR (x)\n")
                    print(
                        "(x) Your right primer sequence lies too close to the marked nucleotide(s),\n"
                        "please choose a different right primer.\n "
                        "\n(x) The right primer sequence should begin at least 50 bp away from the ending\n"
                        "position of the marked nucleotide(s)!\n")
                    print("- Starting position of the right primer sequence: " + str(
                        functions.findEndingPosOfRightPrimer(functions.GeneSwap(rightReversed),
                                                             seq) - len(
                            functions.GeneSwap(rightReversed))))
                    print("- Ending position of the marked nucleotide(s): " + str(
                        functions.nucleotideEndingPosition(seq)))
                    time.sleep(0.2)
                    print("\nExiting the program...")
                    break
                else:
                    print("[GENE_NAME] [DNA_CODE] [FIRST_NAME] [LAST_NAME]", file=f)
                    print("[GENE_NAME] [chromosome-location-Ref-Alt-zyg]", file=f)
                    print("[GENE_NAME] [TRANSCRIPT]", file=f)
                    print("\n[ RAW SEQUENCE ]:", file=f)
                    print(seq, file=f)
                    print("\nLength of the DNA sequence: "+str(len(functions.finalReversedSeq(primerLeft, primerRight,
                                                     functions.GeneSwap(functions.ReverseSeq(
                                                         functions.Trimming(functions.findStartingPosOfLeftPrimer(
                                                             primerLeft, seq),
                                                             functions.findEndingPosOfRightPrimer(
                                                                 functions.GeneSwap(rightReversed),
                                                                 seq), seq)))))) + " bp", file=f)
                    print("\n[ PRIMER SUMMARY ]:", file=f)
                    print("Left primer sequence: " + primerLeft, file=f)
                    newList += [primerLeft]
                    print("Left primer sequence length: " + str(
                        len(primerLeft)) + " bp", file=f)
                    newList += [str(len(primerLeft))]
                    print("Left primer GC content: " + str(
                        functions.GCcontent(primerLeft)) + " %", file=f)
                    newList += [str(functions.GCcontent(primerLeft))]
                    print("Melting temperature of the left primer: " + str(
                        functions.calculatingMeltingTemp(primerLeft)) + "°C", file=f)
                    newList += [str(functions.calculatingMeltingTemp(
                        primerLeft))]
                    print("Right primer sequence (N): " + primerRight, file=f)
                    newList += [primerRight]
                    print("Right primer sequence (C): " + functions.GeneSwap(
                        rightReversed), file=f)
                    newList += [functions.GeneSwap(rightReversed)]
                    print("Right primer sequence length: " + str(
                        len(functions.GeneSwap(rightReversed))) + " bp", file=f)
                    newList += [str(len(functions.GeneSwap(rightReversed)))]
                    print("Right primer GC content: " + str(
                        functions.GCcontent(primerRight)) + " %", file=f)
                    newList += [str(functions.GCcontent(primerRight))]
                    print("Melting temperature of the right primer: " + str(
                        functions.calculatingMeltingTemp(primerRight)) + "°C", file=f)
                    newList += [str(functions.calculatingMeltingTemp(primerRight))]
                    print(
                        "\n{Go to the https://genome.ucsc.edu/cgi-bin/hgPcr and perform the In-Silico PCR and paste it here!}\n",
                        file=f)
                    print(functions.finalReversedSeq(primerLeft, primerRight,
                                                     functions.GeneSwap(functions.ReverseSeq(
                                                         functions.Trimming(functions.findStartingPosOfLeftPrimer(
                                                             primerLeft, seq),
                                                             functions.findEndingPosOfRightPrimer(
                                                                 functions.GeneSwap(rightReversed),
                                                                 seq), seq)))), file=f)
                    newList += [functions.finalReversedSeq(primerLeft, primerRight,
                                                           functions.GeneSwap(functions.ReverseSeq(
                                                               functions.Trimming(
                                                                   functions.findStartingPosOfLeftPrimer(
                                                                       primerLeft, seq),
                                                                   functions.findEndingPosOfRightPrimer(
                                                                       functions.GeneSwap(
                                                                           rightReversed),
                                                                       seq),
                                                                   seq))))]
                    print("\n********************************************************************************", file=f)
                    f.close()
                    print()
                    bar = IncrementalBar('Loading', fill='#', max=len(newList),
                                         suffix='%(percent)d%%')
                    for item in newList:
                        bar.next()
                        time.sleep(0.05)
                    bar.finish()
                    print("\n(✓) DONE\n")
                    time.sleep(0.2)
                    if functions.GCcontent(
                            functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                                               functions.findEndingPosOfRightPrimer(
                                                   functions.GeneSwap(rightReversed),
                                                   seq),
                                               seq)) < 40:
                        print(
                            "(!) WARNING! GC content of the trimmed sequence is bellow 40 %.")
                        time.sleep(0.2)
                    if functions.GCcontent(
                            functions.Trimming(functions.findStartingPosOfLeftPrimer(primerLeft, seq),
                                               functions.findEndingPosOfRightPrimer(
                                                   functions.GeneSwap(rightReversed),
                                                   seq),
                                               seq)) > 60:
                        print(
                            "(!) WARNING! GC content of the trimmed sequence is above 60 %.")
                        time.sleep(0.2)
                    if functions.GCcontent(primerLeft) < 40:
                        print(
                            "(!) WARNING! GC content of your LEFT primer sequence is bellow 40 %.")
                        time.sleep(0.2)
                    if functions.GCcontent(primerLeft) > 60:
                        print(
                            "(!) WARNING! GC content of your LEFT primer sequence is above 60 %.")
                        time.sleep(0.2)
                    if functions.GCcontent(primerRight) < 40:
                        print(
                            "(!) WARNING! GC content of your RIGHT primer sequence is bellow 40 %.")
                        time.sleep(0.2)
                    if functions.GCcontent(primerRight) > 60:
                        print(
                            "(!) WARNING! GC content of your RIGHT primer sequence is above 60 %.")
                        time.sleep(0.2)
                    if functions.calculatingMeltingTemp(primerLeft) < 52:
                        print(
                            "(!) WARNING! Left primer melting temperature is bellow 52°C.")
                        time.sleep(0.2)
                    if functions.calculatingMeltingTemp(primerLeft) > 65:
                        print(
                            "(!) WARNING! Left primer melting temperature is above 65°C.")
                        time.sleep(0.2)
                    if functions.calculatingMeltingTemp(primerRight) < 52:
                        print(
                            "(!) WARNING! Right primer melting temperature is bellow 52°C.")
                        time.sleep(0.2)
                    if functions.calculatingMeltingTemp(primerRight) > 65:
                        print(
                            "(!) WARNING! Right primer melting temperature is above 65°C.")
                        time.sleep(0.2)
                    if abs(functions.calculatingMeltingTemp(
                            primerLeft) - functions.calculatingMeltingTemp(primerRight)) > 0.5:
                        print(
                            "(!) WARNING! The two melting temperatures are not 0.5°C within of each other.")
                    time.sleep(0.2)
                    print(
                        "==========================================================================================")
                    print(
                        "     ANALYSIS DONE! The results of the analysis have been saved to 'analysisFile.txt'.    ")
                    print(
                        "==========================================================================================")
                    break
