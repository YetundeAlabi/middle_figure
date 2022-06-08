def middle_figure(a, b):
    combined_string = (a + b).replace(" ", "")
    if len(combined_string) % 2 == 1:
        middle_element = combined_string[(len(combined_string) // 2)]
        return f"middle figure: {middle_element}"
    else:
        return "no middle figure"

# print(middle_figure("make love", "not wars")) ----> e
# print(middle_figure("python", "code")) -----> no middle figure
