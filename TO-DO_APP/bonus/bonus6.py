contents = ["All carrots are to be sliced longitudinal.",
            "The carrots were reportedly sliced.",
            "The slicing proces was well presented."]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]


for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)
