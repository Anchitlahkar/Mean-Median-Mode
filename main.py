import pandas as pd
from collections import Counter

df = pd.read_csv("SOCR-HeightWeight.csv")

weightList = df["Weight(Pounds)"].tolist()
totalPeople = len(weightList)


def mean():
    total = 0

    for i in weightList:
        total += i

    mean = total/totalPeople

    print('Mean :',mean)


def median():
    weightList.sort()

    if totalPeople % 2 == 0:
        md1 = weightList[totalPeople // 2]
        md2 = weightList[totalPeople // 2 + 1]
        median = (md1+md2)/2
        print('Median: ',median)

    else:
        median = weightList[totalPeople // 2 + 1]
        print('Median: ',median)


def mode():
    countData = Counter(weightList)

    modeDataRange = {
        '90-100': 0,
        '100-110': 0,
        '110-120': 0,
        '120-130': 0,
        '130-140': 0,
        '140-150': 0,
        '150-160': 0
    }

    for height, occurrance in countData.items():

        if 90 < float(height) < 100:
            modeDataRange['90-100'] += occurrance

        elif 100 < float(height) < 110:
            modeDataRange['100-110'] += occurrance

        elif 110 < float(height) < 120:
            modeDataRange['110-120'] += occurrance

        elif 120 < float(height) < 130:
            modeDataRange['120-130'] += occurrance

        elif 130 < float(height) < 140:
            modeDataRange['130-140'] += occurrance

        elif 140 < float(height) < 150:
            modeDataRange['140-150'] += occurrance

        elif 150 < float(height) < 160:
            modeDataRange['150-160'] += occurrance

    modeRange, modeOccurrance = 0, 0

    for range, occurrance in modeDataRange.items():
        if occurrance > modeOccurrance:
            modeRange, modeOccurrance = [
                int(range.split("-")[0]), int(range.split("-")[1])], occurrance
            # print(modeRange)

    # print(modeRange)

    mode = float((modeRange[0] + modeRange[1]) / 2)
    print('Mode: ',mode)


mean()
median()
mode()
