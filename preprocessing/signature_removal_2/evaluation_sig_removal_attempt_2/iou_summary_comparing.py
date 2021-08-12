import json
import matplotlib.pyplot as plt

iou_json = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/signature_removal/evaluation_sig_removal/iou.json'
iou_attempt_2_json = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/signature_removal_2/evaluation_sig_removal_attempt_2/iou_attempt_2.json'

f = open(iou_json,)
iou_data_json = json.load(f)
f.close()

f = open(iou_attempt_2_json,)
iou_attempt_2_data_json = json.load(f)
f.close()

zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty, forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy,\
seventy_to_eighty, eighty_to_ninety, ninety_to_hundered = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for filename in iou_data_json.keys():
    if iou_data_json[filename]['iou_in_percentage'] < 10:
        zero_to_ten = zero_to_ten + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 20:
        ten_to_twenty = ten_to_twenty + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 30:
        twenty_to_thirty = twenty_to_thirty + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 40:
        thirty_to_forty = thirty_to_forty + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 50:
        forty_to_fifthy = forty_to_fifthy + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 60:
        fifthy_to_sixty = fifthy_to_sixty + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 70:
        sixty_to_seventy = sixty_to_seventy + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 80:
        seventy_to_eighty = seventy_to_eighty + 1
    elif iou_data_json[filename]['iou_in_percentage'] < 90:
        eighty_to_ninety = eighty_to_ninety + 1
    elif iou_data_json[filename]['iou_in_percentage'] <= 100:
        ninety_to_hundered = ninety_to_hundered + 1

# Plot
x_axis_labels_attempt_1 = [
    '0%-10%', '10%-20%', '20%-30%', '30%-40%', '40%-50%', '50%-60%', '60%-70%',
    '70%-80%', '80%-90%', '90%-100%'
]
frequency_attempt_1 = [
    zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty,
    forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy, seventy_to_eighty,
    eighty_to_ninety, ninety_to_hundered
]

zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty, forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy,\
seventy_to_eighty, eighty_to_ninety, ninety_to_hundered = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for filename in iou_attempt_2_data_json.keys():
    if iou_attempt_2_data_json[filename]['iou_in_percentage'] < 10:
        zero_to_ten = zero_to_ten + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 20:
        ten_to_twenty = ten_to_twenty + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 30:
        twenty_to_thirty = twenty_to_thirty + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 40:
        thirty_to_forty = thirty_to_forty + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 50:
        forty_to_fifthy = forty_to_fifthy + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 60:
        fifthy_to_sixty = fifthy_to_sixty + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 70:
        sixty_to_seventy = sixty_to_seventy + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 80:
        seventy_to_eighty = seventy_to_eighty + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] < 90:
        eighty_to_ninety = eighty_to_ninety + 1
    elif iou_attempt_2_data_json[filename]['iou_in_percentage'] <= 100:
        ninety_to_hundered = ninety_to_hundered + 1

# Plot
x_axis_labels_attempt_2 = [
    '0%-10%', '10%-20%', '20%-30%', '30%-40%', '40%-50%', '50%-60%', '60%-70%',
    '70%-80%', '80%-90%', '90%-100%'
]
frequency_attempt_2 = [
    zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty,
    forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy, seventy_to_eighty,
    eighty_to_ninety, ninety_to_hundered
]

print(x_axis_labels_attempt_1)
print(x_axis_labels_attempt_2)
print(frequency_attempt_1)
print(frequency_attempt_2)


fig = plt.figure(figsize=(15, 10))
plt.subplot(2,1,1)
attempt_1 = plt.bar(x_axis_labels_attempt_1, frequency_attempt_1, color='maroon', width=0.4)

plt.xlabel('Distribution')
plt.ylabel('Frequency')

plt.subplot(2,1,2)
attempt_2 =plt.bar(x_axis_labels_attempt_2, frequency_attempt_2, color='maroon', width=0.4)

plt.xlabel('Distribution')
plt.ylabel('Frequency')
plt.show()
