import functools

# import itertools
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


# Function which takes in 2 hand strings and converts them to an array of 5 numbers, which has converted all face cards to numbers
def convertHand(hand):
    hand_arr = [0] * len(hand)
    for i in range(len(hand)):
        if hand[i] == "T":
            hand_arr[i] = 10
        elif hand[i] == "J":
            hand_arr[i] = 11
        elif hand[i] == "Q":
            hand_arr[i] = 12
        elif hand[i] == "K":
            hand_arr[i] = 13
        elif hand[i] == "A":
            hand_arr[i] = 14
        else:
            hand_arr[i] = int(hand[i])
    return hand_arr


# h1 = convertHand("2345T")
# h2 = convertHand("JJJ23")
# print(h1, h2)


# Function which takes in 2 hand arrays and returns 1 if hand1 wins, -1 if hand2 wins, and 0 if tie
def compare_hands(hand1, hand2):
    # Check for hand type
    hand1_card_counts = [0] * 15
    hand2_card_counts = [0] * 15
    for card in hand1:
        hand1_card_counts[card] += 1
    for card in hand2:
        hand2_card_counts[card] += 1

    hand1_card_counts.sort(reverse=True)
    hand2_card_counts.sort(reverse=True)
    # print(hand1_card_counts)
    # print(hand2_card_counts)
    if hand1_card_counts[0] > hand2_card_counts[0]:
        return 1
    elif hand1_card_counts[0] < hand2_card_counts[0]:
        return -1
    else:
        for i in range(5):
            if hand1_card_counts[i] > hand2_card_counts[i]:
                return 1
            elif hand1_card_counts[i] < hand2_card_counts[i]:
                return -1
        # Both hands have same type
        for i in range(5):
            if hand1[i] > hand2[i]:
                return 1
            elif hand1[i] < hand2[i]:
                return -1
        return 1  # Shouldn't occur according to rules, means hands are identical. Just return 1


# print(compare_hands(h1, h2))

hands_to_sort = []
hand_and_bid = []
for line in lines:
    hand, bid = line.split()
    hand = convertHand(hand)
    bid = int(bid)

    hands_to_sort.append(hand)
    hand_and_bid.append((hand, bid))

hands_to_sort.sort(key=functools.cmp_to_key(compare_hands))
# print(hands_to_sort)

# iterate through sorted hands, and for each one find its corresponding bid
# then multiply the bid by the index of the hand in the sorted list + 1
total = 0
for i in range(len(hands_to_sort)):
    total += hand_and_bid[i][1] * (hands_to_sort.index(hand_and_bid[i][0]) + 1)
print(total)
