import json

ground_truth_values_json = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/signature_removal_2/eval_signature_detector_lib/ground_truth_bbox.json'
signature_detector_values_json = '/Users/veersingh/Desktop/Internship/data-extraction/preprocessing/signature_removal_2/eval_signature_detector_lib/signature_detector_values.json'

gt = open(ground_truth_values_json,)
ground_truth_values = json.load(gt)
gt.close()

sd = open(signature_detector_values_json,)
signature_detector_values = json.load(sd)
sd.close()

iou_signature_detector_lib = dict()
for filename in ground_truth_values.keys():
    # load ground truth and calculated coordinate values
    xmin_gt = ground_truth_values[filename][0]
    ymin_gt = ground_truth_values[filename][1]
    xmax_gt = ground_truth_values[filename][2]
    ymax_gt = ground_truth_values[filename][3]

    xmin_sd = signature_detector_values[filename][0]
    ymin_sd = signature_detector_values[filename][1]
    xmax_sd = signature_detector_values[filename][2]
    ymax_sd = signature_detector_values[filename][3]

    # Calculate iou
    # ground truth and calculated bbox areas
    gt_bbox_area = (xmax_gt - xmin_gt) * (ymax_gt - ymin_gt)
    sig_det_bbox_area = (xmax_sd - xmin_sd) * (ymax_sd - ymin_sd)

    # Coordinates of intersection
    xmin_inter = max(xmin_gt, xmin_sd)
    ymin_inter = max(ymin_gt, ymin_sd)
    xmax_inter = min(xmax_gt, xmax_sd)
    ymax_inter = min(ymax_gt, ymax_sd)

    if xmax_inter < xmin_inter or ymax_inter < ymin_inter:
        iou = 0.0
    else:
        intersection_area = (xmax_inter - xmin_inter) * (ymax_inter -
                                                         ymin_inter)
        iou = intersection_area / float(gt_bbox_area + sig_det_bbox_area -
                                        intersection_area)
        iou = round(iou * 100, 2)

    # Print filename and iou %age
    print(f'{filename} --> {iou}% accurate')

    # add to dict
    iou_signature_detector_lib.update({
        filename: {
            "ground_truth": [xmin_gt, ymin_gt, xmax_gt, ymax_gt],
            "calculated": [xmin_sd, ymin_sd, xmax_sd, ymax_sd],
            "intersection": [xmin_inter, ymin_inter, xmax_inter, ymax_inter],
            "iou_in_percentage": iou
        }
    })

# writing json output
json_output = json.dumps(iou_signature_detector_lib, indent=4)
output_json_file = 'iou_signature_detector_library.json'
jsonFile = open(output_json_file, "w")
jsonFile.write(json_output)
jsonFile.close()
