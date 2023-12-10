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
            hand_arr[i] = 1
        elif hand[i] == "Q":
            hand_arr[i] = 12
        elif hand[i] == "K":
            hand_arr[i] = 13
        elif hand[i] == "A":
            hand_arr[i] = 14
        else:
            hand_arr[i] = int(hand[i])
    return hand_arr


# h1 = convertHand("T55J5")
# h2 = convertHand("KTJJT")
# print(h1, h2)


# Function which takes in 2 hand arrays and returns 1 if hand1 wins, -1 if hand2 wins, and 0 if tie (can't occur)
def compare_hands(hand1, hand2):
    # Check for hand type
    # This has extra indices and is missing 1 index, but it doesn't matter
    hand1_card_counts = [0] * 15
    hand2_card_counts = [0] * 15

    for card in hand1:
        hand1_card_counts[card] += 1
    for card in hand2:
        hand2_card_counts[card] += 1

    num_jokers_hand1 = hand1_card_counts[1]
    num_jokers_hand2 = hand2_card_counts[1]
    # set jokers to 0
    hand1_card_counts[1] = 0
    hand2_card_counts[1] = 0
    # print(num_jokers_hand1, num_jokers_hand2)

    hand1_card_counts.sort(reverse=True)
    hand2_card_counts.sort(reverse=True)
    # add jokers to hands most commonly occuring card. Full house doesn't have to be considered because best strategy of using jokers is still to use them on the most common card
    hand1_card_counts[0] += num_jokers_hand1
    hand2_card_counts[0] += num_jokers_hand2
    if hand1_card_counts[0] > hand2_card_counts[0]:
        return 1
    elif hand1_card_counts[0] < hand2_card_counts[0]:
        return -1
    else:
        for i in range(1, 5):
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


# print("comparing")
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
