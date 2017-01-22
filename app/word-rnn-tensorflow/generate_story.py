import subprocess

def partition(context, model):
    args = "python3 story_partition.py \"" + context + "\" \"" + model + "\""
    print(args)
    return subprocess.getoutput(args)

def optimal(context, paragraph):
    return paragraph.split(".")[1] + "."
    # return paragraph

def generate(context):
    print("generating....")
    story = ""

    print("generating beg")
    story += optimal(context, partition(context, "model/beg"))

    print("generating mid")
    story += optimal(context, partition(context, "model/mid"))

    print("generating end")
    story += optimal(context, partition(context, "model/end"))
    return story
