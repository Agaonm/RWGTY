document.getElementById("translateBtn").onclick = function() {translate()};

async function translate() {
    var result;
    await fetch('http://127.0.0.1:8000/' + document.getElementById("sentence").value)
    .then(response => response.json())
    .then(data => result = data)
    .then(() => console.log(result))
    .then(() => document.getElementById("sentenceTrans").innerText = result)
}


