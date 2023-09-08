import math

codonTable = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
              "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
              "UAU": "Y", "UAC": "Y", "UAA": "STOP", "UAG": "STOP",
              "UGU": "C", "UGC": "C", "UGA": "STOP", "UGG": "W",
              "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
              "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
              "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
              "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
              "ACU": "I", "ACC": "T", "ACA": "T", "ACG": "T",
              "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
              "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
              "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
              "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
              "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


def CheckRawSeq(seq):
    """Checking whether the nucleotide/codon is highlighted using two '_' signs in the DNA sequence."""
    if seq == 1:
        return 1
    else:
        seq = seq.upper()
        counter = 0
        for nuc in seq:
            if nuc == '_':
                counter += 1
        if counter == 2:
            return 0
        else:
            return 1


def GeneSwap(seq):
    """This function is used to generate the complementary sequence of the DNA sequence or primer sequences. """
    seq = seq.upper()
    comp = ""
    for nuc in seq:
        if nuc == 'A':
            comp += 'T'
        elif nuc == 'T':
            comp += 'A'
        elif nuc == 'G':
            comp += 'C'
        elif nuc == 'C':
            comp += 'G'
        elif nuc == '_':
            comp += '_'
    if len(comp) == len(seq):
        return comp.upper()
    else:
        return 1


def GCcontent(seq):
    """Function which calculates the GC content of DNA sequence or primer sequences."""
    seq = seq.upper()
    a = 0
    t = 0
    c = 0
    g = 0
    for nuc in seq:
        if nuc == 'C':
            c += 1
        if nuc == 'G':
            g += 1
        if nuc == 'A':
            a += 1
        if nuc == 'T':
            t += 1
    return round(((c + g) / (a + t + c + g)) * 100, 2)


def calculatingMeltingTemp(primer):
    """Function which calculates the melting temperature of both primer sequences."""
    primer = primer.upper()
    a = 0
    t = 0
    c = 0
    g = 0
    for nuc in primer:
        if nuc == 'A':
            a += 1
        if nuc == 'T':
            t += 1
        if nuc == 'C':
            c += 1
        if nuc == 'G':
            g += 1
    tM1 = 64.9 + (41 * (g + c - 16.4) / (a + t + g + c))
    tM2 = 100.5 + ((41 * (g + c)) / (a + t + c + g)) - (820 / (a + t + c + g)) + (16.6 * (math.log10(0.05)))
    tM3 = 81.5 + (0.41 * (((g + c) / (a + t + c + g)) * 100)) - (675 / (a + t + c + g))
    tM = (tM1 + tM2 + tM3) / 3
    return round(tM, 2)


def findStartingPosOfLeftPrimer(primer, seq):
    """Function which finds the starting position of the left primer sequence on the DNA sequence."""
    seq = seq.upper()
    primer = primer.upper()
    for nuc in range(len(seq)):
        if seq[nuc:].startswith(primer):
            return int(nuc)
        else:
            continue


def findEndingPosOfRightPrimer(primer, seq):
    """Function which finds the ending position of the right primer sequence on the DNA sequence."""
    seq = seq.upper()
    primer = primer.upper()
    for nuc in range(len(seq)):
        if seq[nuc:].startswith(primer):
            return int(nuc + len(primer))
        else:
            continue


def leftPrimerAlign(primer, seq):
    """Function which produces the standalone right primer sequence with the same length as the DNA sequence.
    (only for visualization in the final report)"""
    primer = primer.upper()
    seq = seq.upper()
    primer = primer.ljust(len(seq), '|')
    alignment = ""
    for nuc in range(0, len(primer)):
        if primer[nuc] == seq[nuc]:
            alignment += primer[nuc]
        else:
            alignment += '|'
    if alignment == primer:
        return alignment
    else:
        return 1


def rightPrimerAlign(primer, seq):
    """Function which produces the standalone left primer sequence with the same length as the DNA sequence.
        (only for visualization in the final report)"""
    primer = primer.upper()
    seq = seq.upper()
    primer = primer[::-1]
    primer = primer.ljust(len(seq), '|')
    primer = primer[::-1]
    alignment = ""
    for nuc in range(0, len(primer)):
        if primer[nuc] == seq[nuc]:
            alignment += primer[nuc]
        else:
            alignment += '|'
    if alignment == primer:
        return alignment
    else:
        return 1


