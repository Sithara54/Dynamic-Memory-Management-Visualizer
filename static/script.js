function simulate() {
    const frames = document.getElementById("frames").value;
    const pages = document.getElementById("pages").value;
    const algorithm = document.getElementById("algorithm").value;

    fetch("/simulate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ frames, pages, algorithm })
    })
    .then(res => res.json())
    .then(data => {
        let html = "<table>";
        html += "<tr><th>Page</th><th>Memory</th><th>Status</th></tr>";

        data.steps.forEach(step => {
            html += `
                <tr>
                    <td>${step.page}</td>
                    <td>${step.memory.join(" | ")}</td>
                    <td>${step.status}</td>
                </tr>
            `;
        });

        html += "</table>";
        html += `<h3>Total Page Faults: ${data.faults}</h3>`;

        document.getElementById("result").innerHTML = html;
    });
}
