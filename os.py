from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def fifo(pages, frames):
    memory = []
    steps = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            status = "Fault"
        else:
            status = "Hit"

        steps.append({
            "page": page,
            "memory": memory.copy(),
            "status": status
        })

    return steps, faults


def lru(pages, frames):
    memory = []
    recent = []
    steps = []
    faults = 0

    for page in pages:
        if page not in memory:
            faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            status = "Fault"
        else:
            recent.remove(page)
            status = "Hit"

        recent.append(page)

        steps.append({
            "page": page,
            "memory": memory.copy(),
            "status": status
        })

    return steps, faults


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    pages = list(map(int, data["pages"].split()))
    frames = int(data["frames"])
    algorithm = data["algorithm"]

    if algorithm == "FIFO":
        steps, faults = fifo(pages, frames)
    else:
        steps, faults = lru(pages, frames)

    return jsonify({
        "steps": steps,
        "faults": faults
    })


if __name__ == "__main__":
    app.run(debug=True)