def Trimming(startingPos, endingPos, seq):
    """Function which trims the raw DNA sequence, from the starting position of the left primer sequence
    to the ending position of the right primer sequence. """
    realStartingPos = startingPos
    realEndingPos = endingPos
    seq = seq.upper()
    return seq[realStartingPos:realEndingPos]


def ReverseSeq(seq):
    """Function which generates the reverse sequence of the DNA sequence or primer sequences."""
    if len(seq) == 0:
        return seq
    else:
        return seq[::-1]


def nucleotideStartingPosition(seq):
    """Function which finds the starting position of the nucleotide/codon that has been marked prior to the start
    of the analysis."""
    seq = seq.upper()
    startingPos = 0
    for nuc in range(len(seq)):
        if seq[nuc] == "_":
            startingPos += nuc
            break
    return int(startingPos)


def nucleotideEndingPosition(seq):
    """Function which finds the ending position of the nucleotide/codon that has been marked prior to the start
    of the analysis. """
    seq = seq.upper()
    endingPos = 0
    for nuc in reversed(range(len(seq))):
        if seq[nuc] == "_":
            endingPos += nuc - 1
            break
    return int(endingPos)


def nucleotideLength(startingPos, endingPos):
    """Function which provides us the length of the nucleotide/codon that has been marked prior to the start
    of the analysis."""
    return int(endingPos - startingPos)


def CodonSeq(seq):
    """Function which provides us the nucleotide/codon reversed sequence."""
    seq = seq.upper()
    counter = 0
    codonSeq = ""
    for nuc in seq:
        if nuc == "_":
            counter += 1
        if counter == 1:
            codonSeq += nuc
        if counter == 2:
            break
    return codonSeq[1:]


def CheckIfLeftPrimerOverlapsTheCodon(endingPosLeft, startingPosCodon):
    """Function to check whether the left primer sequence lies too close to the marked nucleotide/codon."""
    if endingPosLeft + 49 < startingPosCodon:
        return 0
    else:
        return 1


def CheckIfRightPrimerOverlapsTheCodon(startingPosRight, endingPosCodon):
    """Function to check whether the right primer sequence lies too close to the marked nucleotide/codon."""
    if startingPosRight - 49 > endingPosCodon:
        return 0
    else:
        return 1


def finalReversedSeq(leftPrimer, rightPrimer, seq):
    """Function which generates a sequence combining DNA sequence in lower case in between both primers which are
    written in upper case and marked nucleotide/codon."""
    leftPrimer = leftPrimer.upper()
    rightPrimer = rightPrimer.upper()
    seq = seq.upper()
    leftPrimerR = leftPrimer[::-1]
    primerL = GeneSwap(leftPrimerR)
    primerL = primerL[::-1]
    finalSeqR = ""
    finalSeqL = ""
    newSeq1 = ""
    codon = ""
    newSeq2 = ""
    newList = []
    for nuc in range(len(seq)):
        if seq[nuc:].startswith(rightPrimer):
            finalSeqR += rightPrimer
    seq = seq[::-1]
    for nuc in range(len(seq)):
        if seq[nuc:].startswith(primerL):
            finalSeqL += primerL
    seq = seq[::-1]
    for nuc in range(len(finalSeqR), len(seq)):
        if seq[nuc] != '_':
            newSeq1 += seq[nuc]
        else:
            break
    for nuc in range((len(finalSeqR) + len(newSeq1) + 1), len(seq)):
        if seq[nuc] != '_':
            codon += seq[nuc]
        else:
            break
    for nuc in range(len(finalSeqR) + len(newSeq1) + 1 + len(codon) + 1, (len(seq) - len(finalSeqL))):
        if seq[nuc] != '_':
            newSeq2 += seq[nuc]
        else:
            break

    finalSeqL = finalSeqL[::-1]
    newList += [finalSeqR]
    newList += [newSeq1.lower()]
    newList += [codon]
    newList += [newSeq2.lower()]
    newList += [finalSeqL]

    final = ''.join(newList)
    return final


if __name__ == '__main__':
    print("Testing...")
