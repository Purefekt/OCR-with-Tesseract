import json
import matplotlib.pyplot as plt

iou_signature_detector_library_json = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/signature_removal_2/eval_signature_detector_lib/iou_signature_detector_library.json'

f = open(iou_signature_detector_library_json,)
iou_signature_detector_library_json_data = json.load(f)
f.close()

zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty, forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy,\
seventy_to_eighty, eighty_to_ninety, ninety_to_hundered = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for filename in iou_signature_detector_library_json_data.keys():
    if iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 10:
        zero_to_ten = zero_to_ten + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 20:
        ten_to_twenty = ten_to_twenty + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 30:
        twenty_to_thirty = twenty_to_thirty + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 40:
        thirty_to_forty = thirty_to_forty + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 50:
        forty_to_fifthy = forty_to_fifthy + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 60:
        fifthy_to_sixty = fifthy_to_sixty + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 70:
        sixty_to_seventy = sixty_to_seventy + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 80:
        seventy_to_eighty = seventy_to_eighty + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] < 90:
        eighty_to_ninety = eighty_to_ninety + 1
    elif iou_signature_detector_library_json_data[filename][
            'iou_in_percentage'] <= 100:
        ninety_to_hundered = ninety_to_hundered + 1

# Plot
x_axis_labels = [
    '0%-10%', '10%-20%', '20%-30%', '30%-40%', '40%-50%', '50%-60%', '60%-70%',
    '70%-80%', '80%-90%', '90%-100%'
]
frequency = [
    zero_to_ten, ten_to_twenty, twenty_to_thirty, thirty_to_forty,
    forty_to_fifthy, fifthy_to_sixty, sixty_to_seventy, seventy_to_eighty,
    eighty_to_ninety, ninety_to_hundered
]

fig = plt.figure(figsize=(15, 5))

# creating the bar plot
plt.bar(x_axis_labels, frequency, color='maroon', width=0.4)

plt.xlabel('Distribution')
plt.ylabel('Frequency')
plt.show()
