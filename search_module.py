

## поиск совпадений
def search_for_matches(request):
    i = 0
    j = 1
    global length_array
    global array_overlap_str
    length_array = 0
    array_overlap_str.clear()
    while i < len(bd_start):
        overlap = fuzz.token_set_ratio(bd_start.at[i, 'task_text']+ str(bd_start.at[i, 'exam level']) + " " + str(
            bd_start.at[i, 'year']) + " " + str(bd_start.at[i, 'autor']) + " " + str(
            bd_start.at[i, 'variant']) + " " + str(bd_start.at[i, 'job_number']), request)
        if overlap > degree_of_overlap:
            array_overlap_str.append(i)
            j = j + 1
        i = i + 1
    length_array = len(array_overlap_str)  # проверка совпадений через оценку длины массива
    return length_array, array_overlap_str