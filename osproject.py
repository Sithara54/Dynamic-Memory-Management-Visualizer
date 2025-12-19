from flask import Flask, render_template, request

app = Flask(__name__)

def fifo(pages, frames):
    memory = []
    result = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        result.append((page, memory.copy()))
    return result, faults


def lru(pages, frames):
    memory = []
    result = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
        result.append((page, memory.copy()))
    return result, faults


@app.route("/", methods=["GET", "POST"])
def index():
    output = []
    faults = 0

    if request.method == "POST":
        frames = int(request.form["frames"])
        pages = list(map(int, request.form["pages"].split()))
        algo = request.form["algo"]

        if algo == "FIFO":
            output, faults = fifo(pages, frames)
        else:
            output, faults = lru(pages, frames)

    return render_template("index.html", output=output, faults=faults)

if __name__ == "__main__":
    app.run(debug=True)
