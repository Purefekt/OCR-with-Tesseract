import json


def get_evaluation_json(ground_truth_values_json, calculated_values_json,
                        output_json_name):
    f = open(ground_truth_values_json,)
    ground_truth_values = json.load(f)
    f.close()

    f = open(calculated_values_json,)
    calculated_values = json.load(f)
    f.close()

    iou_dict = dict()
    for filename in ground_truth_values.keys():
        # load ground truth and calculated coordinate values
        xmin_gt = ground_truth_values[filename][0]
        ymin_gt = ground_truth_values[filename][1]
        xmax_gt = ground_truth_values[filename][2]
        ymax_gt = ground_truth_values[filename][3]

        xmin_c = calculated_values[filename][0]
        ymin_c = calculated_values[filename][1]
        xmax_c = calculated_values[filename][2]
        ymax_c = calculated_values[filename][3]

        # Calculate iou
        # ground truth and calculated bbox areas
        gt_bbox_area = (xmax_gt - xmin_gt) * (ymax_gt - ymin_gt)
        calc_bbox_area = (xmax_c - xmin_c) * (ymax_c - ymin_c)

        # Coordinates of intersection
        xmin_inter = max(xmin_gt, xmin_c)
        ymin_inter = max(ymin_gt, ymin_c)
        xmax_inter = min(xmax_gt, xmax_c)
        ymax_inter = min(ymax_gt, ymax_c)

        if xmax_inter < xmin_inter or ymax_inter < ymin_inter:
            iou = 0.0
        else:
            intersection_area = (xmax_inter - xmin_inter) * (ymax_inter -
                                                             ymin_inter)
            iou = intersection_area / float(gt_bbox_area + calc_bbox_area -
                                            intersection_area)
            iou = round(iou * 100, 2)

        # Print filename and iou %age
        print(f'{filename} --> {iou}% accurate')

        # add to dict
        iou_dict.update({
            filename: {
                "ground_truth": [xmin_gt, ymin_gt, xmax_gt, ymax_gt],
                "calculated": [xmin_c, ymin_c, xmax_c, ymax_c],
                "intersection": [
                    xmin_inter, ymin_inter, xmax_inter, ymax_inter
                ],
                "iou_in_percentage": iou
            }
        })

    # writing json output
    json_output = json.dumps(iou_dict, indent=4)
    output_json_file = output_json_name
    jsonFile = open(output_json_file, "w")
    jsonFile.write(json_output)
    jsonFile.close()


def evaluate_method_1():
    ground_truth_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_bbox.json'
    calculated_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/calculated_bbox_1.json'
    output_json_name = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/iou_1.json'

    get_evaluation_json(ground_truth_values_json, calculated_values_json,
                        output_json_name)


def evaluate_method_2():
    ground_truth_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_bbox.json'
    calculated_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/calculated_bbox_2.json'
    output_json_name = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/iou_2.json'

    get_evaluation_json(ground_truth_values_json, calculated_values_json,
                        output_json_name)


def evaluate_method_3():
    ground_truth_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/ground_truth_bbox.json'
    calculated_values_json = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/calculated_bbox_3.json'
    output_json_name = '/Users/veersingh/Desktop/docs_with_signs_dataset(tobacco800)/iou_3.json'

    get_evaluation_json(ground_truth_values_json, calculated_values_json,
                        output_json_name)


# evaluate_method_1()
# evaluate_method_2()
# evaluate_method_3()
