"""Script for calculating control number of Land and Mortgage Registry."""

# create multipliers list [1, 3, 7, 1, 3, 7, 1, 3, 7, 1, 3, 7]
multipliers = [n for n in range(1,9,2) if n != 5] * 4
ascii_dict = {
            88: '10', 65: '11', 66: '12', 67: '13', 68: '14', 69: '15', 70: '16',
            71: '17', 72: '18', 73: '19', 74: '20', 75: '21', 76: '22', 77: '23',
            78: '24', 79: '25', 80: '26', 82: '27', 83: '28', 84: '29', 85: '30',
            87: '31', 89: '32', 90: '33'
            }


def get_control_number(land_reg_id: str, court: str) -> int:
    """Calculate control number based on land and mortgage register number and court department code."""
    combination = []
    for value in court:
        translated = value.translate(ascii_dict)  # replace each court  character based on ascii_dict
        combination.append(int(translated))  # add encoded values to combination list

    splitted_id = [int(i) for i in str(land_reg_id)]  # convert land_reg_id string into list of integers

    for number in splitted_id:
        combination.append(number)  # add every number to the combination from previously splitted id

    result = [combination[i] * multipliers[i] for i in range(len(combination))]  # multiply combination list by list of multipliers
    combination_sum = sum(result)  # sum each value of the list

    control_number = combination_sum % 10
    return control_number

