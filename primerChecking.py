import time

left = open("leftPrimer.txt", "r+")
left.truncate(0)
left = open("leftPrimer.txt", "a")

right = open("rightPrimer.txt", "r+")
right.truncate(0)
right = open("rightPrimer.txt", "a")

def CheckPrimerContent(primer):
    """Checking whether the primer sequences include any illegal characters."""
    primer = primer.upper()
    counter = 0;
    for nuc in primer:
        if nuc == 'A' or nuc == 'C' or nuc == 'T' or nuc == 'G':
            counter += 0
        else:
            counter += 1
    return counter

program_runs = True

while program_runs:
    input("Next step is selecting the left primer and right primer sequences!\n"
          "Press ENTER to continue!  ")
    time.sleep(0.2)
    while True:
        try:
            while True:
                leftPrimer = input("\nCopy the selected left primer sequence! ")
                if len(leftPrimer) != 0:
                    break
                else:
                    print("(x) You have forgot to select the Left primer sequence!")
                    continue
            while True:
                rightPrimer = input("Copy the selected right primer sequence! ")
                if len(rightPrimer) != 0:
                    break
                else:
                    print("(x) You have forgot to select the Right primer sequence! ")
                    continue
            if CheckPrimerContent(leftPrimer) == 0 and CheckPrimerContent(rightPrimer) == 0 and len(leftPrimer) != 0 and len(rightPrimer) != 0:
                print(leftPrimer.upper(), file=left)
                print(rightPrimer.upper(), file=right)
                break
            else:
                print("\n(x) Illegal characters in primer sequences! Select the sequences again.\n")
                time.sleep(0.2)
        except ValueError:
            continue
    break
